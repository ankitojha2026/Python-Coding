import customtkinter as ctk

class StudentManagementUI:
    def __init__(self):
        # Set appearance mode and default theme
        ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

        # Initialize the main window
        self.root = ctk.CTk()
        self.root.title("Student Management System")
        self.root.geometry("900x600")

        # Create navigation and module frames
        self.create_navigation()
        self.create_frames()

    def create_navigation(self):
        """Create the navigation bar with buttons."""
        self.nav_frame = ctk.CTkFrame(self.root, width=200)
        self.nav_frame.pack(side="left", fill="y")

        # Navigation Buttons
        nav_buttons = [
            ("Home", self.home_frame),
            ("Add Student", self.add_student_frame),
            ("View Students", self.view_students_frame),
            ("Attendance", self.attendance_frame),
            ("Reports", self.report_frame),
        ]

        for text, frame in nav_buttons:
            btn = ctk.CTkButton(self.nav_frame, text=text, command=lambda f=frame: self.switch_frame(f))
            btn.pack(pady=10, padx=10)

    def create_frames(self):
        """Create frames for different sections."""
        self.home_frame = ctk.CTkFrame(self.root)
        self.add_student_frame = ctk.CTkFrame(self.root)
        self.view_students_frame = ctk.CTkFrame(self.root)
        self.attendance_frame = ctk.CTkFrame(self.root)
        self.report_frame = ctk.CTkFrame(self.root)

        # Place all frames at the same position
        for frame in (self.home_frame, self.add_student_frame, self.view_students_frame, self.attendance_frame, self.report_frame):
            frame.place(x=200, y=0, width=700, height=600)

        # Add placeholder labels
        ctk.CTkLabel(self.home_frame, text="Home Screen", font=("Arial", 20)).pack(pady=20)
        ctk.CTkLabel(self.add_student_frame, text="Add Student Module", font=("Arial", 20)).pack(pady=20)
        ctk.CTkLabel(self.view_students_frame, text="View Students Module", font=("Arial", 20)).pack(pady=20)
        ctk.CTkLabel(self.attendance_frame, text="Attendance Module", font=("Arial", 20)).pack(pady=20)
        ctk.CTkLabel(self.report_frame, text="Reports Module", font=("Arial", 20)).pack(pady=20)

    def switch_frame(self, frame):
        """Bring the selected frame to the front."""
        frame.tkraise()

    def run(self):
        """Run the main application loop."""
        self.home_frame.tkraise()  # Show the home frame by default
        self.root.mainloop()


# Main Execution
if __name__ == "__main__":
    app = StudentManagementUI()
    app.run()
