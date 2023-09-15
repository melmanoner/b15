from tkinter import *
import itertools
import re

class Main(Frame):

    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        btns = [
            "C", "(", ")", "≡",
            "x1", "x2", "x3", "∧",
            "x4", "x5", "x6", "∨",
            "x7", "x8", "x9", "¬",
            "x10", "x11", "x12","=(0)","x13", "x14","x15", "=(1)"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#fff",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 10, "bold"),
                         bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)


    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation =="¬":
            if self.formula == "0":
                self.formula = ""
                self.formula += " not "
            else:
                self.formula += " not "
        elif operation =="∨":
            self.formula += " or "
        elif operation =="∧":
            self.formula += " and "
        elif operation =="≡":
            self.formula += " == "
        elif operation == "=(1)":
            self.res1()
        elif operation == "=(0)":
            self.res0()
        elif operation =="!":
            self.formula += " not "
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def res1(self):
        c=0

        x1 = [0, 1]
        x2 = [0, 1]
        x3 = [0, 1]
        x4 = [0, 1]
        x5 = [0, 1]
        x6 = [0, 1]
        x7 = [0, 1]
        x8 = [0, 1]
        x9 = [0, 1]
        x10 = [0, 1]
        x11 = [0, 1]
        x12 = [0, 1]
        x13 = [0, 1]
        x14 = [0, 1]
        x15 = [0,1]
        if re.search(r'\bx15\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14,x15 in itertools.product(x1, x2, x3, x4, x5, x6,
                                                                                                 x7, x8, x9, x10, x11,
                                                                                                 x12, x13, x14,x15):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx14\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 in itertools.product(x1, x2, x3, x4, x5, x6,
                                                                                                 x7, x8, x9, x10, x11,
                                                                                                 x12, x13, x14):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx13\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13 in itertools.product(x1, x2, x3, x4, x5, x6, x7,
                                                                                            x8, x9, x10, x11, x12, x13):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx12\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8,
                                                                                       x9, x10, x11, x12):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx11\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9,
                                                                                  x10, x11):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx10\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx9\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9 in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx8\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8 in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx7\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7 in itertools.product(x1, x2, x3, x4, x5, x6, x7):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx6\b', self.formula):
            for x1, x2, x3, x4, x5, x6 in itertools.product(x1, x2, x3, x4, x5, x6):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx5\b', self.formula):
            for x1, x2, x3, x4, x5 in itertools.product(x1, x2, x3, x4, x5):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx4\b', self.formula):
            for x1, x2, x3, x4 in itertools.product(x1, x2, x3, x4):
                x = eval(self.formula)
                if x == 0:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx3\b', self.formula):
            for x1, x2, x3 in itertools.product(x1, x2, x3):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c
        else:
            for x1, x2 in itertools.product(x1, x2):
                x = eval(self.formula)
                if x == 1:
                    c = c + 1
            self.formula = c






    def res0(self):
        c = 0

        x1 = [0, 1]
        x2 = [0, 1]
        x3 = [0, 1]
        x4 = [0, 1]
        x5 = [0, 1]
        x6 = [0, 1]
        x7 = [0, 1]
        x8 = [0, 1]
        x9 = [0, 1]
        x10 = [0, 1]
        x11 = [0,1]
        x12 = [0,1]
        x13 = [0,1]
        x14 = [0,1]
        x15 = [0,1]
        if re.search(r'\bx15\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 in itertools.product(x1, x2, x3, x4,
                                                                                                      x5, x6,
                                                                                                      x7, x8, x9, x10,
                                                                                                      x11,
                                                                                                      x12, x13, x14,
                                                                                                      x15):
                x = eval(self.formula)
                if x == 0:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx14\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 in itertools.product(x1, x2, x3, x4, x5, x6,
                                                                                                 x7, x8, x9, x10, x11,
                                                                                                 x12, x13, x14):
                x = eval(self.formula)
                if x == 0:
                    c = c + 1
            self.formula = c
        elif re.search(r'\bx12\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11,x12  in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11,x12):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx11\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11  in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx10\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9, x10  in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx9\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8, x9  in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8, x9):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx8\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7, x8  in itertools.product(x1, x2, x3, x4, x5, x6, x7, x8):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx7\b', self.formula):
            for x1, x2, x3, x4, x5, x6, x7  in itertools.product(x1, x2, x3, x4, x5, x6, x7):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx6\b', self.formula):
            for x1, x2, x3, x4, x5, x6  in itertools.product(x1, x2, x3, x4, x5, x6):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx5\b', self.formula):
            for x1, x2, x3, x4, x5  in itertools.product(x1, x2, x3, x4, x5):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx4\b', self.formula):
            for x1, x2, x3, x4 in itertools.product(x1, x2, x3, x4):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        elif re.search(r'\bx3\b', self.formula):
            for x1, x2, x3 in itertools.product(x1, x2, x3):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c
        else:
            for x1, x2 in itertools.product(x1, x2):
                x = eval(self.formula)
                if x == 0:
                    c=c+1
            self.formula = c



    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)






if __name__=='__main__':
    root = Tk()
    root['bg']='#000'
    root.title(u'Калькулятор логических приложений')
    root.geometry('485x650+200+200')
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()
