from tkinter.constants import VERTICAL

import customtkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
from customtkinter import CTkButton, CTkFrame


class SMSClass:
    def __init__(self):


        #functions

        #new student button
        def new_student():
            pass

        #add student button
        def add_student():
            pass


        #update button

        def update():
            pass

        #delete button
        def delete():
            pass

        # delete all button
        def delete_all():
            pass


        # print button
        def print():
            pass

        #search Button
        def search():
            pass
        # show all button
        def show_all():
            pass







        win = tk.CTk()
        win_width=1500
        win_height=750
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        win.configure(fg_color='#161C30')
        win.geometry(
            f'{win_width}x{win_height}+{(screen_width // 2) - (win_width // 2)}+{(screen_height // 2) - (win_height // 2)}')

        win.resizable(0, 0)
        win.title('Deskbord')
        image=tk.CTkImage(Image.open('Smstopb.png') , size=(1500,150))
        topImg=tk.CTkLabel(win,image=image ,text='')
        topImg.grid(row=0,column=0,columnspan=2)

        #left frame
        leftFrame=tk.CTkFrame(win,fg_color='#161C30')
        leftFrame.grid(row=1,column=0)



        # roll number lebel
        rolllable=tk.CTkLabel(leftFrame,text='Roll No :',font=('arial',22,'bold'))
        rolllable.grid(row=0 , column=0,padx=(0,30) ,pady=15,sticky='w')

        # roll number Entry

        rollNoEntry=tk.CTkEntry(leftFrame,font=('Arial',18,'bold') ,width=230 ,height=22,border_color='white')
        rollNoEntry.grid(row=0,column=1 ,pady=15)
        # name
        namelable = tk.CTkLabel(leftFrame, text='Name :', font=('arial', 22, 'bold'))
        namelable.grid(row=1, column=0, padx=(0, 30),pady=15,sticky='w')

        # roll number Entry

        nameEntry = tk.CTkEntry(leftFrame, font=('Arial', 18, 'bold'), width=230, height=22,border_color='white')
        nameEntry.grid(row=1, column=1 ,pady=15)

        phonelable = tk.CTkLabel(leftFrame, text='Phone :', font=('arial', 22, 'bold'))
        phonelable.grid(row=2, column=0, padx=(0, 30),pady=15,sticky='w')

        # roll number Entry

        phoneEntry = tk.CTkEntry(leftFrame, font=('Arial', 18, 'bold'), width=230, height=22,border_color='white')
        phoneEntry.grid(row=2, column=1 ,pady=15)

        genderlable = tk.CTkLabel(leftFrame, text='Gender :', font=('arial', 22, 'bold'))
        genderlable.grid(row=3, column=0, padx=(0, 30), pady=15,sticky='w')

        GenderCombo = tk.CTkComboBox(leftFrame,values=['Male','Female'], font=('Arial', 18, 'bold'), width=230, height=22,border_color='white')
        GenderCombo.grid(row=3, column=1, pady=15)
        GenderCombo.set('Male')

        DOBlable = tk.CTkLabel(leftFrame, text='DOB :', font=('arial', 22, 'bold'))
        DOBlable.grid(row=4, column=0, padx=(0, 30), pady=15, sticky='w')

        # roll number Entry

        DOBEntry = tk.CTkEntry(leftFrame, font=('Arial', 18, 'bold'), width=230, height=22, border_color='white',placeholder_text='DD / MM / YYYY')
        DOBEntry.grid(row=4, column=1, pady=15)

        Addlable = tk.CTkLabel(leftFrame, text='Address :', font=('arial', 22, 'bold'))
        Addlable.grid(row=5, column=0, padx=(0, 30), pady=15, sticky='w')

        # roll number Entry

        AddEntry = tk.CTkEntry(leftFrame, font=('Arial', 18, 'bold'), width=230, height=22, border_color='white',
                               )
        AddEntry.grid(row=5, column=1, pady=15)

        # right frame
        rightFrame = tk.CTkFrame(win,fg_color='white')
        rightFrame.grid(row=1, column=1,pady=(15,0))

        searchby=['Roll no','Name','DOB','Address','Gender']
        search = tk.CTkComboBox(rightFrame, values=searchby, font=('Arial', 18, 'bold'), width=230,
                                     height=22, border_color='white')
        search.grid(row=0, column=0)
        search.set('Search By')

        #search entry
        searchEntry = tk.CTkEntry(rightFrame, font=('Arial', 18, 'bold'), width=230, height=22, border_color='white')
        searchEntry.grid(row=0, column=1,padx=(20,0))

        # search button
        searchButton = tk.CTkButton(rightFrame, font=('Arial', 17), width=100, height=25,text='Search',cursor='hand2')
        searchButton.grid(row=0, column=2, padx=(20, 0))

        # search All

        searchAllButton = tk.CTkButton(rightFrame, font=('Arial', 17), width=100, height=25, text='Show All',
                                    cursor='hand2')
        searchAllButton.grid(row=0, column=3,pady=5)

        tree=ttk.Treeview(rightFrame,height=25 )
        tree.grid(row=1,column=0 , columnspan=4)
        tree['column']=('Roll No','Name','Phone','Gender','DOB','Address')
        tree.heading('Roll No',text='Roll No')
        tree.heading('Name', text='Name')
        tree.heading('Phone', text='Phone')
        tree.heading('Gender', text='Gender')
        tree.heading('DOB', text='DOB')
        tree.heading('Address', text='Address')
        tree.config(show='headings')
        tree.column('Roll No',width=200)
        tree.column('Name', width=300)
        tree.column('Phone', width=200)
        tree.column('Gender', width=100)
        tree.column('DOB', width=100)
        tree.column('Address', width=400)

        # style the tree font.

        style=ttk.Style()
        style.configure('Treeview.Heading',font=('Arial',17,'bold'))


        # scrollbar
        scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL)
        scrollbar.grid(row=1,column=4,sticky='ns')



        # button frame
        buttonFrame=CTkFrame(win,fg_color='#161C30')
        buttonFrame.grid(row=2,column=0,columnspan=2)

    #new student button
        newStudent=CTkButton(buttonFrame,text='New Student',font=('Arial',15,'bold'),width=180,height=30,corner_radius=15,cursor='hand2')
        newStudent.grid(row=0,column=0,pady=10,padx=15)
    #add new Student
        addStudent = CTkButton(buttonFrame, text='Add Student', font=('Arial', 15, 'bold'), width=180, height=30,
                               corner_radius=15,cursor='hand2')
        addStudent.grid(row=0, column=1, pady=10, padx=15)

        # update button

        updateStudent = CTkButton(buttonFrame, text='Update', font=('Arial', 15, 'bold'), width=180, height=30,
                               corner_radius=15,cursor='hand2')
        updateStudent.grid(row=0, column=2, pady=10, padx=15)


        # delete button
        deleteStudent = CTkButton(buttonFrame, text='Delete', font=('Arial', 15, 'bold'), width=180, height=30,
                               corner_radius=15,cursor='hand2')
        deleteStudent.grid(row=0, column=3, pady=10, padx=15)

        # delete all

        deleteAllStudent = CTkButton(buttonFrame, text='Delete All', font=('Arial', 15, 'bold'), width=180, height=30,
                               corner_radius=15,cursor='hand2')
        deleteAllStudent.grid(row=0, column=4, pady=10, padx=15)

        # print all data

        printAllStudent = CTkButton(buttonFrame, text='Print ', font=('Arial', 15, 'bold'), width=180, height=30,
                                     corner_radius=15, cursor='hand2')
        printAllStudent.grid(row=0, column=4, pady=10, padx=15)


        win.mainloop()

