from tkinter import *
from tkinter import ttk

class SelectionTest:
    def __init__(self, root, discos):
        self.root = root
        self.value = IntVar()

        i = 0
        for disco in discos:
            ttk.Radiobutton(self.root, text=f'{disco}', variable=self.value, value=i).pack()
            i+=1