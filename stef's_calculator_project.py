# Tkinter used for the GUI
from tkinter import *

# AST used to perform calculations
import ast

# Calculator window
root = Tk()
root.title("Calculator App")

# User display
display = Entry(root)
display.grid(row=1, columnspan=6, sticky="ew")

# Function to input the numbers into the user display
i = 0


def get_number(num):
    global i
    display.insert(i, num)
    i += 1


# Function to input the operations into the user display
def get_operation(operator):
    global i
    length = len(operations)
    display.insert(i, operator)
    i += length


# Function to clear all the user input (all clear)
def all_clear():
    display.delete(0, END)


# Function to carry out mathematical calculation
def calculate():
    try:
        entire_string = display.get()
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, "<string>", "eval"))
        all_clear()
        display.insert(0, result)
    except Exception:
        all_clear()
        display.insert(0, "Calculation error!")


# Function to delete the last character of user input
def delete():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        all_clear()
        display.insert(0, new_string)
    else:
        all_clear()
        display.insert(0, "")


# Number buttons from 0-9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=2, height=2, command=lambda text=button_text: get_number(text))
        button.grid(row=x + 2, column=y)
        counter += 1
button = Button(root, text="0", width=2, height=2, command=lambda: get_number(0))
button.grid(row=5, column=1)


# Operator buttons (add, subtract, multiply, divide, pi, percentage, brackets, exponent, square)
count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", ")", "**", "**2"]
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=2, height=2, command=lambda text=operations[count]: get_operation(text))
            count += 1
            button.grid(row=x + 2, column=y+3)

# All clear (AC) button
Button(root, text="AC", width=2, height=2, command=all_clear).grid(row=5, column=0)

# Delete button (del)
Button(root, text="del", width=2, height=2, command=delete). grid(row=5, column=2)

# Equals button (=)
Button(root, text="=", width=8, height=2, command=calculate).grid(row=5, column=4, columnspan=2)

# Adding my stamp to the project
label_frame = Frame(root, relief=RAISED, borderwidth=2)
label_frame.grid(row=6, column=0, columnspan=6, sticky="ew")
label = Label(label_frame, text="Stef's basic calculator Python project ©")
label.pack()

root.mainloop()
