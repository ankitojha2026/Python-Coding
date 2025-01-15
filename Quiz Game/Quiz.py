# this class is works as a data user defiend dataStructor for the question and answer
# o1=option1,  o2=option2
import random
class question_Answer:
    def __init__(self,ques,o1,o2,o3,o4,ans):
        self.ques=ques
        self.o1=o1
        self.o2=o2
        self.o3=o3
        self.o4=o4
        self.ans=ans

class quiz:
   
    def __init__(self):
        self.data=[]
        self.right_ans=0
        self.wronge_ans=0
        #add question 
    def add_question(self,ques,o1,o2,o3,o4,ans):
        self.data.append(question_Answer(ques,o1,o2,o3,o4,ans))

    #display all the question 
    def display(self,idx,i):
        print("________________________________________________________________________________________________________________________________")
        print(f'''{i}. {self.data[idx].ques}\n
(A) {self.data[idx].o1}     (B) {self.data[idx].o2}     (C) {self.data[idx].o3}     (D) {self.data[idx].o4}\n''')
        
        # it is match and return the the output
        ans=self.getAns(idx)
        if ans==True:
            self.right_ans+=1
            print("\nCorrect\n")
        else:
            self.wronge_ans+=1
            print("\nWrong Ans !!! Correct Ans -> : ",self.data[idx].ans ,"\n")
       # print("________________________________________________________________________________________________________________________________")    

    #this method return thye right or wrong result
    def getAns(self,idx):

        while True:
            ans=input("").upper()
            if len(ans)==1 and ans in "ABCD":
                if ans==self.data[idx].ans:
                    return True
                else:
                    return False
            else:
                print("Press Valid Ans \n")

    
    def start(self):
        temp=[]
        i=1
        while True:
            x=random.randint(0,len(self.data)-1)
            if not (x in temp):
                temp.append(x)
                #Calling to the display method and this method return true or false.
                self.display(x,i)
                i=i+1   
            if len(self.data)==len(temp):
                break
    def result(self):
        print(f'''\n result 
__________________________
Total Ques : {len(self.data)}
Right Ans : {self.right_ans}
Wrong Ans : {self.wronge_ans}\n
Thank You !!!''')

    def getSubject(self):
        while True:
            
         subject=input("Choose Your Sub Python, Java , C , C++:\n").title()
         if subject in ["Python","Java","C","C++"] :
             return subject
         else:
             print("Choose Again....!")   

    def main(self):

        print("Welcom The Quiz Game.....\n")
        name=input("Enter Your Name :\n").title()
        print(f'''Welcom You ! {name} In This Game \n''')
        subject=self.getSubject()
        if subject == "Python":
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
        
        elif subject == "Java":
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
        
        elif subject == "C":
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
        
        else:  # C++
            self.add_question("What is C++?", "C++ is a PL", "No PL", "Yes PL", "Not maintained", "A")
            self.add_question("Who is known as the father of C++?", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", "Dr. E. F. Codd", "B")
            self.add_question("C++ is ________ language.", "High level", "Low level", "Middle level", "Machine level", "C")
            self.add_question("Which symbol is used to end a statement in C++?", ".", ",", ";", ":", "C")
            self.add_question("Which function is used to output a string in C++?", "output()", "echo()", "write()", "cout<<", "D")
            self.add_question("Which keyword is used to define a variable in C++?", "var", "dim", "int", "declare", "C")
            self.add_question("What is the size of int in C++?", "1 byte", "2 or 4 bytes", "8 bytes", "None", "B")
            self.add_question("Which operator is used for bitwise OR?", "&", "|", "^", "~", "B")
            self.add_question("Which loop is used to iterate a block of code until a specified condition is false?", "for", "while", "do-while", "All of the above", "D")
            

        self.start()
        self.result()

i=quiz()
i.main()


        
