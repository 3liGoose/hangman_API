import random
import requests
import json
import string

# word -> hanged -> isWordGuessed -> getAvailable -> getWordGuessed -> hangman

# Function to pull a random word from a list of words using API

def word():
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random": "true"}
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "c6a7192fc9msh4931c462d8c53c4p1ced90jsn45cd3d660151"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    word = json.loads(response.text)["word"]
    return word

def hanged(man):
    graphic = [
    '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \
       |
    ==============
    '''
    ]
    return graphic[man]


# -----------------------------------


def isWordGuessed(secretWord, lettersGuessed):
    count = 1

    for i in lettersGuessed:
      if i in secretWord:
        count += 1
    if count == len(secretWord):
      return True
    else:
      return False


def getGuessedWord(secretWord, lettersGuessed):
    correctGuesses = []
    for z in secretWord:
      if z in lettersGuessed:
          correctGuesses.append(z)
    outputString = ''
    for j in secretWord:
          if j in correctGuesses:
            outputString += j
          else:
              outputString +=  "_"
    return outputString



def getAvailableLetters(lettersGuessed):
    
    alphabet=list(string.ascii_lowercase)
    for p in lettersGuessed:
        alphabet.remove(p)
    return ''.join(alphabet)

def hangman(secretWord):
  print("welcome to hangman!")
  print("This word has " + str(len(secretWord)) + " letters in it.")


  global lettersGuessed
  mistakeMade=0
  lettersGuessed=[]

  while 6 - mistakeMade >= 0:
    if isWordGuessed(secretWord, lettersGuessed):
      print("-------------")
      print("Congratulations, you won!")
      break
      
    else:
      print("-------------")
      print("You have", 6-mistakeMade, "guesses left.")
      print("The avalabile letters are " + getAvailableLetters(lettersGuessed))
      print(hanged(mistakeMade))
      guess = str(input("please enter another letter.")).lower()
      if len(guess) != 1:
        print("you can only enter one letter.")
        guess = str(input("please enter another letter.")).lower()
      if guess in lettersGuessed:
        print("you already guessed that letter. Choose another.")
        print(getGuessedWord(secretWord, lettersGuessed))
      elif guess in secretWord and guess not in lettersGuessed:
        lettersGuessed.append(guess)
        print("good job guessing " + guess + " as a letter.")
        print(getGuessedWord(secretWord, lettersGuessed))
      else:
        lettersGuessed.append(guess)
        mistakeMade += 1
        print("that is not the correct word. Youʻre still alive. for now...")
        print(getGuessedWord(secretWord, lettersGuessed))

  print("-------------")
  print(hanged(6))
  print("Sorry, you ran out of guesses. The word was:",secretWord)

secretWord = word()
hangman("apple")