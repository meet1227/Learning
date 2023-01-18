from tkinter import *
root=Tk()
root.title('Calculator')
global op
op=[]
def answer1():
    p_text=Calc_ent.get()
    op.append(int(p_text))
    t=Ans_ent.get()
    Ans_ent.insert(len(t),' '+p_text+' =')
    print(op)
    while len(op)!=1:
        if 'mod' in op:
            opr=op.index('mod')
            print(opr)
            op1=op[opr-1]
            op2=op[opr+1]
            op.pop(opr-1)
            op.pop(opr-1)
            op.pop(opr-1)
            op.insert(opr-1,op1%op2)
            print(op)
        elif '/' in op:
            opr=op.index('/')
            print(opr)
            op1=op[opr-1]
            op2=op[opr+1]
            op.pop(opr-1)
            op.pop(opr-1)
            op.pop(opr-1)
            op.insert(opr-1,op1/op2)
            print(op)
        elif '*' in op:
            opr=op.index('*')
            print(opr)
            op1=op[opr-1]
            op2=op[opr+1]
            op.pop(opr-1)
            op.pop(opr-1)
            op.pop(opr-1)
            op.insert(opr-1,op1/op2)
            print(op)
        elif '-' in op:
            opr=op.index('-')
            print(opr)
            op1=op[opr-1]
            op2=op[opr+1]
            op.pop(opr-1)
            op.pop(opr-1)
            op.pop(opr-1)
            op.insert(opr-1,op1/op2)
            print(op)
        elif '+' in op:
            opr=op.index('+')
            print(opr)
            op1=op[opr-1]
            op2=op[opr+1]
            op.pop(opr-1)
            op.pop(opr-1)
            op.pop(opr-1)
            op.insert(opr-1,op1/op2)
            print(op)
    Calc_ent.delete(first=0,last=len(p_text))
    t=Ans_ent.get()
    Ans_ent.insert(len(t),op[0])

def clear():
    Ans_ent.delete(0,len(Ans_ent.get()))
    op.clear()


Ans_ent=Entry(root,background='white',fg='black',width=49)
Calc_ent=Entry(root,background='white',fg='black',width=49)
btn1=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="1",padx=43,pady=20,command=lambda :number(1))
btn2=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="2",padx=40,pady=20,command=lambda :number(2))
btn3=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="3",padx=40,pady=20,command=lambda :number(3))
btn4=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="4",padx=43,pady=20,command=lambda :number(4))
btn5=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="5",padx=40,pady=20,command=lambda :number(5))
btn6=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="6",padx=40,pady=20,command=lambda :number(6))
btn7=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="7",padx=43,pady=20,command=lambda :number(7))
btn8=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="8",padx=40,pady=20,command=lambda :number(8))
btn9=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="9",padx=40,pady=20,command=lambda :number(9))
btn0=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="0",padx=43,pady=20,command=lambda :number(0))
Add_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="+",padx=39,pady=20,command=lambda :calculate('+'))
Mod_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="Mod",padx=30,pady=20,command=lambda :calculate('mod'))
Sub_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="-",padx=40,pady=20,command=lambda :calculate('-'))
Mul_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="*",padx=40,pady=20,command=lambda :calculate('*'))
Div_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="/",padx=40,pady=20,command=lambda :calculate('/'))
Clear_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='red',borderwidth=3,text="Clr",padx=38,pady=20,command=clear)
S_per_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text="(",padx=42,pady=20)
C_per_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='white',borderwidth=3,text=")",padx=42,pady=20)
Equ_btn=Button(root,activebackground='yellow',activeforeground='blue',fg='black',background='green',borderwidth=3,text="=",padx=37,pady=50,command=answer1)


Ans_ent.grid(row=0,column=0,rowspan=3,columnspan=4,padx=10,pady=10)
Calc_ent.grid(row=3,column=0,rowspan=2,columnspan=4,padx=10,pady=10)

Clear_btn.grid(row=5,column=0)
S_per_btn.grid(row=5,column=1)
C_per_btn.grid(row=5,column=2)
Div_btn.grid(row=5,column=3)

btn7.grid(row=6,column=0)
btn8.grid(row=6,column=1)
btn9.grid(row=6,column=2)
Mul_btn.grid(row=6,column=3)

btn4.grid(row=7,column=0)
btn5.grid(row=7,column=1)
btn6.grid(row=7,column=2)
Sub_btn.grid(row=7,column=3)

btn1.grid(row=8,column=0)
btn2.grid(row=8,column=1)
btn3.grid(row=8,column=2)
Equ_btn.grid(row=8,column=3,rowspan=2)

Add_btn.grid(row=9,column=2)
Mod_btn.grid(row=9,column=1)
btn0.grid(row=9,column=0)

def number(n):
    
    p_text=Calc_ent.get()
    Calc_ent.delete(first=0,last=len(p_text))
    Calc_ent.insert(0,p_text+str(n))

def calculate(o):
    global op
    p_text=Calc_ent.get()
    t=Ans_ent.get()
    Ans_ent.insert(len(t),' '+p_text+' '+o)
    op.append(int(p_text))
    op.append(o)
    Calc_ent.delete(first=0,last=len(p_text))
        


root.mainloop()