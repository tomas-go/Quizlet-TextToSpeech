from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.quizlet.com/tommyboy295'

driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")

sel_soup = BeautifulSoup(html, 'html.parser')

#titles = sel_soup.findAll(class_='DashboardListItem')
#print(titles)
for i in sel_soup.findAll(class_='DashboardListItem'):
    text = i.findAll('span')
    print(text)
    for j in text:
        print(j.get_text())
    #set_name = text[1]
    #set_num_of_terms = text[0]
    #print("Name: " +set_name+ "\tNumber of Terms: " +set_num_of_terms)
