import tkinter as tk

root = tk.Tk()
root.title("Typing Test Layout")
root.geometry("500x400")

# Labels aur Entry box place karte hain
label = tk.Label(root, text="Start Typing:", font=("Arial", 14))
label.place(x=50, y=50)

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.place(x=50, y=100)

button = tk.Button(root, text="Start Test", font=("Arial", 12))
button.place(x=50, y=150)

# Main loop
root.mainloop()
