import tkinter
root=tkinter.Tk()
root.config(bg='red')
b1=tkinter.Button(root,text="click me")
b2=tkinter.Button(root,text="Clear")
l1=tkinter.Label(root,text="ENTER THE NAME")
l2=tkinter.Label(root,text="ENTER THE NUMBER")
t1=tkinter.Entry(root)
t2=tkinter.Entry(root)
l1.place(x=0,y=0,in_=root)
t1.place(x=150,y=0)
l2.place(x=0,y=50)
t2.place(x=150,y=50)
b1.place(x=0,y=100)
b2.place(x=150,y=100,anchor="se")
root.mainloop()
