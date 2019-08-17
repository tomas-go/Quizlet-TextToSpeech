# Imports to web scrap
from bs4 import BeautifulSoup       # Import to web scrap
from selenium import webdriver      # Import to let javascript load on web page
from selenium.common.exceptions import InvalidArgumentException     # Import for error raised when url is invalid.

from Classes import Subject, NoItemsToConvert       # Subject class in Subjects.py in the same directory
from TermsToConvert import get_terms                # Text to Speech
from PatternMatching import quizlet_valid_url       # Format checking url input

from GUI import root    # Import the root/window from GUI.py

root.mainloop()     # Make the window run

# Quizlet url input from user.
legal_url = False
while not legal_url:
    try:
        quizlet_url = input("Enter Quizlet url: ")

        if quizlet_url == "exit":       # Exit option
            print("Program ended.")
            quit()
        elif not quizlet_valid_url(quizlet_url):
            raise ValueError
        # Selenium request
        driver = webdriver.Firefox()
        driver.get(quizlet_url)
        s_html = driver.execute_script("return document.documentElement.outerHTML")
        # BeautifulSoup parser
        sel_soup = BeautifulSoup(s_html, 'html.parser')
        legal_url = True
    except InvalidArgumentException:
        print(quizlet_url + " is not a valid url. The url needs to be in the format \"https://quizlet.com/username\"."
                            " Please try again.")
        driver.close()  # Ends error session
    except ValueError:
        print(quizlet_url + " is not an acceptable quizlet url. The url needs to be in the format "
                            "\"https://quizlet.com/username\". Please try again.")

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


def getFlashcardGroups():
    if len(all_subjects) == 0:
        print("This Quizlet page has no flashcard groups to convert.")
        driver.quit()
        quit()
    else:
        # Prints name and number of terms for each group.
        for i in range(len(all_subjects)):
            print(str(i+1) + ")\t" + all_subjects[i].info())


# Gets user inputs and then tests to make sure it is correct.
# Will loop forever until a legal value is given.
# TODO: Add ability to select more than one group and/or all groups.
def main():
    correct_input = False
    while not correct_input:
        try:
            getFlashcardGroups()
            user_input = input("Type number of group to convert to speech: ")
            if user_input == "exit":    # quit option in case user wants to terminate the program early.
                print("Program ended.")
                driver.quit()
                quit()
            selected = int(user_input) - 1
            if not all_subjects[selected]:
                raise IndexError
            elif all_subjects[selected].num_of_terms == 0:
                raise NoItemsToConvert
            print(all_subjects[selected].all_info())
            correct_input = True
            get_terms(all_subjects[selected])     # Calls text to speech function in TermsToConvert.py
            again()
        except IndexError:
            print("Selected index does not exist. Please try again.")
        except ValueError:
            print("That was not an integer value. Please try again.")
        except NoItemsToConvert:
            print("This flashcard group is empty and has no items to convert to speech. Please select another group.")


def again():
    more_groups_to_convert = input("Would you like to convert another group? Enter y or n: ")
    if more_groups_to_convert == 'y':
        main()
    elif more_groups_to_convert == 'n' or more_groups_to_convert == 'exit':
        print("Program ended.")
        driver.quit()
    else:
        print("Please try again and enter a valid input.")
        again()


main()