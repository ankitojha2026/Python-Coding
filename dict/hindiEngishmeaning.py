import requests
from googletrans import Translator

# Datamuse API URL
API_URL = "https://api.datamuse.com/words"

# Google Translate API setup
translator = Translator()

def get_hindi_meaning(word):
    """Function to get Hindi meaning using Google Translate"""
    translation = translator.translate(word, src='en', dest='hi')
    return translation.text

def get_word_info(word):
    # Fetching synonyms
    response = requests.get(API_URL, params={"rel_syn": word})
    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"Synonyms for '{word}':")
            for i, item in enumerate(data, 1):
                print(f"{i}. {item['word']}")
        else:
            print(f"No synonyms found for '{word}'.")

        # Fetching antonyms
        response_antonyms = requests.get(API_URL, params={"rel_ant": word})
        data_antonyms = response_antonyms.json()
        if data_antonyms:
            print(f"\nAntonyms for '{word}':")
            for i, item in enumerate(data_antonyms, 1):
                print(f"{i}. {item['word']}")
        else:
            print(f"No antonyms found for '{word}'.")

        # Fetching Hindi meaning
        hindi_meaning = get_hindi_meaning(word)
        print(f"\nHindi Meaning of '{word}': {hindi_meaning}")
        

          
    else:
        print("Error fetching data. Please check your connection or the word.")

def main():
    print("Welcome to the Enhanced Vocabulary Software!")
    while True:
        word = input("\nEnter an English word (or 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the vocabulary software...")
            break
        get_word_info(word)

if __name__ == "__main__":
    main()
