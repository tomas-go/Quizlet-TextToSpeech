# Imports to web scrap
from bs4 import BeautifulSoup
from selenium import webdriver

# Subject class in Subjects.py in the same directory
from Subjects import Subject

# Import for google text to speech
from gtts import gTTS

"""
speech = gTTS("Tomas is cool!", 'en', 'slow')

speech.save("testing.mp3")
"""

# Accepts a subject as a parameter and assigns the link value to variable.
def tts(sub):
    item_url = sub.link

    # Selenium request
    driver = webdriver.Firefox()
    driver.get(item_url)
    s_html = driver.execute_script("return document.documentElement.outerHTML")

    sel_soup = BeautifulSoup(s_html, 'html.parser')

    all_items = []
