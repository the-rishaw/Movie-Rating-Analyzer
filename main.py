import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt

from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

class MovieRatingAnalyzer(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Movie Rating Analyzer")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        self.current_page = "Dashboard"
        # self.configure(fg_color="#ffffff")
        self.app_layout()
        self.dashboard_section()


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
            "Export",
            "Settings"
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
            command=self.import_csv()
        ).pack(fill="x", padx=15, pady=(35, 10))
        
        ctk.CTkLabel(
            self.sidebar,
            text="Movie Rating Analyzer\nVersion 1.0",
            text_color="#777e8d",
            font=("Arial", 11)
        ).pack(side="bottom", pady=20)

    def clear_page(self):
        for widget in self.main_layout.winfo_children():
            widget.destroy()

    def create_title(self, title, subtitle):
        ctk.CTkLabel(
            self.main_layout,
            text=title,
            font=FONT["large"] + ("bold",),
            text_color="#404852"
        ).pack(anchor="w", padx=30, pady=(25,0))

        ctk.CTkLabel(
            self.main_layout,
            text=subtitle,
            font=FONT["medium"] + ("bold", ),
            text_color="#404852"
        ).pack(anchor='w', padx=30, pady=(0, 25))

    def navigation(self, page):
        self.current_page = page
        pages_dict = {
            "Dashboar": self.dashboard_section,
            "Movies": self.movies_section,
            "Analytics": self.analytics_section,
            "Charts": self.charts_section,
            "Export": self.export_section,
            "Settings": self.settings_section
        }

        pages_dict[page]()

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
                f"Loaded {len(self.data_manager.df)} valid movies.\n",
                f"Skipped {len(self.data_manager.skipped_rows)} rows."
            )
            self.navigate(self.current_page)

    def dashboard_section(self):
        self.clear_page()
        self.create_title("Dashboard", "Overview of your movie rating dataset.")

    def movies_section(self):
        self.clear_page()
        self.create_title("Movies", "Browse, search and filter your movie collection.")

    def analytics_section(self):
        self.clear_page()
        self.create_title("Analytics", "This and that")

    def charts_section(self):
        self.clear_page()
        self.create_title("Charts", "This and that")

    def export_section(self):
        self.clear_page()
        self.create_title("Exports", "This and that epxorts")

    def settings_section(self):
        self.clear_page()
        self.create_title("Settings", "This and that settings")


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = MovieRatingAnalyzer()
    app.mainloop()