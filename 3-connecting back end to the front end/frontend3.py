#b3 add new & insert
from tkinter import *
import backend


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(fn.get(),ln.get(),term.get(),gpa.get()):
        list1.insert(END,row)


def add_command():#next
    backend.insert(fn.get(),ln.get(),term.get(),gpa.get())
    list1.delete(0,END)
    #list1.insert(END,(fn.get(),ln.get(),term.get(),gpa.get()))
    list1.insert(END,"name added")

        
wind=Tk()
l1=Label(wind,text="First name")
l1.grid(row=0)
l2=Label(wind,text="Last name")
l2.grid(row=0,column=2)
l3=Label(wind,text="Term")
l3.grid(row=1)
l4=Label(wind,text="GPA")
l4.grid(row=1,column=2)


fn=StringVar()
e1=Entry(wind,textvariable=fn)
e1.grid(row=0,column=1)
ln=StringVar()
e2=Entry(wind,textvariable=ln)
e2.grid(row=0,column=3)
term=StringVar()
e3=Entry(wind,textvariable=term)
e3.grid(row=1,column=1)
gpa=StringVar()
e4=Entry(wind,textvariable=gpa)
e4.grid(row=1,column=3)


list1=Listbox(wind,height=6,width=35)
#list1.grid(row=2)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sc=Scrollbar(wind)
sc.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sc.set)
sc.configure(command=list1.yview)


b1=Button(wind,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)


b2=Button(wind,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(wind,text="Add new",width=12,command=add_command)#start from here
b3.grid(row=4,column=3)


b4=Button(wind,text="Update",width=12)
b4.grid(row=5,column=3)

b5=Button(wind,text="Delete",width=12)
b5.grid(row=6,column=3)

b6=Button(wind,text="Exit",width=12)
b6.grid(row=7,column=3)



wind.mainloop()

