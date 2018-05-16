import secrets
import string
from tkinter import *


def generate(*args):
    al = (string.ascii_letters + string.digits)
    try:
        value = int(length.get())
        password.set(''.join(secrets.choice(al) for i in range(value)))
    except ValueError:
        pass


root = Tk()
root.title('pwgen')

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

password = StringVar()
length = StringVar()

length_entry = Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=1, sticky=(W, E))
Label(mainframe, textvariable=password).grid(column=2, row=2, sticky=(W, E))
Button(mainframe, text="Generate", command=generate).grid(column=3, row=3, sticky=W)
Label(mainframe, text="characters").grid(column=3, row=1, sticky=W)
Label(mainframe, text="your password is").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

length_entry.focus()
root.bind('<Return>', generate)

root.mainloop()
