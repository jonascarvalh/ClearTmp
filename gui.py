import tkinter as tk
from tkinter import ttk

from src import radiobutton as rb
from src import status
from src import cleartmp as ct

root = tk.Tk()

root.tk.call('source', 'azure.tcl')
root.tk.call('set_theme', 'dark')


root.title("ClearTemp")
root.geometry('250x200')
root.resizable(False, False)

disks = ct.GetDisks()

sucess_label = tk.Label(text='')

# Clean files and dirs
def clear_gui():
    ct.ClearTemp(disks[st.value.get()])
    response = status.ReadStatus()
    sucess_label['text'] = response['status']
    sucess_label.pack()

# Create Button Clear and Label Select Disk
button1 = ttk.Button(root, text='Clear Now', command=clear_gui)
Label1 = ttk.Label(text='Select a Disk: ')


# Show Text "Select Disk"
Label1.pack()

# Create RadioButtons for disks 
st = rb.SelectionTest(root, disks)

# Show Button Clean
button1.pack()

# Start GUI
root.mainloop()
