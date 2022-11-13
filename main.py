import etc._funct_ as fnct
import tkinter as base_builder

# Body Base
base = base_builder.Tk()
base.geometry("1080x720")
base.minsize(967, 554)
base.title("Student Information System")

# Header Frame
header_frm = base_builder.Frame(base)
header_frm.pack(side='top', anchor='nw')

# Display Frame
display_frm = base_builder.Frame(base)
display_frm.pack(side='right', anchor='n', fill='y', pady=10, padx=25)
scrool = base_builder.Scrollbar(display_frm)
scrool.pack(side='right', fill='y')

# Menu Frame
menu_frm = base_builder.Frame(base, borderwidth=5, relief='solid', padx=0)
menu_frm.pack(side='left', anchor='w', fill='y', pady=10)

# Displayer Box
displayer = base_builder.Text(display_frm, height=110, width=90,fg='green', relief='solid', borderwidth=5, padx=5, pady=5, yscrollcommand=scrool.set, font=("algeria", 10, 'bold'))
displayer.pack(side='right', anchor='e', pady=10, fill='both')

# ----------------------------------------------------------------------------------------------------------------------

# Functions


def view_tables():
    """ List all the tables from sql database. """
    def table_select():
        fnct.logs("Clicked on view table.")
        global table
        table = choicevalue.get()
        displayer.insert(base_builder.END, f"\n {table} selected successfully")
        fnct.logs("Table selected successfully.")
    tables = fnct.dbs_agent("SHow tables;")
    for data in tables:
        for sdata in data:
            displayer.insert(base_builder.END, f" {sdata}\n")
    fnct.logs("Table displayed successfully")
    base_builder.Label(display_frm, text="Select Record", font=(" ", 15, 'bold')).pack(side='top', anchor='n', padx=5, pady=15)
    choicevalue = base_builder.StringVar()
    base_builder.Entry(display_frm, textvariable=choicevalue, relief='solid', borderwidth=2).pack(side='left', anchor='ne', fill='x', padx=5, pady=2)
    base_builder.Button(display_frm, text='Submit', relief='solid',fg='green', command=table_select).pack(side='right', anchor='nw', padx=5)

def new_rec():
    # fnct.dbs_agent(f"insert into {table} (Name, )")
    pass


# Logo
logo = base_builder.PhotoImage(file='image/logo.png')
logo_printer = base_builder.Label(header_frm, image=logo, padx=5, pady=5)
logo_printer.pack(side='left', anchor='nw', padx=20)

# Select Table
sel_rec = base_builder.Button(menu_frm, text="Select Table", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"), command=view_tables)
sel_rec.pack(pady=10)

# New record
new_rec = base_builder.Button(menu_frm, text="New Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=20, font=("abel", 12, "bold"), command=new_rec)
new_rec.pack(pady=10)

# Update Record
upd_rec = base_builder.Button(menu_frm, text="Update Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"))
upd_rec.pack(pady=10)

# Delete Record
del_rec = base_builder.Button(menu_frm, text="Delete Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"))
del_rec.pack(pady=10)

# Creater Name
creater_name = base_builder.Label(menu_frm, text="Created By Matang Mehra", fg='blue', padx=15, font=("abel", 15, "bold"))
creater_name.pack(side='bottom', anchor='s')

base.mainloop()


