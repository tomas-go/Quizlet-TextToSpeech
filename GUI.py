import tkinter as tk

# Imports to web scrap
from bs4 import BeautifulSoup       # Import to web scrap
from selenium import webdriver      # Import to let javascript load on web page
from selenium.common.exceptions import InvalidArgumentException     # Import for error raised when url is invalid.

from Classes import Subject, NoItemsToConvert       # Subject class in Subjects.py in the same directory
from TermsToConvert import get_terms                # Text to Speech
from PatternMatching import quizlet_valid_url       # Format checking url input

# Array to hold all the Subjects
all_subjects = []

# Quizlet url input from user.
def get_page(entry):
    # Selenium request
    driver = webdriver.Firefox()
    driver.get(entry)
    s_html = driver.execute_script("return document.documentElement.outerHTML")
    # BeautifulSoup parser
    sel_soup = BeautifulSoup(s_html, 'html.parser')


# GUI 
HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("Quizlet Text To Speech App")    # Title for window

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

top_frame = tk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

user_input = tk.Entry(top_frame, font=40)
user_input.place(relwidth=0.65, relheight=1)

submit_button = tk.Button(top_frame, text="Go", font="40", command=lambda: get_page(user_input.get()))
submit_button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# root.mainloop()