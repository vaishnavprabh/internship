from tkinter import *

# root=Tk()
# root.title("java")

# root.geometry('20x10')
# root.mainloop()

# root=Tk()
# root.title("java")
# root.geometry('300x250')
# name="we are java"
# lbl=Label(root,text=name,font=("Roman",12),fg='white',bg='indigo')
# lbl.pack()
# root.mainloop()

# root=Tk()
# root.title("biodata")
# def clicked():
#     print("i am clicked")
# btn=Button(root,text="click me",command=clicked)
# btn.pack()
# root.geometry('400x300')
# name=" my name is Sumaiyah"
# lbl=Label(root,text=name,font=("script",15),fg='white',bg='black')
# lbl.pack()
# root.mainloop()

# root=Tk()
# root.title("welcome to vazhakala")
# entry=Entry(root,bg="blue",fg="red",bd=5)
# entry.place(x=100,y=100)
# root.geometry('250x200')
# root.mainloop()

root=Tk()
root.title("login page")
root.geometry('300x200')
lbl1=Label(root,text="Facebook",font=("Helvetica",12),fg='blue',bg='white')
lbl1.pack()
lbl2=Label(root,text="Login to facebook")
lbl2.pack()
lbl3=Label(root,text="username")
lbl3.pack()
entry1=Entry(root,bg="white",fg="blue",bd=2)
entry1.pack()
lbl4=Label(root,text="password")
lbl4.pack()
entry2=Entry(root,bg="white",fg="blue",bd=2)
entry2.pack()
def clicked():
    print("I am login")
btn=Button(root,text="Login",command="logined",bg="blue",fg="white",bd=2
)
btn.pack()
root.mainloop()