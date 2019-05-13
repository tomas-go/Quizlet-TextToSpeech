# Quizlet-TextToSpeech
##Overview
This program uses Python to go to a user requested Quizlet account page and web scraps all flashcard groups. 
The flashcard groups are then shown to the user where they can be selected to have their terms web scraped and turned 
into an audio file using Google's TextToSpeech API. All the audio files will be placed in a folder named after the 
flashcard group. Because the flashcard groups and terms are loaded using javascript, BeautifulSoup and Selerium needed 
to be used in order to properly web scrap.

##Motivation
I have always found flashcards to be helpful for easy studying and quick reviewing before exams. Once I discovered Quizlet,
I ditched physical flashcards for virtual ones. While this has been more convenient, there were some situations where I 
would be unable to physically look at a computer/phone. I decided to see if it was possible to use Quizlet and a 
text-to-speech API to get mp3 files of my flashcards. Now during activities such as driving, exercising, etc., I can 
make good use of my time to study.

##Prerequisites
Install Firefox Web Browser.
Install geckodriver.
##Installing
`pip install selenium`

`pip install bs4`

`pip install gTTS` 
##Usage
Run HelpMeStudy.py. Blah,blah. Windows pop up.

