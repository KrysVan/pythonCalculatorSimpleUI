import tkinter
from tkinter import *

root=Tk()                           #this block creates the pop-up window for the calculator
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):   # this function is for all the buttons except the clear one, it displays everything that user puts in
    global equation  # global equation variable allows access to all functions
    equation+=value
    label_result.config(text=equation)
def clear(): # this function is only for the clear button - to clear the visual part, it of course, clears the equation variable so that the eval funciton has nothing to work with ("") - emtpy string
    global equation
    equation =""
    label_result.config(text=equation)
def calculate(): # function that evaluate/calculate and operate with all the integres and the operaters from the UI calculator
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)          # evaluates string inputs and gives back int result/evaluation
        except:
            result ="error"  #in the case that eval() is not possible (multiple special symbols in a row, not a correct equation)
            equation = ""
    label_result.config(text=result)
label_result= Label(root, width=25, height=2, text="", font=("arial", 30))    # this prints/keeps udated the visual component of the calculator
label_result.pack()
#this block creates visually and functionally the buttons for the input variables for the calculator
Button(root,text="C", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0", width=11, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".", width=5, height=1, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=3, font=("arial", 30,"bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430,y=400)


root.mainloop()  #this function keeps the program running until the app is closed