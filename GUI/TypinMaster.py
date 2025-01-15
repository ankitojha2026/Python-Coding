import tkinter as tk
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk, ImageSequence

win_width = 1500
win_height = 650






# List of sentences
SENTENCES = [
    "Computer programming is the composition of sequences of instructions, called programs, that computers can follow to perform tasks. It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages. Programmers typically use high-level programming languages that are more easily intelligible to humans than machine code, which is directly executed by the central processing unit.",
    "Proficient programming usually requires expertise in several different subjects, including knowledge of the application domain, details of programming languages and generic code libraries, specialized algorithms, and formal logic.",
    "Auxiliary tasks accompanying and related to programming include analyzing requirements, testing, debugging (investigating and fixing problems), implementation of build systems, and management of derived artifacts, such as programs' machine code. While these are sometimes considered programming, often the term software development is used for this larger overall process.",
    

]

def inputName():
    # This function handles the name input screen
    def getName():
        win.withdraw()
        if check(name.get()):
            showTyping(name.get().title())
        else:
            messagebox.showerror('Error', 'Enter a Valid Name')
            win.deiconify()

    win = tk.Tk()
    win.title('Typing Speed Test - Enter Name')
    win['bg'] = 'Skyblue'
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.geometry(f'{win_width}x{win_height}+{(screen_width//2)-(win_width//2)}+{(screen_height//2)-(win_height//2)}')

    tk.Label(win, text='Please Enter Your Name:', font=('Arial', 30, 'bold'), bg='Skyblue').place(x=400, y=100)
    name = tk.Entry(win, width=47, background='White', foreground='Black', font=('Arial', 30, 'bold'))
    name.place(x=250, y=200)

    tk.Button(win, text='Next', height=1, width=15, background='#07ABC4', foreground='Black', font=('Arial', 20, 'bold'), command=getName).place(x=900, y=400)
    win.mainloop()

def showTyping(user_name):
    # This function handles the typing test screen
    def getStartTime():
        if not l:
            l.append(time.time())
            updateTimer()

    def updateTimer():
        if l:
            elapsed = time.time() - l[0]
            timer_label.config(text=f'Time: {int(elapsed)} sec')
            if elapsed < 60:
                global timer_id
                timer_id = win.after(1000, updateTimer)

    def getEntry():
        if 'timer_id' in globals():
            win.after_cancel(timer_id)  # Stop the timer
        showResult(win, user_name, sentence, entrySentence.get(), l[0])

    def reStart():
        win.withdraw()
        showTyping(user_name=user_name)

    win = tk.Tk()
    win.title('Typing Speed Test')
    win['bg'] = 'white'
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.geometry(f'{win_width}x{win_height}+{(screen_width//2)-(win_width//2)}+{(screen_height//2)-(win_height//2)}')

    tk.Label(win, text=f'Welcome {user_name}! Check Your Typing Speed & Accuracy', foreground='white', font=('Arial',25, 'bold'), bg='black').place(x=70, y=10)

    timer_label = tk.Label(win, text='Time: 0 sec', font=('Arial', 20, 'bold'), foreground='black', bg='white')
    timer_label.place(x=1200, y=10)

    tk.Label(win, text='Type the following sentence:', font=('Arial', 20, 'bold'), foreground='red', bg='white').place(x=70, y=70)

    sentence = getSentence()
    tk.Label(win, text=sentence, font=('Arial', 17, 'bold'), foreground='black', bg='white', wraplength=1300).place(x=80, y=150)

    entrySentence = tk.Entry(win, width=40, background='#A8C2ED', foreground='Black', font=("Arial", 40, "bold"))
    entrySentence.place(x=50, y=330)

    # result 
   

    l = []

    tk.Button(win, text='Start', height=1, width=15, font=('Arial', 20, 'bold'), foreground='Black', bg='green', command=getStartTime).place(x=50, y=450)
    tk.Button(win, text='Submit', height=1, width=15, font=('Arial', 20, 'bold'), foreground='Black', bg='red', command=getEntry).place(x=350, y=450)
    tk.Button(win, text='Restart', height=1, width=15, font=('Arial', 20, 'bold'), foreground='Black', bg='#07ABC4', command=reStart).place(x=650, y=450)

    win.mainloop()

def showResult(win, user_name, sentence, user_input, start_time):
    # This function calculates and displays the result
    end_time = time.time()
    time_taken = end_time - start_time
    word_count = len(user_input.split())
    wpm = (word_count / time_taken) * 60

    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(sentence) and c == sentence[i])
    accuracy = (correct_chars / len(sentence)) * 100

    tk.Label(win,text=f'''Your Typing Result !\n\nWord per min : {wpm:.2f}\n
    Accuracy :{accuracy:.2f}''',font=('Arial',30,'bold') , background='red' , foreground='white').place(x=950, y=400)
    
    
   

def getSentence():
    # Returns a random sentence
    return random.choice(SENTENCES)

def check(name):
    # Checks if the name is valid
    name = name.strip()
    return name.isalpha() and len(name) > 0

inputName()
