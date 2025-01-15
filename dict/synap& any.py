import requests

# Datamuse API URL
API_URL = "https://api.datamuse.com/words"

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

        # Fetching related words
        response_related = requests.get(API_URL, params={"rel_trg": word})
        data_related = response_related.json()
        if data_related:
            print(f"\nRelated words to '{word}':")
            for i, item in enumerate(data_related, 1):
                print(f"{i}. {item['word']}")
        else:
            print(f"No related words found for '{word}'.")

    else:
        print("Error fetching data. Please check your connection or API.")

def main():
    print("Welcome to the Datamuse Vocabulary Software!")
    while True:
        word = input("\nEnter an English word (or 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the vocabulary software...")
            break
        get_word_info(word)

if __name__ == "__main__":
    main()
