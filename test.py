import tkinter as tk
from tkinter import PhotoImage, Label

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []  # Empty task list

# Icon
try:
    image_icon = PhotoImage(file="image/task.png")
    root.iconphoto(False, image_icon)
except:
    print("Error: task.png not found!")

# Top Bar
try:
    top_image = PhotoImage(file="image/topbar.png")
    Label(root, image=top_image).pack()
except:
    print("Error: topbar.png not found!")

# Dock Image
try:
    dock_image = PhotoImage(file="image/dock.png")
    Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)
except:
    print("Error: dock.png not found!")

# Note Image
try:
    note_image = PhotoImage(file="image/task.png")
    Label(root, image=note_image, bg="#32405b").place(x=60, y=25)  # Adjusted position to prevent overlap
except:
    print("Error: task.png not found!")

# Heading
heading = Label(root, text="All Tasks", font="Arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Run Tkinter main loop
root.mainloop()
