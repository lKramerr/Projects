from tkinter import *

root = Tk()
root.title("Calculator")

num = Entry(root, width = '25')
num.grid(row = 0, column = 0, columnspan = 4)

def btn_click(number):
    current = num.get()
    num.delete(0, END)
    num.insert(0, str(current) + str(number))

def btn_clear():
    num.delete(0, END)

def btn_add():
    int_num = num.get()
    global int_num1
    global operation
    operation = "+"
    int_num1 = int(int_num)
    num.delete(0, END)

def btn_subs():
    int_num = num.get()
    global int_num1
    global operation
    operation = "-"
    int_num1 = int(int_num)
    num.delete(0, END)

def btn_mult():
    int_num = num.get()
    global int_num1
    global operation
    operation = "*"
    int_num1 = int(int_num)
    num.delete(0, END)

def btn_div():
    int_num = num.get()
    global int_num1
    global operation
    operation = "/"
    int_num1 = int(int_num)
    num.delete(0, END)

def btn_equal():
    int_num2 = num.get()
    num.delete(0, END)
    if operation == "+":
        num.insert(0, int_num1 + int(int_num2))
    elif operation == "-":
        num.insert(0, int_num1 - int(int_num2))
    elif operation == "*":
        num.insert(0, int_num1 * int(int_num2))
    elif operation == "/":
        num.insert(0, int_num1 / int(int_num2))

#Numbers and extras
btn_seven = Button(root, text = "7", width = 2, command = lambda: btn_click(7))
btn_eight = Button(root, text = "8", width = 2, command = lambda: btn_click(8))
btn_nine = Button(root, text = "9", width = 2, command = lambda: btn_click(9))
btn_four = Button(root, text = "4", width = 2, command = lambda: btn_click(4))
btn_five = Button(root, text = "5", width = 2, command = lambda: btn_click(5))
btn_six = Button(root, text = "6", width = 2, command = lambda: btn_click(6))
btn_one = Button(root, text = "1", width = 2, command = lambda: btn_click(1))
btn_two = Button(root, text = "2", width = 2, command = lambda: btn_click(2))
btn_three = Button(root, text = "3", width = 2, command = lambda: btn_click(3))
btn_zero = Button(root, text = "0", width = 2, command = lambda: btn_click(0))
btn_dot = Button(root, text = ".", width = 2, command = lambda: btn_click("."))
btn_equal = Button(root, text = "=", width = 2, command = btn_equal)
btn_clear = Button(root, text = "Clear", width = 2, height = 7, command = btn_clear)

#Operations
btn_div = Button(root, text = "/", width = 2, command = btn_div)
btn_mult = Button(root, text = "X", width = 2, command = btn_mult)
btn_subs = Button(root, text = "-", width = 2, command = btn_subs)
btn_add = Button(root, text = "+", width = 2, command = btn_add)

btn_seven.grid(row = 1, column = 0)
btn_eight.grid(row = 1, column = 1)
btn_nine.grid(row = 1, column = 2)
btn_four.grid(row = 2, column = 0)
btn_five.grid(row = 2, column = 1)
btn_six.grid(row = 2, column = 2)
btn_one.grid(row = 3, column = 0)
btn_two.grid(row = 3, column = 1)
btn_three.grid(row = 3, column = 2)
btn_zero.grid(row = 4, column = 0)
btn_dot.grid(row = 4, column = 1)
btn_equal.grid(row = 4, column = 2)
btn_clear.grid(row = 1, column = 4, rowspan = 4)

#Operations possition
btn_div.grid(row = 1, column = 3)
btn_mult.grid(row = 2, column = 3)
btn_subs.grid(row = 3, column = 3)
btn_add.grid(row = 4, column = 3)




root.mainloop()
