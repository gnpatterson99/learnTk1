import tkinter as tk
from tkinter import ttk
from datetime import datetime
from . import views as v
from . import models as m
#from . import menu as mm


class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Particle Viz Framework")
        self.resizable() #width=False, height=False)

        ttk.Label(
            self,
            text="ABQ Data Entry Application",
            font=("TkDefaultFont", 16)
        ).grid(row=0)



        self.menubar = tk.Menu(self)
        #main_menu=tk.Menu(self.menubar, tearoff=False)

        text_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='TTT', menu=text_menu)

        text_menu.add_command(label='Set to "Hi"',
                              command=lambda: print('Hi'))
        text_menu.add_command(label='Set to "There"',
                              command=lambda: print('There'))

        self.config(menu=self.menubar)

        #text_menu2 = tk.Menu(main_menu, tearoff=False)
        #text_menu2.add_command(label='Set to "Hi"',
        #                      command=lambda: print('Hi'))
        #text_menu2.add_command(label='Set to "There"',
        #                      command=lambda: print('There'))

        #main_menu.add_cascade(label="Text", menu=text_menu)
        #main_menu.add_cascade(label="Text3", menu=text_menu2)

        #self.config(menu=self.main_menu)

        #self.main_menu = mm.MenuClass(self)

        self.recordform = v.DataRecordForm(self, m.CSVModel.fields)
        self.recordform.grid(row=1, padx=10, sticky="W")

        self.plotform=v.PlotForm(self)
        self.plotform.grid(row=2, padx=10)
        self.plotform.plotIt()



        # guess i could put all of these into another frame...
        #self.savebutton = ttk.Button(self, text="Save", command=self.on_save)
        #self.savebutton.grid(sticky="w", row=3, padx=10)

        #self.exitbutton = ttk.Button(self, text="Exit", command=self.on_exit)
        #self.exitbutton.grid(sticky="e", row=3, padx=10)
        myButtonDict = {
            'Save': self.on_save,
            'Exit': self.on_exit,
            'Test': self.on_test,
        }

        self.buttonform=v.ButtonForm(self, myButtonDict)
        self.buttonform.grid(row=3,column=0, sticky='w')
 #       self.buttonform.set_save(self.on_exit)

        # status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky="we", row=4, padx=10)

        self.records_saved = 0

    def on_save(self):
        """Handles save button clicks"""

        # Check for errors first

        errors = self.recordform.get_errors()
        if errors:
            self.status.set(
                "Cannot save, error in fields: {}"
                .format(', '.join(errors.keys()))
            )
            return False

        # For now, we save to a hardcoded filename with a datestring.
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "abq_data_record_{}.csv".format(datestring)
        model = m.CSVModel(filename)
        data = self.recordform.get()
        model.save_record(data)
        self.records_saved += 1
        self.status.set(
            "{} records saved this session".format(self.records_saved)
        )
        self.recordform.reset()

    def on_exit(self):
        self.destroy()
        #datestring = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
        #self.status.set("Exit button called at {}".format(datestring))

    def on_test(self):
        self.plotform.plotIt()
