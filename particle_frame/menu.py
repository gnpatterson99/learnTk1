import tkinter as tk
from tkinter import ttk
from datetime import datetime
from . import widgets as w
import random

class MenuClass(tk.Menu):

    def __init__(self, master=None):
        super().init(master)
        self.master = master
        self.file = tk.Menu(self)
        self.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="Open", command=master.open)


