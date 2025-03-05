import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)


task_list  = []


#icon
Image_icon = PhotoImage(file="image/task.png")
root.iconphoto(False,Image_icon)

#top bar

TopImage = PhotoImage(file="image/topbar.png")
Label(root,image=TopImage).pack()

dockImage = PhotoImage(file="image/dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)


noteImage = PhotoImage(file="image/task.png")
Label(root,image=noteImage, bg="#32405b").place(x=30,y=25)

heading = Label(root, text="All Tasks", font="Arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130,y=20)



#main






root.mainloop()
 


