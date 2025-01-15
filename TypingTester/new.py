# import customtkinter as ctk
# from tkinter import messagebox
# import random
# import time
# import sqlite3



# win_width =1500
# win_height = 650

# # Database 
# def setup_database():
#     conn = sqlite3.connect("progress_reports.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS progress (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             wpm REAL,
#             accuracy REAL,
#             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#         )
#     """)
#     conn.commit()
#     conn.close()

# setup_database()

# SENTENCES = [
#     "Computer programming is the composition of sequences of instructions, called programs, that computers can follow to perform tasks. It involves designing and implementing algorithms, step-by-step specifications of procedures, by .",
#     "Proficient programming usually requires expertise in several different subjects, including knowledge of the application domain, details of programming languages and generic code libraries, specialized algorithms, and formal logic.",
#     "Auxiliary tasks accompanying and related to programming include analyzing requirements, testing, debugging (investigating and fixing problems), implementation of build systems, and management of derived artifacts, such as programs" ]
# def main():
#     def getName():
#         win.withdraw()
#         if check(name_entry.get()):
#             showTyping(name_entry.get().title())
#         else:
#             messagebox.showerror('Error', 'Enter a Valid Name')
#             win.deiconify()

#     win = ctk.CTk()
#     win.title('Typing Speed Test - Enter Name')
   

#     screen_width = win.winfo_screenwidth()
#     screen_height = win.winfo_screenheight()
#     win.geometry(f'{win_width}x{win_height}+{(screen_width//2)-(win_width//2)}+{(screen_height//2)-(win_height//2)}')

#     title_label = ctk.CTkLabel(win, text='Please Enter Your Name:', font=ctk.CTkFont(size=30, weight="bold"))
#     title_label.place(x=400, y=100)

#     name_entry = ctk.CTkEntry(win, width=600, font=ctk.CTkFont(size=30))
#     name_entry.place(x=250, y=200)

#     next_button = ctk.CTkButton(win, text='Next', width=200, font=ctk.CTkFont(size=20), command=getName)
#     next_button.place(x=900, y=400)

#     view_progress_button = ctk.CTkButton(win, text='View Progress', width=200, font=ctk.CTkFont(size=20), command=viewProgress)
#     view_progress_button.place(x=650, y=400)

#     win.mainloop()

# def showTyping(user_name):
#     def getStartTime():
#         if not l:
#             l.append(time.time())
#             updateTimer()

#     def updateTimer():
#         if l:
#             elapsed = time.time() - l[0]
#             timer_label.configure(text=f'Time: {int(elapsed)} sec')
#             if elapsed >= 60:
#                 showResult(win, user_name, sentence, entrySentence.get(), l[0])
#             else:
#                 global timer_id
#                 timer_id = win.after(1000, updateTimer)

#     def getEntry():
#         if 'timer_id' in globals():
#             win.after_cancel(timer_id)
#         showResult(win, user_name, sentence, entrySentence.get(), l[0])

#     def reStart():
#         win.withdraw()
#         showTyping(user_name=user_name)

#     def goBack():
#         win.destroy()
#         main()

#     win = ctk.CTk()
#     win.title('Typing Speed Test')


#     screen_width = win.winfo_screenwidth()
#     screen_height = win.winfo_screenheight()
#     win.geometry(f'{win_width}x{win_height}+{(screen_width//2)-(win_width//2)}+{(screen_height//2)-(win_height//2)}')

#     welcome_label = ctk.CTkLabel(win, text=f'Welcome {user_name}! Check Your Typing Speed & Accuracy',
#                                  font=ctk.CTkFont(size=25, weight="bold"))
#     welcome_label.place(x=70, y=10)

#     timer_label = ctk.CTkLabel(win, text='Time: 0 sec', font=ctk.CTkFont(size=20))
#     timer_label.place(x=1200, y=10)

