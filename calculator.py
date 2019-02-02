
from tkinter import*
from math import*
calculator = Tk()
calculator.resizable(0,0)
calculator.title("Calculator")
calculator.geometry("250x300")





def button_click(num):
    global equation
    equation += str(num)
    input_eq.set(equation)
def clear_click():
    global equation
    equation = ""
    input_eq.set(equation)
def equal_click():
    try:
        global equation

        if "SIN" in equation:
            equation = equation.replace('SIN', "")

            result = str(sin(eval(equation)))

            input_eq.set(result)
            equation = ""
        elif "COS" in equation:
            equation = equation.replace('COS', "")
            result = str(cos(eval(equation)))

            input_eq.set(result)
            equation = ""
        elif "TAN" in equation:
            equation = equation.replace('TAN', "")
            result = str(tan(eval(equation)))

            input_eq.set(result)
            equation = ""
        elif "SQRT" in equation:
            equation = equation.replace('SQRT', "")
            result = str(sqrt(eval(equation)))

            input_eq.set(result)
            equation = ""
        else:
            result = str(eval(equation))
            input_eq.set(result)
            equation = ""
    except:
        input_eq.set("Invalid Input")
        equation = ""

input_eq = StringVar()
entry_1 = Entry(calculator,textvariable = input_eq,width = 58, justify = RIGHT).pack(ipady=15)




equation = ""
button_1 = Button(calculator,text="1",width=6,height=3,command = lambda: button_click(1),bg="black",fg="white").place(x=0,y=50)
button_2 = Button(calculator,text="2",width=6,height=3,command = lambda:  button_click(2),bg="black",fg="white").place(x=50,y=50)
button_3 = Button(calculator,text="3",width=6,height=3,command = lambda:  button_click(3),bg="black",fg="white").place(x=100,y=50)
button_4 = Button(calculator,text="4",width=6,height=3,command = lambda:  button_click(4),bg="black",fg="white").place(x=0,y=100)
button_5 = Button(calculator,text="5",width=6,height=3,command = lambda:  button_click(5),bg="black",fg="white").place(x=50,y=100)
button_6 = Button(calculator,text="6",width=6,height=3,command = lambda:  button_click(6),bg="black",fg="white").place(x=100,y=100)
button_7 = Button(calculator,text="7",width=6,height=3,command = lambda:  button_click(7),bg="black",fg="white").place(x=0,y=150)
button_8 = Button(calculator,text="8",width=6,height=3,command = lambda:  button_click(8),bg="black",fg="white").place(x=50,y=150)
button_9 = Button(calculator,text="9",width=6,height=3,command = lambda:  button_click(9),bg="black",fg="white").place(x=100,y=150)
button_0 = Button(calculator,text="0",width=6,height=3,command = lambda:  button_click(0),bg="black",fg="white").place(x=50,y=200)

button_dot = Button(calculator,text=".",width=6,height=3,command =  lambda: button_click("."),bg="red",fg="white").place(x=100,y=200)
button_add = Button(calculator,text="+",width=6,height=3,command =  lambda: button_click("+"),bg="red",fg="white").place(x=150,y=50)
button_sub = Button(calculator,text="-",width=6,height=3,command =  lambda: button_click("-"),bg="red",fg="white").place(x=150,y=100)
button_mul = Button(calculator,text="*",width=6,height=3,command =  lambda: button_click("*"),bg="red",fg="white").place(x=150,y=150)
button_div = Button(calculator,text="/",width=6,height=3,command =  lambda: button_click("/"),bg="red",fg="white").place(x=150,y=200)
button_cl = Button(calculator,text="C",width=6,height=3,command =  lambda: clear_click(),bg="red",fg="white").place(x=0,y=200)
button_eq = Button(calculator,text="=",width=35,height=3,command =  lambda: equal_click(),bg="green",fg="black").place(x=0,y=255)

button_sin = Button(calculator,text="SIN",width=6,height=3,command =  lambda: button_click("SIN"),bg="red",fg="white").place(x=200,y=50)
button_cos = Button(calculator,text="COS",width=6,height=3,command =  lambda: button_click("COS"),bg="red",fg="white").place(x=200,y=100)
button_tan = Button(calculator,text="TAN",width=6,height=3,command =  lambda: button_click("TAN"),bg="red",fg="white").place(x=200,y=150)
button_sqrt = Button(calculator,text="SQRT",width=6,height=3,command =  lambda: button_click("SQRT"),bg="red",fg="white").place(x=200,y=200)


calculator.mainloop()