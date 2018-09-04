import tkinter as tk


class MenuView(tk.Menu):

    def __init__(self, parent, settings=None, callbacks=None, **kwargs):

    #def __init__(self, master=None):
        #super().__init__(master)

        super().__init__(parent, **kwargs)
        # text_menu = tk.Menu(self, tearoff=False)
        # self.add_cascade(label='TTTMenuView', menu=text_menu)
        #
        # text_menu.add_command(label='Set to "Hi"',
        #                       command=lambda: print('Hi'))
        # text_menu.add_command(label='Set to "There"',
         #                     command=lambda: print('There'))

        #self.config(menu=self)

        # text_menu2 = tk.Menu(self, tearoff=False)
        # self.add_cascade(label='TTTMenuView2', menu=text_menu2)
        # text_menu2.add_command(label='Set to "Hi"',
        #                       command=lambda: print('Hi'))
        # text_menu2.add_command(label='Set to "There"',
        #                      command=lambda: print('There'))

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File...', menu=file_menu)

        for (k,v) in callbacks.items():
            file_menu.add_command(
                label=k,
                command=v)

        if settings != None:
            settings_menu = tk.Menu(self, tearoff=False)
            self.add_cascade(label='Settings...', menu=settings_menu)

            for (k,v) in settings.items():
                file_menu.add_command(
                    label=k,
                    command=v)

        font_size = tk.IntVar()
        size_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='Font size', menu=size_menu)
        for size in range(8, 24, 2):
            size_menu.add_radiobutton(label="{} px".format(size),
                              value=size, variable=font_size)