#     sentence_label = ctk.CTkLabel(win, text='Type the following sentence:', font=ctk.CTkFont(size=20, weight="bold"))
#     sentence_label.place(x=70, y=70)

#     sentence = getSentence()
#     display_sentence = ctk.CTkLabel(win, text=sentence, font=('Arial',20, 'bold'), wraplength=1300)
#     display_sentence.place(x=80, y=150)

#     entrySentence = ctk.CTkEntry(win, width=800, font=ctk.CTkFont(size=30))
#     entrySentence.place(x=50, y=330)

#     l = []
 
#     start_button = ctk.CTkButton(win, text='Start', width=150, font=('Arial',30, 'bold'), command=getStartTime)
#     start_button.place(x=50, y=450)

#     submit_button = ctk.CTkButton(win, text='Submit', width=150, font=('Arial',30, 'bold'), command=getEntry)
#     submit_button.place(x=350, y=450)

#     restart_button = ctk.CTkButton(win, text='Restart', width=150, font=('Arial',30, 'bold'), command=reStart)
#     restart_button.place(x=650, y=450)

#     back_button = ctk.CTkButton(win, text='Back', width=150, font=('Arial',30, 'bold'), command=goBack)
#     back_button.place(x=950, y=450)

#     win.mainloop()

# def showResult(win, user_name, sentence, user_input, start_time):
#     end_time = time.time()
#     time_taken = end_time - start_time
#     word_count = len(user_input.split())
#     wpm = (word_count / time_taken) * 60

#     correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(sentence) and c == sentence[i])
#     accuracy = (correct_chars / len(user_input)) * 100

#     save_progress(user_name, wpm, accuracy)

#     messagebox.showinfo("Typing Result", f"Your Typing Result:\n\nWord per min: {wpm:.2f}\nAccuracy: {accuracy:.2f}%")
    
y='muhammad sohail'
# def save_progress(name, wpm, accuracy):
#     conn = sqlite3.connect("progress_reports.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO progress (name, wpm, accuracy) VALUES (?, ?, ?)", (name, wpm, accuracy))
#     conn.commit()
#     conn.close()

# def viewProgress():
#     def closeProgress():
#         progress_win.destroy()

#     def deleteAllProgress():
#         if messagebox.askyesno("Confirm", "Are you sure you want to delete all progress records?"):
#             conn = sqlite3.connect("progress_reports.db")
#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM progress")
#             conn.commit()
#             conn.close()
#             messagebox.showinfo("Deleted", "All progress records have been deleted.")
#             progress_win.destroy()

#     progress_win = ctk.CTk()
#     progress_win.title("Progress Report")
#     progress_win.geometry("800x600")

#     conn = sqlite3.connect("progress_reports.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, wpm, accuracy, timestamp FROM progress ORDER BY timestamp DESC")
#     rows = cursor.fetchall()
#     conn.close()

#     title_label = ctk.CTkLabel(progress_win, text="Progress Report", font=ctk.CTkFont(size=30, weight="bold"))
#     title_label.pack(pady=20)

#     for row in rows:
#         entry = f"Name: {row[0]}, WPM: {row[1]:.2f}, Accuracy: {row[2]:.2f}%, Date: {row[3]}"
#         progress_label = ctk.CTkLabel(progress_win, text=entry, font=ctk.CTkFont(size=15))
#         progress_label.pack(anchor="w", padx=20)

#     delete_button = ctk.CTkButton(progress_win, text="Delete All Progress", command=deleteAllProgress)
#     delete_button.pack(pady=20)

#     close_button = ctk.CTkButton(progress_win, text="Close", command=closeProgress)
#     close_button.pack(pady=10)

#     progress_win.mainloop()

# def getSentence():
#     return random.choice(SENTENCES)

# def check(name):
#     name = name.strip()
#     return name.isalpha() and len(name) > 0

# main() 
x='https//www.instagram.com/salar_akhater_ll?igsh=MWInejY4ZzMDZxcQ=='
print(y)