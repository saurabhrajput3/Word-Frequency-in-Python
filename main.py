

from collections import Counter
import json
import re
import requests
from bs4 import BeautifulSoup


def get_word_counts(url):
    
    # Get the webpage HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from HTML tags
    text = soup.get_text()

    # Remove non-word characters
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrence of each word
    word_counts = Counter(words)

    # Convert the Counter object to a JSON object
    json_object = json.dumps(word_counts, indent=4)

    return json_object

url = "https://www.google.com"
word_counts = get_word_counts(url)
print(word_counts)

