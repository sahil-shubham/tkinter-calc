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

        # self.label_username = Label(self.content_frame, text = "Username: ", style = 'Content.TLabel')
        # self.label_username.grid(row= 0, column = 0)
        #
        # self.label_password = Label(self.content_frame, text = "Password: ")
        # self.label_password.grid(row = 1, column = 0)
        #
        # self.username = Entry(self.content_frame, width = 30)
        # self.username.grid(row = 0, column = 1, pady=10, columnspan = 2)
        # self.username.focus()
        #
        # self.password = Entry(self.content_frame, width = 30, show = "*")
        # self.password.grid(row = 1, column = 1, pady=10, columnspan = 2)

        def add_click():
            return

        def number_click():
            return

        # self.add_button = Button(self.content_frame,text = "+", command = add_click)
        # self.add_button.grid(row = 2, column = 1, columnspan = 1)

        self.button_0 = Button(self.content_frame,text = "0", command = number_click)
        self.button_0.grid(row = 4, column = 0, columnspan = 1)

        self.button_1 = Button(self.content_frame,text = "1", command = number_click)
        self.button_1.grid(row = 3, column = 0, columnspan = 1)

        self.button_2 = Button(self.content_frame,text = "2", command = number_click)
        self.button_2.grid(row = 3, column = 1, columnspan = 1)

        self.button_3 = Button(self.content_frame,text = "3", command = number_click)
        self.button_3.grid(row = 3, column = 2, columnspan = 1)

        self.button_4 = Button(self.content_frame,text = "4", command = number_click)
        self.button_4.grid(row = 2, column = 0, columnspan = 1)

        self.button_5 = Button(self.content_frame,text = "5", command = number_click)
        self.button_5.grid(row = 2, column = 1, columnspan = 1)

        self.button_6 = Button(self.content_frame,text = "6", command = number_click)
        self.button_6.grid(row = 2, column = 2, columnspan = 1)

        self.button_7 = Button(self.content_frame,text = "7", command = number_click)
        self.button_7.grid(row = 1, column = 0, columnspan = 1)

        self.button_8 = Button(self.content_frame,text = "8", command = number_click)
        self.button_8.grid(row = 1, column = 1, columnspan = 1)

        self.button_9 = Button(self.content_frame,text = "9", command = number_click)
        self.button_9.grid(row = 1, column = 2, columnspan = 1)

if __name__ == "__main__":
    lw = calcWindow()
    lw.mainloop()
