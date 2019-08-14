# THIS BRANCH WILL BE USED FOR TESTING UPDATES.

# Training Tasks
[ ] How to use pipenv and make it easy to run and install on other machines with other developers.
    * Also to get away from installing packages globally.
    * Videos used to refer to:
      * https://www.youtube.com/watch?v=zDYL22QNiWk
    * Progress:
      * Program can run with:
        * `pipenv run HelpMeStudy.py`
          
          OR
        * `pipenv shell`
          
          `py HelpMeStudy.py`
    * Problems:
      * `pipenv install` works and begins to install dependencies but gets stuck on the last one. This seems to be with `urllib3`. I ran `pipenv install urllib3` and the program got stuck in the same way. 
        * Restarted my computer and this works fine now. The last dependency does take the most time but it works fine after that. Not sure how to replicate error.
[ ] Create a GUI to make the user experience better than just using the terminal.
[ ] Practice using git and merging branches.
