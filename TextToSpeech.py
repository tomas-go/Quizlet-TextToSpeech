# Imports to web scrap
from bs4 import BeautifulSoup
from selenium import webdriver

# Subject class in Subjects.py in the same directory
from Subjects import Subject

from Items import Item

# Import for google text to speech
from gtts import gTTS

"""
speech = gTTS("Tomas is cool!", 'en', 'slow')

speech.save("testing.mp3")
"""

url = "https://quizlet.com/381622817/cop4555-module-1-flash-cards/"
# Selenium request
driver = webdriver.Firefox()
driver.get(url)
s_html = driver.execute_script("return document.documentElement.outerHTML")

sel_soup = BeautifulSoup(s_html, 'html.parser')

all_items = []

print("Length of All Items: " + str(len(all_items)))
for card in sel_soup.findAll(class_='SetPageTerm-contentWrapper'):
    print(card.find('div', {'class': 'SetPageTerm-wordText'}))
    print("SHOULD BE END OF TERM ---------------------")

# Accepts a subject as a parameter and assigns the link value to variable.
def tts(sub):
    item_url = sub.link

    # Selenium request
    driver = webdriver.Firefox()
    driver.get(item_url)
    s_html = driver.execute_script("return document.documentElement.outerHTML")

    sel_soup = BeautifulSoup(s_html, 'html.parser')

    all_items = []

    for card in sel_soup.findAll(class_='SetPageTerms-term'):
        t = card.find('TermText notranslate lang-en').get_text()
        #d = card.find('span', {'class': 'SetPageTerm-definitionText'}).get_text()
        d = card.find('TermText notranslate lang-en').get_text()
        y = Item(t, d)
        all_items.append(y)

    # Prints name and number of terms for each group.
    for i in range(len(all_items)):
        print(str(i + 1) + ")\t" + all_items[i].info())

