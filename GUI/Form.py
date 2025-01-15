import tkinter as tk

# Form dimensions
win_width = 1200
win_height = 550

def form():
    def submit_form():
        # Get the values from the entry fields
        name_val = name_entry.get()
        gmail_val = gmail_entry.get()
        phone_val = phone_entry.get()
        password_val = password_entry.get()

        # Hide the current form window
        win.withdraw()

        # Open the second details-filled window
        printresult(name_val, gmail_val, phone_val, password_val)

    win = tk.Tk()
    win.title('Form')
    win['bg'] = '#D2254B'
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.geometry(f'{win_width}x{win_height}+{(screen_width//2)-(win_width//2)}+{(screen_height//2)-(win_height//2)}')

    # Form title
    tk.Label(win, text="Details Form .... ", font=('Arial', 20, 'bold')).place(x=500, y=10)

    # Labels
    tk.Label(win, text="Name     :", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=50)
    tk.Label(win, text="Gmail    :", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=100)
    tk.Label(win, text="Phone No :", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=150)
    tk.Label(win, text="Password :", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=200)

    # Entry fields
    name_entry = tk.Entry(win, font=('Arial', 10, 'bold'), foreground='#1b1b1b', background='pink', width='60')
    name_entry.place(x=150, y=50)

    gmail_entry = tk.Entry(win, font=('Arial', 10, 'bold'), foreground='#1b1b1b', background='pink', width='60')
    gmail_entry.place(x=150, y=100)

    phone_entry = tk.Entry(win, font=('Arial', 10, 'bold'), foreground='#1b1b1b', background='pink', width='60')
    phone_entry.place(x=150, y=150)

    password_entry = tk.Entry(win, font=('Arial', 10, 'bold'), foreground='#1b1b1b', background='pink', width='60', show="*")
    password_entry.place(x=150, y=200)

    # Submit button
    submit_btn = tk.Button(win, text='Submit', foreground='#1b1b1b', background='pink', command=submit_form)
    submit_btn.place(x=150, y=250)

    win.mainloop()

def printresult(name, gmail, phone_no, password):
    win = tk.Tk()
    win.title('Form Submitted')
    win['bg'] = '#D2254B'
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.geometry(f'{win_width}x{win_height}+{(screen_width//2)-(win_width//2)}+{(screen_height//2)-(win_height//2)}')

    # Display submitted details
    tk.Label(win, text="Details Filled .... ", font=('Arial', 20, 'bold')).place(x=500, y=10)
    tk.Label(win, text=f"Name     : {name}", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=50)
    tk.Label(win, text=f"Gmail    : {gmail}", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=100)
    tk.Label(win, text=f"Phone No : {phone_no}", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=150)
    tk.Label(win, text=f"Password : {password}", font=('Arial', 15, 'bold'), foreground='#1b1b1b', background='#D2254B').place(x=15, y=200)

    win.mainloop()

form()
