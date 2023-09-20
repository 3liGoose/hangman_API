import random
import requests
import json
import string

def word():

    '''
    # FIXME - Returns a random word from "https://wordsapiv1.p.rapidapi.com/words/".
              There should be three parameters for request.get function - url, headers, and params
              headers should have   {
                    'x-rapidapi-host': SERVER_URL_HERE
                    'x-rapidapi-key': YOUR_API_KEY_HERE
              } format
              params should have {"random: "true/false"}
    '''

    response = requests.get()
    word = json.loads(response.text)["word"]
    pass