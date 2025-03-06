import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def openTaskFile():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            
        for task in tasks:
            if task.strip():
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        open("tasklist.txt", "w").close()  # Create the file if it doesn't exist

def addTask():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_list.append(task)
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(task + "\n")
        task_entry.delete(0, END)

def deleteTask():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        del task_list[selected_task]
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
    except IndexError:
        pass  # Do nothing if no task is selected

# Load Icon
Image_icon = PhotoImage(file="image/task.png")
root.iconphoto(False, Image_icon)

# Top bar
TopImage = PhotoImage(file="image/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="image/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=30, y=25)

heading = Label(root, text="All Tasks", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Main Entry Frame
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

add_button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
add_button.place(x=300, y=0)

# Listbox Frame
frame1 = Frame(root, bd=3, width=400, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

# Scrollbar for Listbox
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", 
                  selectbackground="#5a95ff", yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar.config(command=listbox.yview)

# Load tasks from file
openTaskFile()

# Delete Button
Delete_icon = PhotoImage(file="image/delete.png")
delete_button = Button(root, image=Delete_icon, bd=0, command=deleteTask)
delete_button.pack(side=BOTTOM, pady=13)

root.mainloop()
