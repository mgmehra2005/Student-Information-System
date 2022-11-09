from colorama import Fore, Style
import etc._funct_ as fnct
import os
import tkinter as base_builder

# Body Base
base = base_builder.Tk()
base.geometry("967x554")
base.minsize(967, 554)
base.title("Student Information System")

# Header Frame
header_frm = base_builder.Frame(base)
header_frm.pack(side='top', anchor='nw')

# Logo
logo = base_builder.PhotoImage(file='image/logo.png')
logo_printer = base_builder.Label(header_frm, image=logo, padx=5, pady=5)
logo_printer.pack(side='left', anchor='nw')

# Menu Frame
menu_frm = base_builder.Frame(base, borderwidth=5, relief='solid', padx=40)
menu_frm.pack(side='left', anchor='w', fill='y', pady=10)

# Select Record
sel_rec = base_builder.Button(menu_frm, text="Select Table", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 10, "bold"))
sel_rec.pack(pady=10)

# New record
new_rec = base_builder.Button(menu_frm, text="New Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 10, "bold"))
new_rec.pack(pady=10)
base.mainloop()
