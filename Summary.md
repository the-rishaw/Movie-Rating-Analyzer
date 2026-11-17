# Movie Rating Analyzer – Project Summary

## 1. Project Overview

**Project Title:** Movie Rating Analyzer  
**Student Name:** Rishaw Kumar  
**Class:** B.Tech CSE(AIML) 
**Section:** J  
**Roll Number:** RU-26-02282
**Programming Language:** Python 3

### About the Project

Movie Rating Analyzer is a Python-based desktop application developed to analyze movie-rating datasets. It allows users to import movie data through CSV files, clean and validate the data, calculate useful statistics, and visualize movie ratings through an interactive graphical user interface.

The application helps users understand movie-rating patterns and compare ratings across different genres without manually processing large amounts of data.

The project uses Python libraries such as CustomTkinter, Pandas, and Matplotlib to provide an interactive and user-friendly experience.

---

## 2. Project Objectives

The main objectives of this project are:

- To develop a desktop application using Python.
- To understand and implement file handling using CSV files.
- To perform data cleaning and validation.
- To calculate useful statistics from movie datasets.
- To analyze movie ratings based on different genres.
- To represent data using charts and graphs.
- To apply Python programming concepts and object-oriented programming in a practical project.

---

## 3. Features and Functionality

### 3.1 CSV File Import

Users can import movie datasets using CSV files. The application reads the data and processes it for further analysis.

### 3.2 Data Cleaning and Validation

The application checks the imported dataset and handles invalid records.

The cleaning process includes:

- Skipping records with missing values.
- Removing records with empty movie names or genres.
- Skipping non-numeric ratings.
- Rejecting ratings outside the valid range of 0–10.
- Identifying and skipping duplicate records.
- Tracking skipped records and their reasons.

### 3.3 Dashboard

The dashboard displays an overview of the movie dataset through important statistics, such as:

- Total number of movies.
- Average movie rating.
- Highest-rated movie.
- Lowest-rated movie.
- Number of genres.

### 3.4 Movies Section

The Movies section allows users to explore the available movie records.

It provides functionality to:

- View movie information.
- Search for movies.
- Filter movies by genre.

### 3.5 Analytics Section

The Analytics section provides genre-wise statistical information, including:

- Average rating of each genre.
- Highest rating in each genre.
- Lowest rating in each genre.

This helps users compare movie ratings across different genres.

### 3.6 Charts and Data Visualization

The Charts section uses Matplotlib to represent the analyzed data visually.

It includes:

- Genre-wise average rating comparison.
- Movie rating distribution.

These visualizations make it easier to understand patterns in the dataset.

---

## 4. Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| CustomTkinter | Graphical user interface |
| Pandas | Data processing and analysis |
| Matplotlib | Charts and data visualization |
| CSV | Dataset storage and input |

---

## 5. Python Concepts Implemented

The project uses several fundamental Python programming concepts.

1. **Variables and Data Types:** Used to store movie information, ratings, statistics, and application data.
2. **Conditional Statements:** Used to validate records and make decisions based on different conditions.
3. **Loops:** Used to process movie records and perform repetitive operations.
4. **Functions:** Used to organize code into reusable blocks.
5. **Lists and Dictionaries:** Used to store and manage movie records and related information.
6. **File Handling:** Used to import and read CSV datasets.
7. **Classes and Objects:** Used to organize the application using object-oriented programming.
8. **Exception Handling:** Used to handle errors during file loading and data processing.

---

## 6. Difficulties Faced and Solutions

During the development of this project, I encountered several challenges. Solving these problems helped me understand Python programming and application development more practically.

### 6.1 Handling Invalid CSV Data

**Difficulty:**  
Imported CSV files could contain missing values, empty fields, duplicate records, non-numeric ratings, or ratings outside the accepted range.

**Solution:**  
I implemented data validation and cleaning logic using Pandas and conditional statements. Invalid records were skipped, and the application tracked the reasons for skipping them.

### 6.2 Calculating Genre-wise Statistics

**Difficulty:**  
Calculating average, highest, and lowest ratings separately for different movie genres required organizing and grouping the dataset correctly.

**Solution:**  
I used Pandas data grouping and aggregation operations to calculate the required statistics for each genre.

### 6.3 Integrating Charts into the GUI

**Difficulty:**  
Displaying Matplotlib charts inside a CustomTkinter application required integrating two different libraries.

**Solution:**  
I used Matplotlib's Tkinter integration through `FigureCanvasTkAgg` to display charts within the application's graphical interface.

### 6.4 Organizing the Application Code

**Difficulty:**  
As the application included multiple sections and functionalities, maintaining organized and understandable code became challenging.

**Solution:**  
I used classes, functions, meaningful variable names, and comments to organize the code and separate data-processing responsibilities from the graphical interface.

### 6.5 Debugging and Testing

**Difficulty:**  
During development, some application sections did not display the expected information, and errors occurred while integrating different functionalities.

**Solution:**  
I tested the application, examined error messages, corrected the relevant code, and verified the output after making changes.

---

## 7. Testing and Test Cases

The following test cases can be used to demonstrate the working of the Movie Rating Analyzer application.

