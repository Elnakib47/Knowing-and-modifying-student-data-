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

wind.mainloop()

