import tkinter as tk

# Main window create karte hain
root = tk.Tk()
root.title("Entry Size Example")
root.geometry("400x300")

# Function to display entry size
def show_entry_size():
    text = entry.get()  # Entry ka text lete hain
    length = len(text)  # Text ki length calculate karte hain
    label_result.config(text=f"Entry Size: {length} characters")  # Result show karte hain

# Entry Widget
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.place(x=50, y=50)

# Button to check entry size
button = tk.Button(root, text="Check Size", font=("Arial", 12), command=show_entry_size)
button.place(x=50, y=100)

# Label to display the size
label_result = tk.Label(root, text="Entry Size: 0 characters", font=("Arial", 12))
label_result.place(x=50, y=150)

# Main loop
root.mainloop()
