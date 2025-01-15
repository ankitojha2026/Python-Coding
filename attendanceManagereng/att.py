import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# Database setup
def setup_database():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        due_date TEXT,
                        status TEXT DEFAULT 'Pending'
                    )''')
    conn.commit()
    conn.close()

# Functions to manage tasks
def add_task(title, description, due_date):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, description, due_date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task added successfully!")

def fetch_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, status):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task status updated!")

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task deleted successfully!")

# GUI Functions
def open_add_task():
    def save_task():
        title = title_entry.get()
        description = desc_entry.get("1.0", "end").strip()
        due_date = due_date_entry.get()

        if not title or not due_date:
            messagebox.showerror("Error", "Title and Due Date are required.")
            return

        add_task(title, description, due_date)
        add_task_window.destroy()
        update_task_list()

    add_task_window = ctk.CTk()
    add_task_window.title("Add Task")
    add_task_window.geometry("400x400")

    ctk.CTkLabel(add_task_window, text="Task Title:").pack(pady=5)
    title_entry = ctk.CTkEntry(add_task_window)
    title_entry.pack(pady=5)

    ctk.CTkLabel(add_task_window, text="Description:").pack(pady=5)
    desc_entry = ctk.CTkTextbox(add_task_window, height=100)
    desc_entry.pack(pady=5)

    ctk.CTkLabel(add_task_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
    due_date_entry = ctk.CTkEntry(add_task_window)
    due_date_entry.pack(pady=5)

    ctk.CTkButton(add_task_window, text="Save Task", command=save_task).pack(pady=10)

def open_view_tasks():
    def mark_complete(task_id):
        update_task_status(task_id, "Completed")
        update_task_list()

    def remove_task(task_id):
        delete_task(task_id)
        update_task_list()

    view_tasks_window = ctk.CTkToplevel()
    view_tasks_window.title("View Tasks")
    view_tasks_window.geometry("600x400")

    tasks = fetch_tasks()

    for task in tasks:
        frame = ctk.CTkFrame(view_tasks_window)
        frame.pack(pady=5, fill="x")

        task_label = ctk.CTkLabel(frame, text=f"{task[1]} (Due: {task[3]}, Status: {task[4]})", anchor="w")
        task_label.pack(side="left", padx=10)

        complete_btn = ctk.CTkButton(frame, text="Mark Complete", command=lambda tid=task[0]: mark_complete(tid))
        complete_btn.pack(side="right", padx=5)

        delete_btn = ctk.CTkButton(frame, text="Delete", command=lambda tid=task[0]: remove_task(tid))
        delete_btn.pack(side="right", padx=5)

def update_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    tasks = fetch_tasks()

    for task in tasks:
        task_label = ctk.CTkLabel(task_list_frame, text=f"{task[1]} (Due: {task[3]}, Status: {task[4]})")
        task_label.pack(pady=5)

# Main GUI Setup
app = ctk.CTk()
app.title("Task Management System")
app.geometry("600x500")

ctk.CTkLabel(app, text="Task Management System", font=("Arial", 24)).pack(pady=20)

ctk.CTkButton(app, text="Add Task", command=open_add_task).pack(pady=10)
ctk.CTkButton(app, text="View Tasks", command=open_view_tasks).pack(pady=10)

task_list_frame = ctk.CTkFrame(app)
task_list_frame.pack(pady=20, fill="both", expand=True)

setup_database()
update_task_list()

app.mainloop()
