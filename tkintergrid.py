
import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.config(bg='red')
def clicked():
    messagebox.showinfo("MESSAGE BOX","BOTTON WAS CLICKED")
b1=tkinter.Button(root,text="click me",activebackground="cyan",activeforeground="red",bd=5,bg="yellow",fg="black",command=clicked,justify="left",width=50)
b2=tkinter.Button(root,text="Clear",command=clicked,font="jockerman",height=20,justify="right",underline=-1)
l1=tkinter.Label(root,text="ENTER THE NAME")
l2=tkinter.Label(root,text="ENTER THE NUMBER")
t1=tkinter.Entry(root)
t2=tkinter.Entry(root)
l1.grid(row=0,column=0,padx=10)
t1.grid(row=0,column=1,pady=10)
l2.grid(row=1,column=0,ipadx=5)
t2.grid(row=1,column=1,ipady=5)
b1.grid(row=2,column=0,columnspan=2)
b2.grid(row=2,column=2,rowspan=2,sticky="se")
root.mainloop()
