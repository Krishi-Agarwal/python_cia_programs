from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("Palindrome")
win.geometry("400x400+700+300")
var=StringVar()
def palincheck():
    if(t1.get()==(t1.get()[::-1])):
        messagebox.showinfo("CONGRATS",f"{t1.get()} is palindrome")
        var.set("TRUE")
    else:
        messagebox.showinfo("SORRY",f"{t1.get()} is palindrome")
        var.set("FALSE")
win.resizable(height="False",width="False")
t1=Entry(win,fg="blue",bg="cyan",cursor="heart",relief="raised",justify="center")
b1=Button(win,text="CHECK PALINDROME",anchor="e",command=palincheck)
l1=Label(win,font="Jokerman 20 underline",textvariable=var,justify="right")
t1.pack()
b1.pack()
l1.pack()
win.mainloop()