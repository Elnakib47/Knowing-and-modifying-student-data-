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

wind.mainloop()

