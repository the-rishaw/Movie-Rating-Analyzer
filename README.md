
# 🎬 Movie Rating Analyzer

A Python-based desktop application to import, clean, analyze, and visualize movie rating datasets through a modern graphical user interface.

Built using **Python, CustomTkinter, Pandas, and Matplotlib**, this application transforms raw movie data into meaningful insights through statistical analysis and interactive visualizations.

---

## 📌 Overview

Movie Rating Analyzer is designed to make movie rating analysis simple and accessible. Users can import movie datasets in CSV format, automatically clean invalid records, explore movie information, compare genres, and visualize rating distributions.

The application follows an **Object-Oriented Programming (OOP)** approach, separating data management from the graphical interface for better code organization and maintainability.

## ✨ Features

### 📊 Interactive Dashboard
- View the total number of movies.
- Calculate the overall average rating.
- Identify the highest-rated movie.
- Identify the lowest-rated movie.
- Display the number of unique genres.
- View the number of skipped records.

### 📂 CSV Import & Data Cleaning
- Import movie datasets from CSV files.
- Validate required columns.
- Detect missing and empty values.
- Identify invalid or non-numeric ratings.
- Reject ratings outside the 0–10 range.
- Detect duplicate movie records.
- Keep track of skipped records and their reasons.

### 🎞️ Movie Management
- Browse imported movie records.
- Search movies by title.
- Filter movies by genre.
- View movie names, genres, and ratings.

### 📈 Statistical Analytics
- Calculate average ratings by genre.
- Find the highest and lowest ratings in each genre.
- Count movies belonging to each genre.
- Identify the best-performing genre.

### 📉 Data Visualization
- Genre-wise average rating bar chart.
- Movie rating distribution histogram.
- Graphical representation using Matplotlib.

### 📤 Data Export
- Export cleaned movie datasets.
- Export genre-wise analytical reports.
- Export skipped records with cleaning reasons.

### ⚙️ Appearance Settings
- Dark mode.
- Light mode.
- System appearance mode.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CustomTkinter | Modern desktop GUI |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| Tkinter | Native file dialogs and message boxes |
| CSV | Dataset format |

---

## 📁 Project Structure

```text
Movie-Rating-Analyzer/
│
├── .venv/                  # Virtual environment (not committed)
│
├── main.py                 # Main application
├── movies.csv              # Sample movie dataset
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignored files
```

---

## 🚀 Getting Started

Follow these instructions to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/the-rishaw/Movie-Rating-Analyzer.git
```

Navigate to the project directory:

```bash
cd Movie-Rating-Analyzer
```

### 2. Create a Virtual Environment

Make sure Python 3.10 or later is installed.

Create a virtual environment:

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` is not available, install the dependencies manually:

```bash
python -m pip install customtkinter pandas matplotlib
```

### 5. Run the Application

```bash
python main.py
```

---

## 📄 Dataset Format

The application accepts CSV files containing the following three required columns:

| Column | Description | Example |
|---|---|---|
| Movie | Movie title | Inception |
| Genre | Movie genre | SciFi |
| Rating | Movie rating between 0 and 10 | 8.8 |

### Sample Dataset

```csv
Movie,Genre,Rating
Inception,SciFi,8.8
Titanic,Romance,7.9
Interstellar,SciFi,8.6
The Dark Knight,Action,9.0
Avatar,SciFi,7.8
The Notebook,Romance,7.5
Gladiator,Action,8.5
Sholay,Action,10
```

You can use the included `movies.csv` file to test the application.

---

## 🧹 Data Cleaning Rules

The application validates every imported record before including it in the analysis.

| Condition | Action |
|---|---|
| Missing movie name | Skip record |
| Missing genre | Skip record |
| Missing rating | Skip record |
| Empty movie or genre | Skip record |
| Non-numeric rating | Skip record |
| Rating below 0 | Skip record |
| Rating above 10 | Skip record |
| Duplicate record | Skip duplicate |

Valid records are retained and used for statistical calculations and visualizations.

---

## 🧠 Object-Oriented Design

The application is organized into two main classes:

### 1. `MovieDataManager`

Responsible for:
- Loading CSV datasets.
- Cleaning and validating records.
- Calculating movie statistics.
- Generating genre-wise analytics.
- Exporting datasets and reports.

### 2. `MovieRatingAnalyzer`

Responsible for:
- Creating the main application window.
- Managing the graphical interface.
- Handling navigation between pages.
- Displaying movie data and analytics.
- Rendering charts.
- Handling user interactions.

This separation makes the application easier to understand, maintain, and extend.

---

## 🔄 Version Management

This project uses Git for version control and GitHub for source code hosting.

### Versioning Format

The project follows Semantic Versioning:

`MAJOR.MINOR.PATCH`

Example: `1.0.0`

- **MAJOR:** Major changes or incompatible updates.
- **MINOR:** New features and functionality.
- **PATCH:** Bug fixes and minor improvements.

### Git Workflow

```bash
# Check project changes
git status

# Stage changes
git add .

# Commit changes
git commit -m "Describe your changes"

# Push changes to GitHub
git push
```

---

## 🔮 Future Improvements

- Add, edit, and delete movie records.
- Sort movies by title, genre, and rating.
- Add advanced search and filtering.
- Support additional data formats such as Excel.
- Add rating distribution by genre.
- Add interactive charts and detailed reports.
- Add database integration for persistent storage.
- Improve the user interface and dashboard experience.

---

## 🎯 Project Objectives

- Understand practical implementation of Python programming.
- Apply Object-Oriented Programming concepts.
- Learn data processing using Pandas.
- Implement data validation and cleaning.
- Generate statistical insights from datasets.
- Visualize data using Matplotlib.
- Develop a desktop application using CustomTkinter.
- Practice Git and GitHub version management.

---

## 👨‍💻 Author

**Rishaw Kumar**

- GitHub: [@the-rishaw](https://github.com/the-rishaw)

---

## 📜 License

This project is open-source and available under the MIT License.

---

<p align="center">
  Made with ❤️ using Python
</p>
