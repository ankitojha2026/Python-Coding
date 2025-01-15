import random
import tkinter as tk
from tkinter import messagebox

class QuestionAnswer:
    def __init__(self, ques, o1, o2, o3, o4, ans):
        self.ques = ques
        self.o1 = o1
        self.o2 = o2
        self.o3 = o3
        self.o4 = o4
        self.ans = ans

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        # Set the window dimensions and center it
        self.root.geometry("1100x1600")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 1100) // 2
        y = (screen_height - 1600) // 2
        self.root.geometry(f"1100x1600+{x}+{y}")
        
        self.data = []
        self.right_ans = 0
        self.wrong_ans = 0
        self.current_question = None
        self.question_index = 0
        self.selected_answer = tk.StringVar()
        self.user_name = ""
        
        self.setup_initial_widgets()
    
    def setup_initial_widgets(self):
        # Welcome screen for user details
        self.name_label = tk.Label(self.root, text="Enter Your Name:", font=("Arial", 14))
        self.name_label.pack(pady=20)
        
        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=10)
        
        self.subject_label = tk.Label(self.root, text="Choose Your Subject (Python, Java, C, C++):", font=("Arial", 14))
        self.subject_label.pack(pady=20)
        
        self.subject_entry = tk.Entry(self.root, font=("Arial", 14))
        self.subject_entry.pack(pady=10)
        
        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Arial", 14))
        self.start_button.pack(pady=20)
    
    def start_quiz(self):
        # Get user name and subject
        self.user_name = self.name_entry.get().title()
        subject = self.subject_entry.get().title()
        
        # Clear initial widgets
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.subject_label.pack_forget()
        self.subject_entry.pack_forget()
        self.start_button.pack_forget()
        
        # Load questions based on subject
        if subject == "Python":
            self.add_python_questions()
        elif subject == "Java":
            self.add_java_questions()
        elif subject == "C":
            self.add_c_questions()
        elif subject == "C++":
            self.add_cpp_questions()
        else:
            messagebox.showerror("Error", "Invalid subject. Choose Python, Java, C, or C++.")
            self.root.quit()
        
        # Display first question
        self.setup_quiz_widgets()
        self.display_question()
    
    def add_python_questions(self):
        self.data.append(QuestionAnswer("Who developed Python Programming Language?", 
                                        "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", "C"))
        self.data.append(QuestionAnswer("Which type of Programming does Python support?", 
                                        "Object-oriented programming", "Structured programming", "Functional programming", "All of the mentioned", "D"))
        self.data.append(QuestionAnswer("Is Python case sensitive when dealing with identifiers?", 
                                        "No", "Yes", "Machine dependent", "None of the mentioned", "B"))
        # Add more questions as needed
    
    def add_java_questions(self):
        self.data.append(QuestionAnswer("What is Java?", "Java is a programming language", "No PL", "Yes PL", "Not maintained", "A"))
        self.data.append(QuestionAnswer("Who is the founder of Java?", "James Gosling", "Dennis Ritchie", "Ken Thompson", "Bjarne Stroustrup", "A"))
        # Add more questions as needed
    
    def add_c_questions(self):
        self.data.append(QuestionAnswer("What is C?", "C is a PL", "No PL", "Yes PL", "Not maintained", "A"))
        self.data.append(QuestionAnswer("Who is known as the father of C language?", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Dr. E. F. Codd", "C"))
        # Add more questions as needed
    
    def add_cpp_questions(self):
        self.data.append(QuestionAnswer("What is C++?", "C++ is a PL", "No PL", "Yes PL", "Not maintained", "A"))
        self.data.append(QuestionAnswer("Who is known as the father of C++?", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Dr. E. F. Codd", "B"))
        # Add more questions as needed
    
    def setup_quiz_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=700)
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_answer, value=chr(65 + i), font=("Arial", 12))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)
        
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12, "italic"))
        self.feedback_label.pack(pady=10)
        
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)
    
    def display_question(self):
        self.current_question = self.data[self.question_index]
        self.question_label.config(text=f"Q{self.question_index + 1}: {self.current_question.ques}")
        options = [self.current_question.o1, self.current_question.o2, self.current_question.o3, self.current_question.o4]
        
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option)
        
        self.selected_answer.set(None)
        self.feedback_label.config(text="")
    
    def check_answer(self):
        selected = self.selected_answer.get()
        if selected:
            if selected == self.current_question.ans:
                self.right_ans += 1
                self.feedback_label.config(text="Correct!", fg="green")
            else:
                self.wrong_ans += 1
                self.feedback_label.config(text=f"Wrong! Correct Answer: {self.current_question.ans}", fg="red")
    
    def next_question(self):
        self.check_answer()
        self.question_index += 1
        if self.question_index < len(self.data):
            self.display_question()
        else:
            self.show_result()
    
    def show_result(self):
        # Clear quiz widgets
        self.question_label.pack_forget()
        for rb in self.option_buttons:
            rb.pack_forget()
        self.feedback_label.pack_forget()
        self.next_button.pack_forget()
        
        # Display result
        result_text = f"Quiz Over!\n\nName: {self.user_name}\nTotal Questions: {len(self.data)}\nCorrect Answers: {self.right_ans}\nWrong Answers: {self.wrong_ans}"
        self.result_label = tk.Label(self.root, text=result_text, font=("Arial", 14))
        self.result_label.pack(pady=50)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14))
        self.exit_button.pack(pady=20)

# Running the Quiz
root = tk.Tk()
quiz_app = Quiz(root)
root.mainloop()
