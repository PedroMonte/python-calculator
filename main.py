from tkinter import *
from math import sqrt

class Calculator():
    def __init__(self, toplevel):
        toplevel.title('Calculator')

        self.frame_exp = Frame(toplevel, pady=20)
        self.frame_exp.pack()

        self.frame_but = Frame(toplevel, padx=10, pady=10)
        self.frame_but.pack()

        self.expression = ''
        self.equation = StringVar(self.frame_exp)

        Entry(self.frame_exp, width = 35, textvariable=self.equation).pack()

        self.exit = Button(toplevel, text='Exit', width=6, height=3, command=quit, background='red')
        self.exit.pack(side=BOTTOM)

        self.frame_but.columnconfigure(0, weight=1)
        self.frame_but.columnconfigure(1, weight=1)
        self.frame_but.columnconfigure(2, weight=1)


        Button(self.frame_but, height=5, width=7, text='1', command= lambda: self.action('1')).grid(row=0, column=0)
        Button(self.frame_but, height=5, width=7, text='2', command= lambda: self.action('2')).grid(row=0, column=1)
        Button(self.frame_but, height=5, width=7, text='3', command= lambda: self.action('3')).grid(row=0, column=2)
        Button(self.frame_but, height=5, width=7, text='4', command= lambda: self.action('4')).grid(row=0, column=3)
        Button(self.frame_but, height=5, width=7, text='5', command= lambda: self.action('5')).grid(row=1, column=0)
        Button(self.frame_but, height=5, width=7, text='6', command= lambda: self.action('6')).grid(row=1, column=1)
        Button(self.frame_but, height=5, width=7, text='7', command= lambda: self.action('7')).grid(row=1, column=2)
        Button(self.frame_but, height=5, width=7, text='8', command= lambda: self.action('8')).grid(row=1, column=3)
        Button(self.frame_but, height=5, width=7, text='9', command= lambda: self.action('9')).grid(row=2, column=0)
        Button(self.frame_but, height=5, width=7, text='0', command= lambda: self.action('0')).grid(row=2, column=1)

        Button(self.frame_but, height=5, width=7, text='+', command= lambda: self.action('+')).grid(row=2, column=2)
        Button(self.frame_but, height=5, width=7, text='-', command= lambda: self.action('-')).grid(row=2, column=3)
        Button(self.frame_but, height=5, width=7, text='/', command= lambda: self.action('/')).grid(row=3, column=0)
        Button(self.frame_but, height=5, width=7, text='*', command= lambda: self.action('*')).grid(row=3, column=1)
        Button(self.frame_but, height=5, width=7, text='sqrt', command= lambda: self.action('sqrt(')).grid(row=3, column=2)
        Button(self.frame_but, height=5, width=7, text='^', command= lambda: self.action('**')).grid(row=3, column=3)
        Button(self.frame_but, height=5, width=7, text='(', command= lambda: self.action('(')).grid(row=4, column=0)
        Button(self.frame_but, height=5, width=7, text=')', command= lambda: self.action(')')).grid(row=4, column=1)

        Button(self.frame_but, height=5, width=7, text='C', command=self.clear).grid(row=4, column=2)
        Button(self.frame_but, height=5, width=7, text='=', command=self.solve).grid(row=4, column=3)

    #adding chars to entry
    def action(self, char):
        self.expression += char
        self.equation.set(self.expression)
    #cleaning the entry
    def clear(self):
        self.expression = ''
        self.equation.set(self.expression)
    #solving the expression
    def solve(self):
        result = eval(self.expression)
        self.expression = str(result)
        self.equation.set(self.expression)


        
window = Tk()
c = Calculator(window)
mainloop()

