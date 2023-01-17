
# 1
from tkinter import *   
top = Tk()
top.geometry("400x400")  
b = Button(top,text = "Simple")  
b.pack()   
top.mainloop()  

# # 2
# from tkinter import *   
# from tkinter import messagebox
# top = Tk()  
# top.geometry("200x100")  
# def fun():  
#     messagebox.showinfo("Hello", "Red Button clicked")   
# b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10,bd=5,font=)   
# b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)  
# b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
# b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
# b1.pack(side = LEFT)  
# b2.pack(side = RIGHT)  
# b3.pack(side = TOP)   
# b4.pack(side = BOTTOM) 
# top.mainloop()  

# # 3
# from tkinter import *   
  
# top = Tk()  
  
# top.geometry("200x200")  
  
# checkvar1 = IntVar()  
  
# checkvar2 = IntVar()  
  
# checkvar3 = IntVar()  
  
# chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
# chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
# chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
# chkbtn1.pack()  
  
# chkbtn2.pack()  
  
# chkbtn3.pack()  
  
# top.mainloop()  