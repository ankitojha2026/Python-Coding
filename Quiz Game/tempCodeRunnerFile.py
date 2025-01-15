import random
import customtkinter as ctk

class QuestionAnswer:
    def __init__(self, ques, o1, o2, o3, o4, ans):
        self.ques = ques
        self.o1 = o1
        self.o2 = o2
        self.o3 = o3
        self.o4 = o4
        self.ans = ans

class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("600x500")

        self.data = []
        self.right_ans = 0
        self.wrong_ans = 0
        self.current_question_index = 0
        self.selected_subject = None
        self.temp_indices = []

        self.feedback_label = None  # Label to show feedback (correct/wrong)
        self.create_widgets()

    def create_widgets(self):
        self.intro_frame = ctk.CTkFrame(self)
        self.intro_frame.pack(fill="both", expand=True)

        self.quiz_frame = ctk.CTkFrame(self)

        self.result_frame = ctk.CTkFrame(self)

        self.intro_label = ctk.CTkLabel(self.intro_frame, text="Welcome to the Quiz Game", font=("Arial", 24))
        self.intro_label.pack(pady=20)

        self.name_entry = ctk.CTkEntry(self.intro_frame, placeholder_text="Enter Your Name")
        self.name_entry.pack(pady=10)

        self.subject_label = ctk.CTkLabel(self.intro_frame, text="Choose Your Subject", font=("Arial", 18))
        self.subject_label.pack(pady=10)

        self.subject_menu = ctk.CTkOptionMenu(self.intro_frame, values=["Python", "Java", "C", "C++"], command=self.set_subject)
        self.subject_menu.pack(pady=10)

        self.start_button = ctk.CTkButton(self.intro_frame, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)

        self.question_label = ctk.CTkLabel(self.quiz_frame, text="", font=("Arial", 18), wraplength=500)
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = ctk.CTkButton(self.quiz_frame, text=f"Option {i+1}", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5, fill="x")
            self.options.append(btn)

        self.feedback_label = ctk.CTkLabel(self.quiz_frame, text="", font=("Arial", 16), text_color="blue")
        self.feedback_label.pack(pady=10)

        self.result_label = ctk.CTkLabel(self.result_frame, text="", font=("Arial", 18))
        self.result_label.pack(pady=20)

        self.play_again_button = ctk.CTkButton(self.result_frame, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)

    def set_subject(self, subject):
        self.selected_subject = subject

    def add_question(self, ques, o1, o2, o3, o4, ans):
        self.data.append(QuestionAnswer(ques, o1, o2, o3, o4, ans))

    def load_questions(self):
        if self.selected_subject == "Python":
            self.add_question("Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", "C")
            self.add_question("Which type of Programming does Python support?", "Object-oriented programming", "Structured programming", "Functional programming", "All of the mentioned", "D")
            self.add_question("Is Python case sensitive when dealing with identifiers?", "No", "Yes", "Machine dependent", "None of the mentioned", "B")
            self.add_question("Which of the following is the correct extension of the Python file?", ".python", ".py", ".pl", ".p", "B")
            self.add_question("All keywords in Python are in _________", "Capitalized", "lower case", "Upper Case", "None of the mentioned", "D")
            self.add_question("Which language is more readable: Python or Java?", "Java", "Python", "Both", "None", "B")
            self.add_question("Which operator is used for exponentiation in Python?", "^", "*", "**", "&", "C")
            self.add_question("What is the output of print(2 * 3 ** 3)?", "54", "54.0", "None", "56", "A")
            self.add_question("Which keyword is used to define a function in Python?", "func", "define", "def", "function", "C")
            self.add_question("Which keyword is used for error handling in Python?", "try", "except", "error", "catch", "A")
            # Add more Python questions here...
        elif self.selected_subject == "Java":
            self.add_question("What is Java?", "Java is a programming language", "No PL", "Yes PL", "Not maintained", "A")
            self.add_question("Who is the founder of Java?", "James Gosling", "Dennis Ritchie", "Ken Thompson", "Bjarne Stroustrup", "A")
            self.add_question("What is JVM?", "Java Variable Machine", "Java Virtual Machine", "Java Virtual Management", "Java Version Machine", "B")
            self.add_question("Which of these is not a Java feature?", "Object-oriented", "Architecture Neutral", "Use of pointers", "Dynamic", "C")
            self.add_question("Which package contains the Random class?", "java.util", "java.lang", "java.awt", "java.io", "A")
            self.add_question("Which keyword is used for inheritance?", "this", "super", "extends", "final", "C")
            self.add_question("Which operator is used to allocate memory in Java?", "alloc", "malloc", "new", "mem", "C")
            self.add_question("What is the default value of an instance variable?", "null", "0", "Depends", "garbage value", "B")
            self.add_question("Which method is called when an object is created?", "init", "finalize", "new", "constructor", "D")
            self.add_question("Which of these are used for comments in Java?", "//", "/*", "/**/", "All of the mentioned", "D")
        
            # Add more Java questions here...
        elif self.selected_subject == "C":
            self.add_question("What is C?", "C is a PL", "No PL", "Yes PL", "Not maintained", "A")
            self.add_question("Who is known as the father of C language?", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Dr. E. F. Codd", "C")
            self.add_question("C is a ________ language.", "High level", "Low level", "Middle level", "Machine level", "C")
            self.add_question("Which symbol is used to end a statement in C?", ".", ",", ";", ":", "C")
            self.add_question("Which function is used to output a string in C?", "output()", "echo()", "write()", "printf()", "D")
            self.add_question("Which keyword is used to define a variable in C?", "var", "dim", "int", "declare", "C")
            self.add_question("What is the size of int in C?", "1 byte", "2 or 4 bytes", "8 bytes", "None", "B")
            self.add_question("Which operator is used for bitwise AND?", "&", "|", "^", "~", "A")
            self.add_question("Which loop is used to iterate a block of code until a specified condition is false?", "for", "while", "do-while", "All of the above", "D")
            self.add_question("Which header file is required for input-output functions?", "stdlib.h", "stdio.h", "conio.h", "math.h", "B")
            # Add more C questions here...
        elif self.selected_subject == "C++":
            self.add_question("What is C++?", "C++ is a PL", "No PL", "Yes PL", "Not maintained", "A")
            self.add_question("Who is known as the father of C++?", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Dr. E. F. Codd", "B")
            self.add_question("C++ is ________ language.", "High level", "Low level", "Middle level", "Machine level", "C")
            self.add_question("Which symbol is used to end a statement in C++?", ".", ",", ";", ":", "C")
            self.add_question("Which function is used to output a string in C++?", "output()", "echo()", "write()", "cout<<", "D")
            self.add_question("Which keyword is used to define a variable in C++?", "var", "dim", "int", "declare", "C")
            self.add_question("What is the size of int in C++?", "1 byte", "2 or 4 bytes", "8 bytes", "None", "B")
            self.add_question("Which operator is used for bitwise OR?", "&", "|", "^", "~", "B")
            self.add_question("Which loop is used to iterate a block of code until a specified condition is false?", "for", "while", "do-while", "All of the above", "D")
            
            # Add more C++ questions here...

    def start_quiz(self):
        if not self.name_entry.get():
            self.intro_label.configure(text="Please enter your name!", text_color="red")
            return

        if not self.selected_subject:
            self.intro_label.configure(text="Please select a subject!", text_color="red")
            return

        self.load_questions()

        if not self.data:
            self.intro_label.configure(text="No questions available for this subject!", text_color="red")
            return

        self.intro_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)

        self.temp_indices = list(range(len(self.data)))
        random.shuffle(self.temp_indices)

        self.current_question_index = 0
        self.show_question()

    def show_question(self):
        self.feedback_label.configure(text="")  # Clear previous feedback
        idx = self.temp_indices[self.current_question_index]
        question = self.data[idx]

        self.question_label.configure(text=f"{self.current_question_index + 1}. {question.ques}")
        self.options[0].configure(text=f"A. {question.o1}")
        self.options[1].configure(text=f"B. {question.o2}")
        self.options[2].configure(text=f"C. {question.o3}")
        self.options[3].configure(text=f"D. {question.o4}")

    def check_answer(self, selected_index):
        idx = self.temp_indices[self.current_question_index]
        question = self.data[idx]
        correct_answer = ord(question.ans) - ord("A")

        if selected_index == correct_answer:
            self.right_ans += 1
            self.feedback_label.configure(text="Correct!", text_color="green")
        else:
            self.wrong_ans += 1
            self.feedback_label.configure(text=f"Wrong! Correct answer: {question.ans}", text_color="red")

        self.current_question_index += 1
        if self.current_question_index < len(self.data):
            self.after(1000, self.show_question)  # Wait 1 second before showing the next question
        else:
            self.after(1000, self.show_result)  # Wait 1 second before showing the result

    def show_result(self):
        self.quiz_frame.pack_forget()
        self.result_frame.pack(fill="both", expand=True)
        self.result_label.configure(text=f"Quiz Over!\nRight: {self.right_ans}\nWrong: {self.wrong_ans}\nTotal: {len(self.data)}")

    def play_again(self):
        self.result_frame.pack_forget()
        self.intro_frame.pack(fill="both", expand=True)

        self.data.clear()
        self.right_ans = 0
        self.wrong_ans = 0
        self.current_question_index = 0

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
