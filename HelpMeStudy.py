# Imports to web scrap
from bs4 import BeautifulSoup
from selenium import webdriver

# Subject class in Subjects.py in the same directory
from Classes import Subject, NoItemsToConvert

# Text to Speech
from TermsToConvert import get_terms

# My personal quizlet for testing
#url = 'https://www.quizlet.com/tommyboy295'

# Quizlet url input from user.
# TODO: Add feature to allow user to copy url link for quizlet. Must have error checking to make sure it is a valid url.
entered_url = input("Enter quizlet url: ")

try:
    # Selenium request
    driver = webdriver.Firefox()
    driver.get(entered_url)
    s_html = driver.execute_script("return document.documentElement.outerHTML")
    # BeautifulSoup parser
    sel_soup = BeautifulSoup(s_html, 'html.parser')
except Exception:
    print("Exception Type: " + str(Exception))

# Array to hold all the Subjects
all_subjects = []

# DashboardListItem is the section that holds all information regarding each flashcard group.
# This loop pulls the name of the item, the number of terms associated with the item, and the link to the item.
# It is then added to all_subjects as a new object with those values
for item in sel_soup.findAll(class_='DashboardListItem'):
    name = item.find('span', {'class': 'SetPreview-cardHeaderTitle'}).get_text()
    number_of_terms = item.find('span', {'class': 'SetPreview-cardBylineTermsCount'}).get_text()
    link = item.find('a', href=True)['href']
    x = Subject(name, number_of_terms, link)
    all_subjects.append(x)

# Prints name and number of terms for each group.
for i in range(len(all_subjects)):
    print(str(i+1) + ")\t" + all_subjects[i].info())

# Gets user inputs and then tests to make sure it is correct.
# Will loop forever until a legal value is given.
# TODO: Add ability to select more than one group and/or all groups.
correct_input = False
while not correct_input:
    try:
        user_input = input("Type number of group to convert to speech: ")
        selected = int(user_input) - 1
        if not all_subjects[selected]:
            raise IndexError
        elif all_subjects[selected].num_of_terms == 0:
            raise NoItemsToConvert
        print(all_subjects[selected].all_info())
        correct_input = True
        get_terms(all_subjects[selected])     # Calls text to speech function in TermsToConvert.py
    except IndexError:
        print("Selected index does not exist. Please try again.")
    except ValueError:
        print("That was not an integer value. Please try again.")
    except NoItemsToConvert:
        print("This flashcard group is empty and has no items to convert to speech. Please select another group.")



