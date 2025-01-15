from googletrans import Translator

def translate_to_hindi(text):
    translator = Translator()
    translated = translator.translate(text, src='hi', dest='en')
    return translated.text

def main():
    print("Welcome to the English to Hindi Dictionary!")
    while True:
        word = input("Enter an English word (or 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the dictionary...")
            break
        translated_word = translate_to_hindi(word)
        print(f"The Hindi translation of '{word}' is: {translated_word}")

if __name__ == "__main__":
    main()
