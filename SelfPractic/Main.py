import customtkinter as ctk
import mysql.connector
from googletrans import Translator
import requests

# Initialize the main application window
app = ctk.CTk()
app.title("English Learning Software")
app.geometry("500x400")
translator=Translator()

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

# Functions for feature buttons

    
    
def vocabulary():
    app = ctk.CTk()
    app.title("English Learning Software")
    app.geometry("800x600")

    translator = Translator()

    # Function to get Hindi meaning
    def search_hindi_meaning(word):
        try:
            translation = translator.translate(word, src='en', dest='hi').text
            return translation
        except Exception as e:
            print(f"Error fetching Hindi meaning: {e}")
            return "Error in fetching Hindi meaning."

    # Function to get synonyms using Datamuse API
    def get_synonyms(word):
        try:
            url = f"https://api.datamuse.com/words?rel_syn={word}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return [item['word'] for item in data[:5]] if data else ["No synonyms found."]
            return ["Error fetching synonyms."]
        except Exception as e:
            print(f"Error fetching synonyms: {e}")
            return ["Error fetching synonyms."]

    # Function to get antonyms using Datamuse API
    def get_antonyms(word):
        try:
            url = f"https://api.datamuse.com/words?rel_ant={word}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return [item['word'] for item in data[:5]] if data else ["No antonyms found."]
            return ["Error fetching antonyms."]
        except Exception as e:
            print(f"Error fetching antonyms: {e}")
            return ["Error fetching antonyms."]

    # Function to handle search
    def search_word():
        query = search_entry.get().strip()
        if not query:
            result_label.configure(text="Please enter a word to search!")
            return

        # Display Hindi meaning
        hindi_translation = search_hindi_meaning(query)
        result_label.configure(text=f"Word: {query}\nHindi Meaning: {hindi_translation}")

        # Display synonyms and antonyms
        synonyms = get_synonyms(query)
        antonyms = get_antonyms(query)
        display_list(synonym_frame, synonyms, "Synonyms")
        display_list(antonym_frame, antonyms, "Antonyms")

    # Function to dynamically update synonym/antonym frames
    def display_list(frame, items, title):
        for widget in frame.winfo_children():
            widget.pack_forget()  # Reusing widgets by removing them, instead of destroying
        title_label = ctk.CTkLabel(frame, text=title, font=("Arial", 14, "bold"))
        title_label.pack(pady=5)
        for idx, item in enumerate(items):
            translation = search_hindi_meaning(item)
            item_label = ctk.CTkLabel(frame, text=f"{idx + 1}. {item} - {translation}")
            item_label.pack(anchor="w")

    # Function to connect to MySQL and fetch data
    def fetch_mysql_data():
        try:
            connection = mysql.connector.connect(
                host="localhost",      # MySQL server hostname
                user="root",           # Replace with your username
                password="123456789",  # Replace with your password
                database="learn_english",  # Replace with your database name
                port=3306              # Default MySQL port
            )

            cursor = connection.cursor()
            fetch_query = "SELECT * FROM word_meaning;"
            cursor.execute(fetch_query)

            # Fetch all rows from the executed query
            results = cursor.fetchall()

            # Clear any previous data before displaying new results
            for widget in mysql_frame.winfo_children():
                widget.pack_forget()

            # Display data in the scrollable frame
            for row in results:
                word, meaning = row
                item_label = ctk.CTkLabel(mysql_frame, text=f"{word} - {meaning}")
                item_label.pack(anchor="w", pady=2)

            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # Search Entry with placeholder
    search_entry = ctk.CTkEntry(app, width=350, placeholder_text="Enter word to search")
    search_entry.pack(pady=(20, 10))

    # Search Button
    search_button = ctk.CTkButton(app, text="Search", command=search_word)
    search_button.pack(pady=(5, 10))

    # Result Label
    result_label = ctk.CTkLabel(app, text="", wraplength=500, font=("Arial", 12))
    result_label.pack(pady=10)

    # Frames for Synonyms and Antonyms
    synonym_frame = ctk.CTkFrame(app, width=250, height=200, corner_radius=10,)
    synonym_frame.pack(side="left", padx=(20, 10), pady=10, fill="both", expand=True)

    antonym_frame = ctk.CTkFrame(app, width=250, height=200, corner_radius=10)
    antonym_frame.pack(side="right", padx=(10, 20), pady=10, fill="both", expand=True)

    # Scrollable Frame for MySQL Data
    scrollable_frame = ctk.CTkFrame(app )
    scrollable_frame.pack(pady=(20, 10), fill="both", expand=True)

    # Create a canvas for scrolling
    canvas = ctk.CTkCanvas(scrollable_frame)
    canvas.pack(side="left", fill="both", expand=True)

    # Add scrollbar
    scrollbar = ctk.CTkScrollbar(scrollable_frame, orientation="vertical", command=canvas.yview )
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold the MySQL data inside the canvas
    mysql_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=mysql_frame, anchor="nw")

    # Bind the canvas to scrollbar
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    mysql_frame.bind("<Configure>", on_frame_configure)

    # Call the function to fetch MySQL data
    fetch_mysql_data()

    app.mainloop()








    
    
    
# Adding Feature Buttons
button_frame = ctk.CTkFrame(app)  # Frame to hold buttons
button_frame.pack(pady=(10, 0))

# First row of buttons
btn1 = ctk.CTkButton(button_frame, text="Vocabulary", command=vocabulary)
btn2 = ctk.CTkButton(button_frame, text="Translation")
btn3 = ctk.CTkButton(button_frame, text="Quiz", )

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