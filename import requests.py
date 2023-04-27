import requests
from bs4 import BeautifulSoup
import json


def count_words(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.get_text()

    words = text.split()

    word_counts = {}
    for word in words:
        word = word.lower()
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    word_list = [(word, count) for word, count in word_counts.items()]

    word_list.sort(key=lambda x: x[1], reverse=True)

    json_result = json.dumps(word_list)

    return json_result


url = 'https://www.youtube.com/'
Output = count_words(url)
print(Output)
