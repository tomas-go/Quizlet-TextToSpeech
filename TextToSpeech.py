# Import for google text to speech
from gtts import gTTS
import os


def tts(all_terms, subject_name):
    print('Beginning work on ' + subject_name + '. Please wait till done message is shown.')

    if not os.path.exists(os.path.dirname(subject_name + '/')):
        os.makedirs(os.path.dirname(subject_name + '/'))

    for i in range(len(all_terms)):
        text = all_terms[i].term + ' ' + all_terms[i].definition
        speech = gTTS(text, 'en', 'slow')
        speech.save('%d.mp3' % (i+1))
        print(str(i+1) + ') ' + text)
    print(subject_name + 'is done!')
