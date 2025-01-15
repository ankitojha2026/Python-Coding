
import requests
from googletrans import Translator

def get_words_starting_with(letter, limit=200):
    # Use Datamuse API to fetch words
    url = f"https://api.datamuse.com/words?sp={letter}*&max={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [item['word'] for item in data]
    return []

def translate_to_hindi(words):
    translator = Translator()
    translated_list = []
    for word in words:
        try:
            translation = translator.translate(word, src="en", dest="hi").text
            translated_list.append([word, translation])
        except Exception as e:
            translated_list.append([word, "Translation Error"])
    return translated_list

# Fetch and translate words
english_words = get_words_starting_with("a", limit=200)
sorted_words = sorted(english_words)  # Sort alphabetically
word_meaning_list = translate_to_hindi(sorted_words)

# Display the list
for pair in word_meaning_list:
    print(pair)
