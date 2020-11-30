from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class calcWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Calculator")
        self.geometry("500x300")
        self.resizable(0, 0)
        self.style = Style()

        self.style.configure('Header.TFrame', background = '#2C3C53')
        self.header_frame = Frame(self, style = 'Header.TFrame')
        self.header_frame.pack(fill = X)

        self.style.configure('Header.TLabel', background = '#2C3C53', foreground ='white', font = (None, 30))
        self.header_label = Label(self.header_frame, text = "Calculator", style = "Header.TLabel")
        self.header_label.pack()

        self.style.configure('Login.TFrame')
        self.login_frame = Frame(self, style = 'Login.TFrame')
        self.login_frame.pack(fill = BOTH, expand = True)

        self.style.configure('Content.TFrame')
        self.content_frame = Frame(self.login_frame, style = 'Content.TFrame')
        self.content_frame.place(relx = 0.5, rely =0.5, anchor = CENTER)

        self.style.configure('Content.TLabel')

        self.calculation = Entry(self.content_frame, width = 40)
        self.calculation.grid(row = 0, column = 0, pady=10, columnspan = 4)
        self.calculation.focus()

        def add_click():
            first_number = self.calculation.get()
            global f_num
            f_num = int(first_number)
            global math
            math = 'addition'

            self.calculation.delete(0, END)

        def sub_click():
            first_number = self.calculation.get()
            global f_num
            f_num = int(first_number)
            global math
            math = 'subtraction'

            self.calculation.delete(0, END)

        def mult_click():
            first_number = self.calculation.get()
            global f_num
            f_num = int(first_number)
            global math
            math = 'multiplication'

            self.calculation.delete(0, END)

        def divide_click():
            first_number = self.calculation.get()
            global f_num
            f_num = int(first_number)
            global math
            math = 'division'

            self.calculation.delete(0, END)

        def equal_click():
            second_number = self.calculation.get()
            self.calculation.delete(0, END)

            if math=='addition':
                self.calculation.insert(0, f_num + int(second_number))
            if math=='subtraction':
                self.calculation.insert(0, f_num - int(second_number))
            if math=='multiplication':
                self.calculation.insert(0, f_num * int(second_number))
            if math=='division':
                self.calculation.insert(0, f_num / int(second_number))

        def clear_click():
            self.calculation.delete(0, END)

        def number_click(number):
            current = self.calculation.get()
            self.calculation.delete(0, END)
            self.calculation.insert(0, str(current) + str(number))

        self.button_0 = Button(self.content_frame,text = "0", command = lambda: number_click(0))
        self.button_0.grid(row = 4, column = 1, columnspan = 1)

        self.button_1 = Button(self.content_frame,text = "1", command = lambda: number_click(1))
        self.button_1.grid(row = 3, column = 0, columnspan = 1)

        self.button_2 = Button(self.content_frame,text = "2", command = lambda: number_click(2))
        self.button_2.grid(row = 3, column = 1, columnspan = 1)

        self.button_3 = Button(self.content_frame,text = "3", command = lambda: number_click(3))
        self.button_3.grid(row = 3, column = 2, columnspan = 1)

        self.button_4 = Button(self.content_frame,text = "4", command = lambda: number_click(4))
        self.button_4.grid(row = 2, column = 0, columnspan = 1)

        self.button_5 = Button(self.content_frame,text = "5", command = lambda: number_click(5))
        self.button_5.grid(row = 2, column = 1, columnspan = 1)

        self.button_6 = Button(self.content_frame,text = "6", command = lambda: number_click(6))
        self.button_6.grid(row = 2, column = 2, columnspan = 1)

        self.button_7 = Button(self.content_frame,text = "7", command = lambda: number_click(7))
        self.button_7.grid(row = 1, column = 0, columnspan = 1)

        self.button_8 = Button(self.content_frame,text = "8", command = lambda: number_click(8))
        self.button_8.grid(row = 1, column = 1, columnspan = 1)

        self.button_9 = Button(self.content_frame,text = "9", command = lambda: number_click(9))
        self.button_9.grid(row = 1, column = 2, columnspan = 1)


        self.add_button = Button(self.content_frame,text = "+", command = add_click)
        self.add_button.grid(row = 1, column = 3, columnspan = 1)

        self.add_button = Button(self.content_frame,text = "-", command = sub_click)
        self.add_button.grid(row = 2, column = 3, columnspan = 1)

        self.add_button = Button(self.content_frame,text = "*", command = mult_click)
        self.add_button.grid(row = 3, column = 3, columnspan = 1)

        self.add_button = Button(self.content_frame,text = "/", command = divide_click)
        self.add_button.grid(row = 4, column = 3, columnspan = 1)

        self.equal_button = Button(self.content_frame,text = "=", command = equal_click)
        self.equal_button.grid(row = 4, column = 2, columnspan = 1)

        self.clear_button = Button(self.content_frame,text = "Clear", command = clear_click)
        self.clear_button.grid(row = 4, column = 0, columnspan = 1)



if __name__ == "__main__":
    lw = calcWindow()
    lw.mainloop()
