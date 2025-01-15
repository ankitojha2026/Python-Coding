import customtkinter as ctk
import requests

# Function to get Hindi meaning from MyMemory API
def get_hindi_meaning(word):
    try:
        url = f"https://api.mymemory.translated.net/get?q={word}&langpair=en|hi"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['responseData']['translatedText']
        else:
            return "Hindi meaning not found!"
    except Exception as e:
        return f"Error: {e}"

# Function to get Synonyms and Antonyms from WordsAPI
def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []
    try:
        api_key = "YOUR_WORDSAPI_KEY"  # Replace with your WordsAPI key
        url = f"https://wordsapi.com/mashape/words/{word}/relatedWords?useCanonical=true&api_key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                if item['relationshipType'] == 'synonym':
                    synonyms = item['words'][:5]  # Limit to 5 synonyms
                elif item['relationshipType'] == 'antonym':
                    antonyms = item['words'][:5]  # Limit to 5 antonyms
        else:
            return [], []
    except Exception as e:
        return [], []

    return synonyms, antonyms

# Vocabulary Window Function
def open_vocabulary_window():
    vocab_window = ctk.CTk()
    vocab_window.title("Vocabulary")
    vocab_window.geometry("500x600")

    # Search Entry for Vocabulary Window
    search_entry_vocabulary = ctk.CTkEntry(vocab_window, width=300, placeholder_text="Search Vocabulary")
    search_entry_vocabulary.pack(pady=(20, 5))

    # Search Button for Vocabulary Window
    search_button_vocabulary = ctk.CTkButton(vocab_window, text="Search", command=lambda: search_vocab_word(search_entry_vocabulary.get(), vocab_window))
    search_button_vocabulary.pack(pady=(5, 10))

    # Result Label for Vocabulary Window
    result_label_vocabulary = ctk.CTkLabel(vocab_window, text="", wraplength=400)
    result_label_vocabulary.pack(pady=(10, 20))

    # Synonym and Antonym Frames
    frame = ctk.CTkFrame(vocab_window)
    frame.pack(pady=10)

    # Synonyms Frame
    synonym_frame = ctk.CTkFrame(frame)
    synonym_frame.pack(side="left", padx=10)

    synonym_label = ctk.CTkLabel(synonym_frame, text="Synonyms")
    synonym_label.pack()

    synonym_listbox = ctk.CTkLabel(synonym_frame, text="")
    synonym_listbox.pack()

    # Antonyms Frame
    antonym_frame = ctk.CTkFrame(frame)
    antonym_frame.pack(side="left", padx=10)

    antonym_label = ctk.CTkLabel(antonym_frame, text="Antonyms")
    antonym_label.pack()

    antonym_listbox = ctk.CTkLabel(antonym_frame, text="")
    antonym_listbox.pack()

    # Scrollable A-Z Words Frame
    scroll_frame = ctk.CTkFrame(vocab_window)
    scroll_frame.pack(pady=(10, 20), fill="both", expand=True)

    canvas = ctk.CTkCanvas(scroll_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ctk.CTkScrollbar(scroll_frame, orientation="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Adding A to Z words to the scrollable frame (dummy example)
    words_list = ["apple", "banana", "cat", "dog", "elephant"]
    for word in words_list:
        word_label = ctk.CTkLabel(scrollable_frame, text=f"{word.upper()} - {get_hindi_meaning(word)}")
        word_label.pack(pady=2)

    # Update the scroll region to fit all content
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Function to handle search results
    def search_vocab_word(query, window):
        if query:
            # Get Hindi meaning
            hindi_translation = get_hindi_meaning(query)

            # Get Synonyms and Antonyms
            synonyms, antonyms = get_synonyms_antonyms(query)

            # Display results
            result_label_vocabulary.configure(text=f"Word: {query}\nHindi Meaning: {hindi_translation}")
            synonym_listbox.configure(text="\n".join(synonyms))
            antonym_listbox.configure(text="\n".join(antonyms))
        else:
            result_label_vocabulary.configure(text="Please enter a word!")
            synonym_listbox.configure(text="")
            antonym_listbox.configure(text="")
    vocab_window.mainloop()

# Initialize the main application window
open_vocabulary_window()

import customtkinter as ctk

# Vocabulary Window Function (Only GUI)
def open_vocabulary_window():
    vocab_window = ctk.CTk()
    vocab_window.title("Vocabulary")
    vocab_window.geometry("500x600")

    # Search Entry for Vocabulary Window
    search_entry_vocabulary = ctk.CTkEntry(vocab_window, width=300, placeholder_text="Search Vocabulary")
    search_entry_vocabulary.pack(pady=(20, 5))

    # Search Button for Vocabulary Window
    search_button_vocabulary = ctk.CTkButton(vocab_window, text="Search")
    search_button_vocabulary.pack(pady=(5, 10))

    # Result Label for Vocabulary Window
    result_label_vocabulary = ctk.CTkLabel(vocab_window, text="", wraplength=400)
    result_label_vocabulary.pack(pady=(10, 20))

    # Synonym and Antonym Frames
    frame = ctk.CTkFrame(vocab_window)
    frame.pack(pady=10)

    # Synonyms Frame
    synonym_frame = ctk.CTkFrame(frame)
    synonym_frame.pack(side="left", padx=10)

    synonym_label = ctk.CTkLabel(synonym_frame, text="Synonyms")
    synonym_label.pack()

    synonym_listbox = ctk.CTkLabel(synonym_frame, text="")
    synonym_listbox.pack()

    # Antonyms Frame
    antonym_frame = ctk.CTkFrame(frame)
    antonym_frame.pack(side="left", padx=10)

    antonym_label = ctk.CTkLabel(antonym_frame, text="Antonyms")
    antonym_label.pack()

    antonym_listbox = ctk.CTkLabel(antonym_frame, text="")
    antonym_listbox.pack()

    # Scrollable A-Z Words Frame
    scroll_frame = ctk.CTkFrame(vocab_window)
    scroll_frame.pack(pady=(10, 20), fill="both", expand=True)

    canvas = ctk.CTkCanvas(scroll_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ctk.CTkScrollbar(scroll_frame, orientation="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Adding A to Z words to the scrollable frame (dummy example)
    words_list = ["apple", "banana", "cat", "dog", "elephant"]
    for word in words_list:
        word_label = ctk.CTkLabel(scrollable_frame, text=f"{word.upper()} - Example Hindi meaning")
        word_label.pack(pady=2)

    # Update the scroll region to fit all content
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    vocab_window.mainloop()

# Initialize the main application window
open_vocabulary_window()
