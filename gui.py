import tkinter as tk
from radiobutton import SelectionTest
from cleartmp import ClearTemp, GetDisks
import status

root = tk.Tk()
root.title("ClearTemp")
root.geometry('250x200')
root.resizable(False, False)

disks = GetDisks()

sucess_label = tk.Label(text='')

# Clean files and dirs
def clear_gui():
    ClearTemp(disks[st.value.get()])
    response = status.ReadStatus()
    sucess_label['text'] = response['status']
    sucess_label.pack()

# Create Button Clear and Label Select Disk
button1 = tk.Button(root, text='Clear Now', command=clear_gui)
Label1 = tk.Label(text='Select a Disk: ')


# Show Text "Select Disk"
Label1.pack()

# Create RadioButtons for disks 
st = SelectionTest(root, disks)

# Show Button Clean
button1.pack()

# Start GUI
root.mainloop()
