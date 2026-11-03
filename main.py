import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt

from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MovieRatingAnalyzer(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Movie Rating Analyzer")
        self.geometry("1200x750")
        self.minsize(1000, 650)

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    app = MovieRatingAnalyzer()
    app.mainloop()