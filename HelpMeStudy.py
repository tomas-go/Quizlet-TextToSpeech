from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.quizlet.com/tommyboy295'

# Selenium request
driver = webdriver.Firefox()
driver.get(url)
s_html = driver.execute_script("return document.documentElement.outerHTML")

sel_soup = BeautifulSoup(s_html, 'html.parser')


# Class for the flashcard groups. Gets there info so we can use this later based on the cards the user wants to study.
class Subject:
    def __init__(self, name, num_of_terms, link):
        self.name = name
        self.num_of_terms = num_of_terms
        self.link = link

    def info(self):
        return "Group:" + self.name + "has " + self.num_of_terms + "terms."

    def all_info(self):
        print("Name: " + str(self.name) + "\nNumber of Terms: " + str(self.num_of_terms) + "\nLink: " + str(self.link))
        print("---------------------------------")


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

# For testing purposes. Prints all information regarding all subjects pulled from Quizlet user's page
for i in range(len(all_subjects)):
    all_subjects[i].all_info()

# For testing purposes. Prints the number of subjects pulled.
print(len(all_subjects))
