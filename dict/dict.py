import tkinter as tk
from tkinter import messagebox
import requests

# Function to get word meaning
def get_meaning():
    word = word_entry.get()  # Get the word entered by the user
    if word == "":
        messagebox.showwarning("Input Error", "Please enter a word.")
        return

    # API URL (using a free API)
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        # Make an API request to get the meaning of the word
        response = requests.get(url)
        data = response.json()

        # Check if the response contains word definitions
        if "title" in data and data["title"] == "No Definitions Found":
            meaning_text.set(f"Sorry, no definitions found for '{word}'.")
        else:
            # Extracting the meaning and displaying it
            meaning = data[0]['meanings'][0]['definitions'][0]['definition']
            meaning_text.set(f"Meaning of '{word}':\n\n{meaning}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        meaning_text.set("Error fetching word meaning.")

# Creating the main window
root = tk.Tk()
root.title("Dictionary App")
root.geometry("500x400")

# Title label
title_label = tk.Label(root, text="Dictionary App", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Word entry label and input field
word_label = tk.Label(root, text="Enter a word:", font=("Arial", 14))
word_label.pack(pady=5)

word_entry = tk.Entry(root, font=("Arial", 14), width=30)
word_entry.pack(pady=10)

# Button to get meaning
search_button = tk.Button(root, text="Get Meaning", command=get_meaning, bg="lightblue", fg="black", font=("Arial", 12))
search_button.pack(pady=10)

# Label to display meaning
meaning_text = tk.StringVar()
meaning_label = tk.Label(root, textvariable=meaning_text, font=("Arial", 12), justify=tk.LEFT, wraplength=450)
meaning_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