**Note:** Attach actual screenshots captured while executing these test cases. Replace or modify the cases below if your teacher has assigned specific test cases.

### Test Case 1: Importing a Valid CSV File

**Objective:** To verify that the application successfully imports a valid movie dataset.

**Test Input:** A CSV file containing valid movie names, genres, and numeric ratings between 0 and 10.

**Expected Output:** The application successfully loads and displays the movie records and updates the dashboard statistics.

**Screenshot:**  
`![Test Case 1 - Valid CSV Import](screenshots/test_valid_csv.png)`

### Test Case 2: Handling Missing Values

**Objective:** To verify that records containing missing values are handled correctly.

**Test Input:** A CSV file containing records with missing movie names, genres, or ratings.

**Expected Output:** Invalid records are skipped during data cleaning, and the valid records are retained.

**Screenshot:**  
`![Test Case 2 - Missing Values](screenshots/test_missing_values.png)`

### Test Case 3: Validating Movie Ratings

**Objective:** To verify that non-numeric ratings and ratings outside the accepted range are rejected.

**Test Input:** A CSV file containing ratings such as text values, negative numbers, and values greater than 10.

**Expected Output:** Invalid rating records are skipped, while valid records are processed.

**Screenshot:**  
`![Test Case 3 - Invalid Ratings](screenshots/test_invalid_rating.png)`

### Test Case 4: Handling Duplicate Records

**Objective:** To verify that duplicate movie records are identified and skipped.

**Test Input:** A CSV file containing duplicate records.

**Expected Output:** Duplicate records are excluded from the cleaned dataset.

**Screenshot:**  
`![Test Case 4 - Duplicate Records](screenshots/test_duplicate_records.png)`

### Test Case 5: Genre-wise Analytics

**Objective:** To verify that the application calculates movie-rating statistics for different genres.

**Test Input:** A valid dataset containing movies from multiple genres.

**Expected Output:** The Analytics section displays the average, highest, and lowest ratings for each genre.

**Screenshot:**  
`![Test Case 5 - Genre Analytics](screenshots/analytics.png)`

### Test Case 6: Charts and Visualization

**Objective:** To verify that the application generates charts using the imported movie dataset.

**Test Input:** A valid movie dataset containing different ratings and genres.

**Expected Output:** The Charts section displays genre-wise average ratings and rating distribution visualizations.

**Screenshot:**  
`![Test Case 6 - Charts](screenshots/charts.png)`

---

## 8. Learning Outcomes

Through this project, I gained practical experience in:

- Writing and organizing Python programs.
- Applying object-oriented programming concepts.
- Reading and processing CSV files.
- Cleaning and validating datasets.
- Performing data analysis using Pandas.
- Creating charts using Matplotlib.
- Developing graphical desktop applications using CustomTkinter.
- Debugging errors and testing application functionality.
- Organizing project files and writing documentation.

---

## 9. Conclusion

The Movie Rating Analyzer project helped me apply fundamental Python programming concepts to develop a practical desktop application.

It combines CSV file handling, data cleaning, statistical analysis, and data visualization into a single graphical interface.

While developing this project, I improved my understanding of Python, object-oriented programming, data processing, GUI development, and debugging.

Overall, this project provided valuable hands-on experience in building a complete Python application and strengthened my programming fundamentals.

---

## 10. Project Repository

**GitHub Repository:**  
https://github.com/the-rishaw/Movie-Rating-Analyzer

## 11. Sample Dataset Used for Testing

The application was tested using a sample CSV dataset containing movie names, genres, and ratings. The dataset was designed to verify normal application functionality as well as data-cleaning and validation operations.

### 11.1 Sample CSV Data

The following sample data represents the structure of the CSV file used for testing:

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
Sholay, Action, 10
Ironman, Action, abc
The Batman, Action, 11
Batman Begins, Acton,
Action, 9
Batman Begins, , 9
Batman Begins, Action,, -2
```

### 11.2 Data Validation Test Samples

Additional test records were used to verify the application's data-cleaning functionality.

| Test condition | Sample input | Expected result |
|---|---|---|
| Missing movie name | `,Action,9` | Skip record |
| Missing genre | `Batman Begins,,9` | Skip record |
| Missing rating | `Batman Begins,Action,` | Skip record |
| Non-numeric rating | `Ironman,Action,abc` | Skip record |
| Negative rating | `Batman Begins,Action,-2` | Skip record |
| Rating above 10 | `Batman Begins,Action,11` | Skip record |
| Duplicate record | `Sholay,Action,10` (repeated) | Skip duplicate |

### 11.3 Purpose of the Sample Dataset

The sample dataset was used to test:

- Successful CSV file importing.
- Movie record display.
- Search and genre filtering.
- Missing-value validation.
- Invalid rating detection.
- Duplicate record handling.
- Dashboard statistics.
- Genre-wise average, highest, and lowest rating calculations.
- Chart generation and visualization

### 11.4 Test Data File

The sample dataset is included in the project's `data/` directory.

**File:** `data/sample_movies.csv`

The dataset can be imported into the application using the CSV import option to reproduce the testing process.