import tkinter as tk  # Tkinter ko import karte hain

# Ek window create karte hain
root = tk.Tk()

# Window ka title set karte hain
root.title("Mera Pehla Tkinter Program")


# Window ka size set karte hain
root.geometry("600x600+400+200")  # Width x Height


# Ek Label add karte hain
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20))
label.pack()  # Label ko screen par show karte hain

# Window ko display karne ke liye loop chalayen
root.mainloop()
