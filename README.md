# A**nagrams**

**Goal:** Recreate the Anagrams game from GamePigeon in a Web Application

### **Game Rules:**

Try to get as many valid Anagrams of the given letters as you can within the time limit! 

- Only words of 3 or more words are valid anagrams
- Valid words are those in the English Scrabble dictionary
- Score is determined the way Scrabble words are scored

### Our Spin:

- Players can customize the number of letters, instead of the standard 6 letters
- Since this is a web version, players can type faster on a keyboard vs tapping letters

## Web Browser Version

Instructions to run and play it locally:

1. Have `flask` installed (make sure it’s under python 3.1 or higher)
2. Navigate to where you want to save the project locally 
3. `git clone https://github.com/ryangithubaccount/anagrams`
4. `cd anagrams`
5. `export FLASK_APP=flask_app.py`
6. `flask run`
7. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 

## Pure Python Version

Instructions to run and play it locally in the terminal:

1. Have `flask` installed (make sure it’s under python 3.1 or higher)
2. Navigate to where you want to save the project locally 
3. `git clone https://github.com/ryangithubaccount/anagrams`
4. `cd anagrams/app`
5. Go into the `anagrams.py` file and un-comment the last few lines 
6. `python anagrams.py`
