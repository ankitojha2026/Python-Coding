import customtkinter as ctk

# Initialize the main app
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Student Management System")
app.geometry("800x600")

# Navigation Frame
nav_frame = ctk.CTkFrame(app, width=200)
nav_frame.pack(side="left", fill="y")

# Navigation Buttons
def switch_frame(frame):
    frame.tkraise()

home_frame = ctk.CTkFrame(app)
add_student_frame = ctk.CTkFrame(app)
view_students_frame = ctk.CTkFrame(app)
attendance_frame = ctk.CTkFrame(app)

for frame in (home_frame, add_student_frame, view_students_frame, attendance_frame):
    frame.place(x=200, y=0, width=600, height=600)

btn_home = ctk.CTkButton(nav_frame, text="Home", command=lambda: switch_frame(home_frame))
btn_home.pack(pady=20)
btn_add_student = ctk.CTkButton(nav_frame, text="Add Student", command=lambda: switch_frame(add_student_frame))
btn_add_student.pack(pady=20)
btn_view_students = ctk.CTkButton(nav_frame, text="View Students", command=lambda: switch_frame(view_students_frame))
btn_view_students.pack(pady=20)
btn_attendance = ctk.CTkButton(nav_frame, text="Attendance", command=lambda: switch_frame(attendance_frame))
btn_attendance.pack(pady=20)

# Example widgets in the "Add Student" frame
ctk.CTkLabel(add_student_frame, text="Add New Student", font=("Arial", 20)).pack(pady=10)
ctk.CTkEntry(add_student_frame, placeholder_text="Name").pack(pady=10)
ctk.CTkEntry(add_student_frame, placeholder_text="Roll Number").pack(pady=10)
ctk.CTkButton(add_student_frame, text="Save").pack(pady=10)

switch_frame(home_frame)  # Show the home frame initially
app.mainloop()

import sqlite3

# Database setup
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_number TEXT PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")
conn.commit()

# Add student function
def add_student(roll_number, name, course, marks):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll_number, name, course, marks))
    conn.commit()

# Get all students
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()
def save_student():
    roll_number = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()
    marks = marks_entry.get()
    add_student(roll_number, name, course, marks)
    update_table()

def update_table():
    for row in student_table.get_children():
        student_table.delete(row)
    for student in get_students():
        student_table.insert("", "end", values=student)

# Add Student Frame
roll_entry = ctk.CTkEntry(add_student_frame, placeholder_text="Roll Number")
roll_entry.pack(pady=10)
name_entry = ctk.CTkEntry(add_student_frame, placeholder_text="Name")
name_entry.pack(pady=10)
course_entry = ctk.CTkEntry(add_student_frame, placeholder_text="Course")
course_entry.pack(pady=10)
marks_entry = ctk.CTkEntry(add_student_frame, placeholder_text="Marks")
marks_entry.pack(pady=10)
ctk.CTkButton(add_student_frame, text="Save", command=save_student).pack(pady=10)

# View Students Frame
student_table = ttk.Treeview(view_students_frame, columns=("Roll", "Name", "Course", "Marks"))
student_table.heading("Roll", text="Roll Number")
student_table.heading("Name", text="Name")
student_table.heading("Course", text="Course")
student_table.heading("Marks", text="Marks")
student_table.pack(fill="both", expand=True)
