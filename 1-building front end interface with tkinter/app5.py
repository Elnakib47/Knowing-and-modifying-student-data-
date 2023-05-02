from tkinter import *
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

list1.configure(yscrollcommand=sc.set)#new list box=list1 will move verticaly (y)with respect to the value of sc.set
sc.configure(command=list1.yview)#new  scrollbar =sc will move with respect to the value of list box



wind.mainloop()

