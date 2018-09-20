import tkinter as tk


class MenuView(tk.Menu):

    def __init__(self, parent, settings=None, callbacks=None, **kwargs):

    #def __init__(self, master=None):
        #super().__init__(master)

        super().__init__(parent, **kwargs)

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
