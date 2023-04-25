# Word Counter Microservice

# Summary:
## This is a Python microservice that takes a URL of a static website as an input and identifies all the unique words and how many times they occur on a web      page.      The output is a list of words in JSON format along with the frequency of occurrence (number of times the word is repeated).

# Prerequisite:
## Python, BeautifulSoup, requests, Counter, json

# Installation:
## To use this microservice, you must have Python 3 installed on your system. You can install it from the https://www.python.org/downloads/

## To install the required libraries, run the following command in your terminal:  pip install requests beautifulsoup4


# Code Explanation:
## A)
  from collections import Counter
  import json
  import re
  import requests
  from bs4 import BeautifulSoup

- The above lines import the required libraries for the microservice. 'collections.Counter' is used to count the frequency of each word, 'json' is used to convert       the word counts into a JSON object, 're' is used for regular expression operations to remove non-word characters, 'requests' is used to fetch the webpage content,     and 'bs4.BeautifulSoup' is used to extract text from the HTML tags.

## def get_word_counts(url):

### This function takes a URL of a static website as an input and identifies all the unique words and their frequency of occurrence on the webpage. It returns a JSON         object containing the words and their frequency of occurrence.

##  response = requests.get(url)
##  soup = BeautifulSoup(response.content, 'html.parser')

### These lines fetch the webpage content using the requests library and create a BeautifulSoup object to parse the HTML content.

##   text = soup.get_text()

### This line extracts the text from the HTML tags using the get_text() method of the BeautifulSoup object.

##  words = re.findall(r'\b\w+\b', text)

### These lines use a regular expression to remove non-word characters from the text. The '\b\w+\b' pattern matches all words in the text by requiring at least one         word character ('\w+') surrounded by word boundaries ('\b').

## word_counts = Counter(words)

### This line uses the 'collections.Counter' library to count the frequency of each word.

##  json_object = json.dumps(word_counts, indent=4)

### This line converts the 'Counter' object into a JSON object with indentation for readability using the 'json.dumps()' method.

## return json_object

### This line returns the JSON object containing the unique words and their frequency of occurrence on the webpage.














