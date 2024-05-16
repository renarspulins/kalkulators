from tkinter import *
import math


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")


def button_log():
    try:
        num = float(e.get())
        result = math.log10(num)
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")


mansLogs = Tk()
mansLogs.title('Calculator')

e = Entry(mansLogs, width=15, bd=10, font=("Arial Black", 20), justify="right")
e.grid(row=0, column=0, columnspan=4)


btn7 = Button(mansLogs, text='7', padx='40', pady='20', command=lambda: button_click(7))
btn8 = Button(mansLogs, text='8', padx='40', pady='20', command=lambda: button_click(8))
btn9 = Button(mansLogs, text='9', padx='40', pady='20', command=lambda: button_click(9))
btn4 = Button(mansLogs, text='4', padx='40', pady='20', command=lambda: button_click(4))
btn5 = Button(mansLogs, text='5', padx='40', pady='20', command=lambda: button_click(5))
btn6 = Button(mansLogs, text='6', padx='40', pady='20', command=lambda: button_click(6))
btn1 = Button(mansLogs, text='1', padx='40', pady='20', command=lambda: button_click(1))
btn2 = Button(mansLogs, text='2', padx='40', pady='20', command=lambda: button_click(2))
btn3 = Button(mansLogs, text='3', padx='40', pady='20', command=lambda: button_click(3))
btn0 = Button(mansLogs, text='0', padx='40', pady='20', command=lambda: button_click(0))

btn_plus = Button(mansLogs, text='+', padx='40', pady='20', command=lambda: button_click('+'))
btn_minus = Button(mansLogs, text='-', padx='40', pady='20', command=lambda: button_click('-'))
btn_multiply = Button(mansLogs, text='*', padx='40', pady='20', command=lambda: button_click('*'))
btn_divide = Button(mansLogs, text='/', padx='40', pady='20', command=lambda: button_click('/'))

btn_clear = Button(mansLogs, text='C', padx='40', pady='20', command=button_clear)
btn_equal = Button(mansLogs, text='=', padx='40', pady='20', command=button_equal)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn0.grid(row=4, column=0)

btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)

btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)

# Change button colors
buttons = [btn7, btn8, btn9, btn4, btn5, btn6, btn1, btn2, btn3, btn0, btn_plus, btn_minus, btn_multiply, btn_divide, btn_clear, btn_equal]
for btn in buttons:
    btn.configure(bg="lightgray")

mansLogs.mainloop()
