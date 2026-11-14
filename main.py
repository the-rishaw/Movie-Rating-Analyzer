# GUI, data analysis, and charting libraries used by the application.
import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt

from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Shared font settings keep text styling consistent across the interface.
FONT_FAMILY = "ROBOTO"

FONT = {
    "default": (FONT_FAMILY, 13),
    "small": (FONT_FAMILY, 11),
    "medium": (FONT_FAMILY, 14),
    "large": (FONT_FAMILY, 18),
    "heading": (FONT_FAMILY, 28, "bold"),
    "subheading": (FONT_FAMILY, 20, "bold"),
    "button": (FONT_FAMILY, 13, "bold"),
    "card_value": (FONT_FAMILY, 25, "bold")
}

# --------------------------------------------------
# MOVIE DATA MANAGEMENT
# Handles CSV loading, data validation, cleaning, and statistics.
# --------------------------------------------------
class MovieDataManager:
    # Set up an empty dataset and track import/cleaning information.
    def __init__(self):
        self.df = pd.DataFrame(columns=["Movie", "Genre", "Rating"])
        self.skipped_rows = []
        self.loaded_file = None

    # Read the selected CSV file, check its required columns, and clean its records.
    def load_csv(self, file_path):
        try:
            # Load the CSV into a Pandas DataFrame for processing.
            raw_df = pd.read_csv(file_path)
            required_columns = ["Movie", "Genre", "Rating"]

            # Stop the import if any required column is missing.
            if not all(column in raw_df.columns for column in required_columns):
                raise ValueError(
                    "CSV must contain Movie, Genre and Rating columns."
                )

            self.clean_data(raw_df)
            self.loaded_file = file_path

            return True
        
        except Exception as error:
            messagebox.showerror("Import Error", str(error))
            return False

    # Keep valid records and record a reason for every skipped row.
    def clean_data(self, raw_df):
        cleaned_rows = []
        self.skipped_rows = []
        seen = set()

        # Examine each CSV row so invalid records can be identified individually.
        for index, row in raw_df.iterrows():

            row_number = index + 1 

            movie = row["Movie"]
            genre = row["Genre"]
            rating = row["Rating"]

            # Reject rows where any required field is missing.
            if pd.isna(movie) or pd.isna(genre) or pd.isna(rating):
                self.skipped_rows.append(
                    {"Row": row_number,
                     "Reason": "Missing value"}
                )
                continue

            movie = str(movie).strip()
            genre = str(genre).strip()

            # Reject rows with blank movie names or genre values.
            if not movie or not genre:
                self.skipped_rows.append(
                    {"Row": row_number,
                     "Reason": "Empty movie or genre"}
                )
                continue

            try:
                rating = float(rating)
            except (ValueError, TypeError):
                self.skipped_rows.append(
                    {"Row": row_number,
                     "Reason": "Invalid Rating"}
                )
                continue

            # Ratings must be between 0 and 10, inclusive.
            if not 0 <= rating <= 10:
                self.skipped_rows.append(
                    {"Row": row_number, "Reason": "Rating outside 0-10"}
                )
                continue

            # Build a normalized key to detect duplicate movie records.
            duplicate_key = (
                movie.casefold(),
                genre.casefold(),
                rating
            )

            # Skip a record if the same movie, genre, and rating were already seen.
            if duplicate_key in seen:
                self.skipped_rows.append(
                    {"Row": row_number, "Reason": "Duplicate record"}
                )
                continue

            seen.add(duplicate_key)

            # Add the validated record to the collection of accepted rows.
            cleaned_rows.append({
                "Movie": movie,
                "Genre": genre,
                "Rating": rating
            })

        # Replace the current dataset with the cleaned records.
        self.df = pd.DataFrame(
            cleaned_rows,
            columns=["Movie", "Genre", "Rating"]
        )

    # Calculate summary metrics and identify the highest- and lowest-rated movies.
    def get_statistics(self):
        if self.df.empty:
            return None

        return {
            "total": len(self.df),
            "average": self.df["Rating"].mean(),
            "highest": self.df.loc[self.df["Rating"].idxmax()],
            "lowest": self.df.loc[self.df["Rating"].idxmin()],
            "genres": self.df["Genre"].nunique()
        }

    # Group movies by genre and calculate rating metrics for each group.
    def get_genre_statistics(self):
        if self.df.empty:
            return pd.DataFrame()

        return self.df.groupby("Genre")["Rating"].agg(
            Average="mean",
            Count="count",
            Highest="max",
            Lowest="min"
        ).sort_values("Average", ascending=False)

    # Save the cleaned movie records to a CSV file.
    def export_cleaned_data(self, file_path):
        self.df.to_csv(file_path, index=False)

    # Save the genre-wise summary report to a CSV file.
    def export_genre_report(self, file_path):
        self.get_genre_statistics().to_csv(file_path)

    # Save the rejected row numbers and their validation reasons.
    def export_skipped_rows(self, file_path):
        pd.DataFrame(self.skipped_rows).to_csv(file_path, index=False)



