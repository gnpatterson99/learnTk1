import tkinter as tk
from tkinter import ttk
from datetime import datetime
from . import widgets as w
import random


class DataRecordForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, fields, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets
        self.inputs = {}

        # Build the form
        # recordinfo section
        recordinfo = tk.LabelFrame(self, text="Record Information")

        # line 1
        self.inputs['X position'] = w.LabelInput(
            recordinfo, "Xposition",
            field_spec=fields['Position']
        )
        self.inputs['X position'].grid(row=0, column=0)

        self.inputs['Y position'] = w.LabelInput(
            recordinfo, "Yposition",
            field_spec=fields['Position']
        )
        self.inputs['Y position'].grid(row=0, column=1)

        # line 2
        self.inputs['X velocity'] = w.LabelInput(
            recordinfo, "Xvelocity",
            field_spec=fields['Velocity']
        )
        self.inputs['X velocity'].grid(row=1, column=0)


        self.inputs['Y Velocity'] = w.LabelInput(
            recordinfo, "Yvelocity",
            field_spec=fields['Velocity']
        )
        self.inputs['Y Velocity'].grid(row=1, column=1)

        # next row...

        self.inputs['Radius'] = w.LabelInput(
            recordinfo, "Radius",
            field_spec=fields['Position']
        )
        self.inputs['Radius'].grid(row=1, column=2)

        recordinfo.grid(row=0, column=0, sticky="we")

        self.reset()

    def get(self):
        """Retrieve data from form as a dict"""

        # We need to retrieve the data from Tkinter variables
        # and place it in regular Python objects

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):

        # """Resets the form entries"""
        #
        # # gather the values to keep for each lab
        # lab = self.inputs['Lab'].get()
        # time = self.inputs['Time'].get()
        # technician = self.inputs['Technician'].get()
        # plot = self.inputs['Plot'].get()
        # plot_values = self.inputs['Plot'].input.cget('values')
        #
        # # clear all values
        for widget in self.inputs.values():
             widget.set('')
        #
        current_date = datetime.today().strftime('%Y-%m-%d')
        #self.inputs['Date'].set(current_date)
        #self.inputs['Time'].input.focus()
        #
        # # check if we need to put our values back, then do it.
        # if plot not in ('', plot_values[-1]):
        #     self.inputs['Lab'].set(lab)
        #     self.inputs['Time'].set(time)
        #     self.inputs['Technician'].set(technician)
        #     next_plot_index = plot_values.index(plot) + 1
        #     self.inputs['Plot'].set(plot_values[next_plot_index])
        #     self.inputs['Seed sample'].input.focus()

    def get_errors(self):
        """Get a list of field errors in the form"""

        errors = {}
        for key, widget in self.inputs.items():
            if hasattr(widget.input, 'trigger_focusout_validation'):
                widget.input.trigger_focusout_validation()
            if widget.error.get():
                errors[key] = widget.error.get()

        return errors


class PlotForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent,  *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets
        #self.inputs = {}

        # Build the form
        # recordinfo section
        #plotform = tk.Frame(self)

        self.canvas=tk.Canvas(self, width=800, height=400)
        self.canvas.grid(row=0, column=0)

    def reset(self):
        pass

    def plotIt(self):
        #self.canvas.create_line(0,0,100,100)
        for i in range(20):
            x = random.randint(10, 400)
            y = random.randint(10, 400)
            self.plotPoint(x,y,10)


    def plotPoint(self, xpos, ypos, radius):
        x0=xpos-radius
        y0=ypos-radius

        x1=xpos + radius
        y1=ypos + radius
        self.canvas.create_oval(x0,y0,x1,y1)




class ButtonForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, dictConfig, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets

        self.buttons = {}
        i=0
        for key, value in dictConfig.items():
            self.buttons[key] = ttk.Button(self, text=key, command=value)
            self.buttons[key].grid(sticky="w", row=0, column=i, padx=10)
            i=i+1


    def set_save(self, save_command):
        pass

