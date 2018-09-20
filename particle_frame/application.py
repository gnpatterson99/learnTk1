import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter.filedialog import askdirectory, asksaveasfilename
from threading import Thread, Timer

from . import views as v
from . import models as m
from . import menu as mm



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

        self.filename=tk.StringVar()
        self.path = tk.StringVar()

        my_callbacks= { 'Open...': self.on_file_open,
                        'Default Path...': self.on_specify_path,
                        'Save': self.on_save,
                        'Save As...': self.on_save_as,
                        }



        self.menubar=mm.MenuView(self,callbacks=my_callbacks)
        self.config(menu=self.menubar)

        self.recordform = v.DataRecordForm(self, m.CSVModel.fields)
        self.recordform.grid(row=1, padx=10, sticky="W")

        self.plotform=v.PlotForm(self)
        self.plotform.grid(row=2, padx=10)
        #self.plotform.plotIt()



        # guess i could put all of these into another frame...
        #self.savebutton = ttk.Button(self, text="Save", command=self.on_save)
        #self.savebutton.grid(sticky="w", row=3, padx=10)

        #self.exitbutton = ttk.Button(self, text="Exit", command=self.on_exit)
        #self.exitbutton.grid(sticky="e", row=3, padx=10)
        myButtonDict = {
            'Create': self.on_create_particle,
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


        self.my_particle_bag=m.ParticleBag()


    def on_save_as(self):
        # first we need to ask which file to use...
        pass



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

    def on_save_as(self):
        # This seems to save the default path if set using related tk file functions.

        tmpfilename = asksaveasfilename(
            title='Select the target file for saving data',
            defaultextension='.csv',
            filetypes=[('Comma-Separated Values', '*.csv *.CSV')])

        print("Chose filename", tmpfilename)
        self.status.set(tmpfilename)


    def on_exit(self):
        self.destroy()
        #datestring = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
        #self.status.set("Exit button called at {}".format(datestring))

    def on_test(self):
        #print("about to start thread...")
        #thread = Thread(target=self._on_test())
        #thread.start()
        #print("done starting thread...")
        next_collision_time=self.my_particle_bag.time_to_wall_collision_list()
        for i in next_collision_time:
            print(i)

        self.my_particle_bag.updateAllParticles(1.0)
        self.plotform.plotAllParticles(self.my_particle_bag)
        #Timer(0.25, self.on_test).start()

    def _on_test(self):
        self.my_particle_bag.updateAllParticles(1.0)
        self.plotform.plotAllParticles(self.my_particle_bag)
        print("loop")

    def on_specify_path(self):
        tmpdirname = askdirectory(
            title='Select the target file for saving records',
            initialdir="/Users/george",
            parent=self
        )
        print("Chose tmpdirname of",tmpdirname)
        self.path.set(tmpdirname)
        self.status.set(tmpdirname)

    def on_file_open(self):
        pass


    def on_create_particle(self):
        errors = self.recordform.get_errors()
        if errors:
            self.status.set(
                "Cannot save, error in fields: {}"
                    .format(', '.join(errors.keys()))
            )
            return False

        # For now, we save to a hardcoded filename with a datestring.
        datestring = datetime.today().strftime("%Y-%m-%d")
        data = self.recordform.get()
        for k,v in data.items():
            print("Key:",k,"\tValue",v)

        tmp_particle=m.Particle(data['X position'],data['Y position'],data['X velocity'],data['Y velocity'],data['Radius'],'red')

        self.my_particle_bag.add_particle(tmp_particle)
        self.plotform.plotParticle(tmp_particle)

