# Import for google text to speech
from gtts import gTTS

"""
speech = gTTS("Tomas is cool!", 'en', 'slow')

speech.save("testing.mp3")
"""
def tts(all_terms):
    for card in all_terms:
        text = card.term + card.definition

        print(text)
