import tkinter as tk


class MenuView(tk.Menu):

    def __init__(self, master=None):
        super().__init__(master)

        #self.menubar = tk.Menu(self)
        #main_menu=tk.Menu(self.menubar, tearoff=False)

        text_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='TTTMenuView', menu=text_menu)

        text_menu.add_command(label='Set to "Hi"',
                              command=lambda: print('Hi'))
        text_menu.add_command(label='Set to "There"',
                              command=lambda: print('There'))

        #self.config(menu=self)

        text_menu2 = tk.Menu(self, tearoff=False)
        self.add_cascade(label='TTTMenuView2', menu=text_menu2)
        text_menu2.add_command(label='Set to "Hi"',
                              command=lambda: print('Hi'))
        text_menu2.add_command(label='Set to "There"',
                              command=lambda: print('There'))

