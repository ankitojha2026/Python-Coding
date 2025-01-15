import tkinter as tk

def center_window(window, width, height):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    print(screen_height,screen_width)
    
    # Calculate position x and y
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the geometry of the window
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create the main window
root = tk.Tk()

# Define the dimensions of the window
window_width = 1200
window_height = 550

# Center the window on the screen
center_window(root, window_width, window_height)

root.title("Centered Tkinter Window")
root.mainloop()
