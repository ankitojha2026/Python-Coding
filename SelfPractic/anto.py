import requests

# Function to get synonyms from Datamuse API
def get_synonyms(word):
    url = f"https://api.datamuse.com/words?rel_syn={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        return [item['word'] for item in data[:5]]  # Limit to 5 synonyms
    else:
        return ["No synonyms found."]

# Function to get antonyms from Datamuse API
def get_antonyms(word): 
    url = f"https://api.datamuse.com/words?rel_ant={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [item['word'] for item in data[:5]]  # Limit to 5 antonyms
    else:
        return ["No antonyms found."]

# Function to handle user input and show results
def search_word():
    word = input("Enter a word to search for synonyms and antonyms: ")
    if word:
        # Get synonyms and antonyms
        synonyms = get_synonyms(word)
        antonyms = get_antonyms(word)

        # Display results
        print("\nSynonyms: ")
        if synonyms:
            print(", ".join(synonyms))
        else:
            print("No synonyms found.")
        
        print("\nAntonyms: ")
        if antonyms:
            print(", ".join(antonyms))
        else:
            print("No antonyms found.")
    else:
        print("Please enter a valid word.")

# Main program loop
if __name__ == "__main__":
    while True:
        search_word()
        cont = input("\nDo you want to search another word? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting the program. Goodbye!")
            break