# --------------------------------------------------
# MAIN APPLICATION AND USER INTERFACE
# Builds the desktop interface and connects it to MovieDataManager.
# --------------------------------------------------
class MovieRatingAnalyzer(ctk.CTk):
    # Configure the main window, initialize shared state, and show the dashboard.
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Movie Rating Analyzer")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        self.data_manager = MovieDataManager()

        self.current_page = "Dashboard"
        self.search_var = ctk.StringVar()
        self.genre_var = ctk.StringVar(value = "All Genres")
        # self.configure(fg_color="#ffffff")
        self.app_layout()
        self.dashboard_section()


    # Create the sidebar and the main content area of the application.
    def app_layout(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=200,
            corner_radius=10,
            fg_color="#1d2d4a"
        )

        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.sidebar.pack_propagate(True)

        self.main_layout = ctk.CTkFrame(
            self,
            width=1000,
            fg_color="#191b24"
        )

        self.main_layout.pack(side="right", fill="both", padx=(0, 10), pady=10, expand=True)

        self.app_sidebar()

    # Add the application title, page navigation buttons, and CSV import button.
    def app_sidebar(self):
        ctk.CTkLabel(
            self.sidebar,
            text="Movie Rating Analyzer",
            # text_color="Red",
            font=FONT["large"],
            fg_color="transparent"
        ).pack(padx=10, pady=10)

        pages = (
            "Dashboard",
            "Movies",
            "Analytics",
            "Charts",
        )

        for page in pages:
            ctk.CTkButton(
                self.sidebar,
                anchor="center",
                text=page,
                height=42,
                corner_radius=10,
                fg_color="transparent",
                hover_color="#293645",
                # fg_color="#2d2945",
                text_color="#dce1eb",
                font=FONT["button"],
                border_width=1,
                command=lambda p=page: self.navigation(p)
            ).pack(fill="x", padx=15, pady=4)

        ctk.CTkButton(
            self.sidebar,
            text="+ Import CSV",
            height=42,
            fg_color="#4968df",
            hover_color="#3652bd",
            command=self.import_csv
        ).pack(fill="x", padx=15, pady=(35, 10))
        
        ctk.CTkLabel(
            self.sidebar,
            text="Movie Rating Analyzer\nVersion 1.0",
            text_color="#777e8d",
            font=("Arial", 11)
        ).pack(side="bottom", pady=20)

    # Remove the widgets from the previous page before drawing the next page.
    def clear_page(self):
        for widget in self.main_layout.winfo_children():
            widget.destroy()

    # Display a consistent heading and subtitle at the top of a page.
    def create_title(self, title, subtitle):
        ctk.CTkLabel(
            self.main_layout,
            text=title,
            font=FONT["large"] + ("bold",),
            text_color="#C9CFD6"
        ).pack(anchor="w", padx=30, pady=(25,0))

        ctk.CTkLabel(
            self.main_layout,
            text=subtitle,
            font=FONT["medium"] + ("bold", ),
            text_color="#C9CFD6"
        ).pack(anchor='w', padx=30, pady=(0, 25))

    # Build a reusable card for presenting one statistic.
    def create_card(self, parent, title, value):
        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            fg_color="#1d222c"
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=7,
            pady=7
        )

        ctk.CTkLabel(
            card,
            text=title,
            text_color="#9299a8",
            font=FONT["default"]
        ).pack(anchor="w", padx=18, pady=(18,5))

        ctk.CTkLabel(
            card,
            text=str(value),
            text_color="#ffffff",
            font=FONT["card_value"]
        ).pack(anchor="w", padx=18, pady=(0, 18))

        return card

    # Show guidance when a page has no data to display.
    def show_empty_message(self, message="Import a CSV file to get started."):
        ctk.CTkLabel(
            self.main_layout,
            text=message,
            font=FONT["medium"],
            text_color="#9299a8"
        ).pack(expand=True)

    # Remember the selected page and call its corresponding display method.
    def navigation(self, page):
        self.current_page = page
        pages_dict = {
            "Dashboard": self.dashboard_section,
            "Movies": self.movies_section,
            "Analytics": self.analytics_section,
            "Charts": self.charts_section
        }

        pages_dict[page]()



    # Ask the user to choose a CSV file, import it, and refresh the current page.
    def import_csv(self):
        selected_file_path = filedialog.askopenfilename(
            title = "Select a CSV File to Import",
            initialdir="~",
            filetypes=[('CSV Files', "*.csv")]
        )

        if not selected_file_path:
            return

        success = self.data_manager.load_csv(selected_file_path)

        if success:
            messagebox.showinfo(
                "Import Successful",
                f"Loaded {len(self.data_manager.df)} valid movies.\n" 
                f"Skipped {len(self.data_manager.skipped_rows)} rows."
            )
            self.navigation(self.current_page)

    # DASHBOARD SECTION: presents a summary of the imported movie dataset.
    #DASHBOARD SECTION

    # Display key totals and the highest-/lowest-rated movie highlights.
    def dashboard_section(self):
        self.clear_page()
        self.create_title("Dashboard", "Overview of your movie rating dataset.")

        # Request the overall statistics calculated by the data manager.
        stats = self.data_manager.get_statistics()

        if stats is None:
            self.show_empty_message()
            return

        # Group the statistic cards in one horizontal container.
        cards = ctk.CTkFrame(
            self.main_layout,
            fg_color="transparent"
        )
        cards.pack(fill="x", padx=20)

        self.create_card(cards, "Total Movies", stats["total"])
        self.create_card(cards, "Average Rating", f'{stats["average"]:.2f}')
        self.create_card(cards, "Genres", stats["genres"])
        self.create_card(cards, "Skipped Rows", len(self.data_manager.skipped_rows))

        details = ctk.CTkFrame(
            self.main_layout,
            fg_color="#1d222c",
            corner_radius=12
        )
        details.pack(fill="x", padx=27, pady=20)

        # Retrieve the movie records with the maximum and minimum ratings.
        highest = stats["highest"]
        lowest = stats["lowest"]

        ctk.CTkLabel(
            details,
            text="Rating Highlights",
            font=FONT["large"]
        ).pack(anchor="w", padx=20, pady=(18, 12))

        ctk.CTkLabel(
            details,
            text=f'Highest Rated: {highest["Movie"]} ({highest["Rating"]}/10)',
            font=FONT["medium"]
        ).pack(anchor="w", padx=20, pady=7)

        ctk.CTkLabel(
            details,
            text=f'Lowest Rated: {lowest["Movie"]} ({lowest["Rating"]}/10)',
            font=FONT["medium"]
        ).pack(anchor="w", padx=20, pady=7)

    # MOVIES SECTION: allows users to browse, search, and filter records.
    #MOVIES SECTION

    # Create the search/filter controls and the scrollable movie list.
    def movies_section(self):
        self.clear_page()
        self.create_title("Movies", "Browse, search and filter your movie collection.")

        df = self.data_manager.df

        if df.empty:
            self.show_empty_message()
            return

        controls = ctk.CTkFrame(
            self.main_layout,
            fg_color="transparent"
        )
        controls.pack(fill="x", padx=30, pady=5)

        search = ctk.CTkEntry(
            controls,
            placeholder_text="Search Movie...",
            textvariable=self.search_var,
            width=260
        )
        search.pack(side="left", padx=(0, 10))
        search.bind("<KeyRelease>", lambda event: self.display_movies())

        # Populate the genre selector using the genres present in the dataset.
        genres = ["All Genres"] + sorted(df['Genre'].unique().tolist())

        genre_menu = ctk.CTkOptionMenu(
            controls,
            values=genres,
            variable=self.genre_var,
            command=lambda value: self.display_movies()
        )
        genre_menu.pack(side="left")

        self.movie_list = ctk.CTkScrollableFrame(
            self.main_layout,
            fg_color="#191c23"
        )
        self.movie_list.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.display_movies()

    # Rebuild the visible movie list using the current search and genre selections.
    def display_movies(self):
        for widget in self.movie_list.winfo_children():
            widget.destroy()
        
        # Work on a copy so filtering does not modify the original dataset.
        df = self.data_manager.df.copy()
        
        # Normalize the search text to make matching case-insensitive.
        search_text = self.search_var.get().strip().casefold()
        
        if search_text:
            df = df[
                df["Movie"].str.casefold().str.contains(
                    search_text,
                    na=False
                )
            ]
        
        # Read the selected genre before applying the optional genre filter.
        selected_genre = self.genre_var.get()
        
        if selected_genre != "All Genres":
            df = df[df["Genre"] == selected_genre]
        
        # Create one display row for every movie that matches the filters.
        for _, row in df.iterrows():
        
            movie_row = ctk.CTkFrame(
                self.movie_list,
                fg_color="#252b36",
                corner_radius=8
            )
            movie_row.pack(fill="x", padx=5, pady=5)
        
            ctk.CTkLabel(
                movie_row,
                text=row["Movie"],
                font=("Arial", 14, "bold"),
                anchor="w"
            ).pack(side="left", padx=15, pady=14)
        
            ctk.CTkLabel(
                movie_row,
                text=row["Genre"],
                text_color="#9299a8"
            ).pack(side="right", padx=15)
        
            ctk.CTkLabel(
                movie_row,
                text=f'{row["Rating"]:.1f}/10',
                text_color="#70b7ff",
                font=("Arial", 13, "bold")
            ).pack(side="right", padx=15)
        
        # Inform the user when the current filters return no matching movies.
        if df.empty:
            ctk.CTkLabel(
                self.movie_list,
                text="No matching movies found.",
                text_color="#9299a8"
            ).pack(pady=30)

    # ANALYTICS SECTION: displays rating statistics grouped by genre.
    #ANALYTICS SECTION

    # Build a table containing each genre and its calculated rating metrics.
    def analytics_section(self):
        self.clear_page()
        self.create_title("Analytics", "Exlore movie genres rating and performances")

        stats = self.data_manager.get_genre_statistics()

        if stats.empty:
            self.show_empty_message()
            return

        table = ctk.CTkFrame(
            self.main_layout,
            fg_color="#1d222c",
            corner_radius=12
        )
        table.pack(fill="x", padx=30, pady=10)

        # Define the column labels used by the genre statistics table.
        headers = ["Genre", "Average", "Count", "Highest", "Lowest"]

        for column, heading in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=heading,
                font=FONT["medium"],
                text_color="#70b7ff"
            ).grid(row=0, column=column, padx=15, pady=15)

        # Convert each genre summary into values for one table row.
        for row_number, (genre, row) in enumerate(stats.iterrows(), start=1):
            values = [
                genre,
                f"{row['Average']:.2f}",
                int(row["Count"]),
                f"{row['Highest']:.1f}",
                f"{row['Lowest']:.1f}"

            ]

            for column, value in enumerate(values):

                ctk.CTkLabel(
                    table,
                    text=str(value),
                    font=FONT["default"]
                ).grid(
                    row=row_number,
                    column=column,
                    padx=15,
                    pady=12
                )

        # The genre table is sorted by average rating, so its first entry is highest.
        best_genre = stats.index[0]

        ctk.CTkLabel(
            self.main_layout,
            text=f"Best Performing Genre: {best_genre}",
            font=FONT["default"],
            text_color="#70b7ff"
        ).pack(anchor="w", padx=35, pady=25)

    # CHARTS SECTION: visualizes genre averages and the distribution of ratings.
    #CHARTS SECTION

    # Create and embed Matplotlib charts using the currently loaded movie data.
    def charts_section(self):
        self.clear_page()
        self.create_title("Charts", "Visual representation of your movie ratings.")

        df = self.data_manager.df

        if df.empty:
            self.show_empty_message()
            return 

        # Create two side-by-side plots in a single Matplotlib figure.
        figure, axes = plt.subplots(1, 2, figsize=(10, 4))
        figure.patch.set_facecolor("#191b23")

        # Calculate the average rating for each genre for the bar chart.
        genre_average = df.groupby('Genre')['Rating'].mean()

        # Compare average movie ratings across genres.
        axes[0].bar(genre_average.index, genre_average.values)
        axes[0].set_title("Average Rating by Genre", color="white")
        axes[0].set_ylabel("Rating", color="white")
        axes[0].tick_params(axis="x", colors="white")
        axes[0].tick_params(axis="y", color="white")

        # Show how frequently ratings occur across the 0–10 scale.
        axes[1].hist(
            df["Rating"],
            bins=10,
            edgecolor="white"
        )
        axes[1].set_title("Rating Distribution", color="white")
        axes[1].set_xlabel("Rating", color="white")
        axes[1].set_ylabel("Number of Movies", color="white")
        axes[1].tick_params(colors="white")

        figure.tight_layout()

        # Connect the Matplotlib figure to the Tkinter application window.
        canvas = FigureCanvasTkAgg(
            figure,
            master=self.main_layout
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill='both',
            expand=True,
            padx=20,
            pady=10
        )


# Start the desktop application when this file is run directly.
if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = MovieRatingAnalyzer()
    app.mainloop()