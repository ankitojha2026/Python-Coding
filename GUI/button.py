import tkinter as tk

# Main window create karte hain
root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

# Ek function define karte hain jab button click ho
def button_clicked():
    label.config(text="Button Clicked!")

# Ek Label aur Button create karte hain
label = tk.Label(root, text="Click the Button", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=button_clicked)
button.pack(pady=10)

# Main loop run karte hain
root.mainloop()
