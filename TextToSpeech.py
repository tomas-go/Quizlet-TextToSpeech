
from gtts import gTTS   # Import for google text to speech
import os               # Import os for creating a directory

# https://buildmedia.readthedocs.org/media/pdf/gtts/latest/gtts.pdf
# gtts documentation

def tts(all_terms, subject_name):
    print('Beginning work on ' + subject_name + '. Please wait till done message is shown.')
    folder = subject_name + '/'

    if not os.path.exists(os.path.dirname(folder)):
        os.makedirs(os.path.dirname(folder))

    for i in range(len(all_terms)):
        text = all_terms[i].term + ' ' + all_terms[i].definition

        # the true value is for if you want the audio to be slow. Can give options later
        speech = gTTS(text, 'en', True)

        # default the file should be saved as mp3 with the file name being the term used.
        try:
            speech.save('%s.mp3' % os.path.join(folder, all_terms[i].term))
        # If term is unusable as a file name, just use the flashcard number
        except (FileNotFoundError, OSError):
            speech.save('%s.mp3' % os.path.join(folder, str(i+1)))
        print(str(i+1) + ') ' + text)

    print(subject_name + ' is done!')
