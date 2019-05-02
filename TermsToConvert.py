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


# Accepts a subject as a parameter and assigns the link value to variable.
# Then it creates a new soup and web scrapes for information regarding the flashcards themselves.
def get_terms(sub):
    item_url = sub.link

    # Selenium request
    driver = webdriver.Firefox()
    driver.get(item_url)
    s_html = driver.execute_script("return document.documentElement.outerHTML")

    sel_soup = BeautifulSoup(s_html, 'html.parser')

    all_items = []

    for card in sel_soup.findAll(class_='SetPageTerm-contentWrapper'):
        content = card.findAll(class_='TermText notranslate lang-en')
        left = content[0].get_text()
        right = content[1].get_text()
        c = Item(left, right)
        all_items.append(c)

    print("Number of flashcards: " + str(len(all_items)))

    for item in all_items:
        print(item.all_info())

