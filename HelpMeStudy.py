import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time

my_url = "https://www.quizlet.com/tommyboy295"
my_url2 = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards"
my_url3 = "https://www.amazon.com/s?k=graphics+cards&ref=nb_sb_noss_1"

driver = webdriver.Chrome()
driver.get(my_url)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
test = soup.findAll('div', {'class': 'DashboardFeedGroup'})
print(test)

# Get input for username of quizlet account
print("Enter Quizlet Username: ")
#username = input()
username = 'tommyboy295'
# TODO: Make it so a url can be entered for the user page directly.
# TODO: Make it so a url of the flashcards can be entered directly.
print("Username: " + username)
"""
response = requests.get(my_url, headers={'User-Agent': 'Chrome/73.0.3683.103'})
soup = BeautifulSoup(response.content, 'html5lib')

#print(soup.prettify())
#print(len(soup.findAll('div', class_='DashboardFeedGroup')))
containers = soup.findAll('div', {'class': 'DashboardFeedGroup'})
print(containers)
"""
"""
# opening up connection and getting the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = BeautifulSoup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class": "DashboardFeedGroup"})
print(len(containers))
"""

