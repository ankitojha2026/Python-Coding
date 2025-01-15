import customtkinter as ctk
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Initialize the main application window
app = ctk.CTk()
app.title("English Learning Software")
app.geometry("500x500")

# Function to handle the search button click
def search_word():
    query = search_entry.get().strip()
    if query:
        try:
            # Translate to Hindi
            hindi_translation = translator.translate(query, src='en', dest='hi').text
            result_label.configure(text=f"Word: {query}\nHindi Meaning: {hindi_translation}")
        except Exception as e:
            result_label.configure(text="Error fetching translation. Please try again!")
    else:
        result_label.configure(text="Please enter a word to search!")

# Search Entry with placeholder text
search_entry = ctk.CTkEntry(app, width=300, placeholder_text="Search words")
search_entry.pack(pady=(20, 5))  # Padding to place it at the top center

# Search Button
search_button = ctk.CTkButton(app, text="Search", command=search_word)
search_button.pack(pady=(5, 10))

# Label to display search results
result_label = ctk.CTkLabel(app, text="", wraplength=400)
result_label.pack(pady=(10, 20))

# Adding Feature Buttons
button_frame = ctk.CTkFrame(app)  # Frame to hold buttons
button_frame.pack(pady=(20, 10))

# Functions for feature buttons
def feature_action(name):
    result_label.configure(text=f"You selected: {name}")

# First row of buttons
btn1 = ctk.CTkButton(button_frame, text="Vocabulary", command=lambda: feature_action("Vocabulary"))
btn2 = ctk.CTkButton(button_frame, text="Translation", command=lambda: feature_action("Translation"))
btn3 = ctk.CTkButton(button_frame, text="Quiz", command=lambda: feature_action("Quiz"))

btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3.grid(row=0, column=2, padx=5, pady=5)

# Second row of buttons
btn4 = ctk.CTkButton(button_frame, text="Typing Test", command=lambda: feature_action("Typing Test"))
btn5 = ctk.CTkButton(button_frame, text="Self Test", command=lambda: feature_action("Self Test"))
btn6 = ctk.CTkButton(button_frame, text="Daily Words Meaning", command=lambda: feature_action("Daily Words Meaning"))

btn4.grid(row=1, column=0, padx=5, pady=5)
btn5.grid(row=1, column=1, padx=5, pady=5)
btn6.grid(row=1, column=2, padx=5, pady=5)

# Third row with a single button
btn7 = ctk.CTkButton(button_frame, text="Notes", command=lambda: feature_action("Notes"))
btn7.grid(row=2, column=1, pady=5)

# Run the main loop
app.mainloop()
