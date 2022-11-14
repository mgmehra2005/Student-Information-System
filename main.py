import etc._funct_ as fnct
import tkinter as base_builder
from colorama import Fore, Style
import os

try:
    # Body Base
    base = base_builder.Tk()
    base.geometry("1280x480")
    base.minsize(967, 554)
    if "config.py" in os.listdir():

        base.title("Student Information System")

        # Header Frame
        header_frm = base_builder.Frame(base)
        header_frm.pack(side='top', anchor='nw', fill='x')

        # Display Frame
        display_frm = base_builder.Frame(base, relief='solid', borderwidth=2, width=100)
        display_frm.pack(side='right', anchor='n', fill='y', pady=10, padx=25)

        # Menu Frame
        menu_frm = base_builder.Frame(base, borderwidth=2, relief='solid', padx=0)
        menu_frm.pack(side='left', anchor='w', fill='y', pady=10, padx=5)

        # Displayer Box
        scroll = base_builder.Scrollbar(display_frm)
        scroll.pack(side='right', fill='y')
        displayer = base_builder.Text(display_frm, height=90, width=140, fg='green', relief='solid',
                                      borderwidth=2, padx=5, pady=5, font=("algeria", 10, 'bold'),
                                      yscrollcommand=scroll.set)
        displayer.pack(side='right', anchor='e', pady=10, padx=5, fill='both')
        scroll.config(command=displayer.yview)


        # ----------------------------------------------------------------------------------------------------------------------

        # Functions
        def display_clear():
            displayer.delete("1.0", "end")


        def view_tables():
            """ List all the tables from sql database. """
            fnct.logs("Clicked on view table.")
            display_clear()
            def table_select():
                global table
                table = choicevalue.get()
                displayer.insert(base_builder.END, f"\n {table} selected successfully")
                fnct.logs("Table selected successfully.")

            tables = fnct.dbs_agent("SHow tables;")
            for data in tables:
                for sdata in data:
                    displayer.insert(base_builder.END, f" {sdata}\n")
            fnct.logs("Table displayed successfully")
            base_builder.Label(header_frm, text="Select Record", font=(" ", 15, 'bold')).pack(side='top', anchor='ne',
                                                                                              padx=5, pady=15)
            choicevalue = base_builder.StringVar()
            base_builder.Entry(header_frm, textvariable=choicevalue, relief='solid', borderwidth=2).pack(side='right',
                                                                                                         anchor='ne',
                                                                                                         fill='x',
                                                                                                         padx=10,
                                                                                                         pady=2)
            base_builder.Button(header_frm, text='Submit', relief='solid', fg='green', command=table_select).pack(
                side='right', anchor='ne', padx=5)


        def show_record():
            """ Displays all the data of a record. """
            fnct.logs("Record displayed successfully.")
            from tabulate import tabulate
            display_clear()
            record = fnct.dbs_agent(f"select ID, name, roll_num, Phone_num, Address from {table};")
            displayer.insert(base_builder.END,
                             f"\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> {table} <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
            displayer.insert(base_builder.END, f"\n")

        def new_record():
            import tkinter as tki
            display_clear()
            def submit_rec():
                pass
                try:
                    fnct.dbs_agent(
                        f"insert into {table} (Name, Rol_num, phone_num, father_name, mother_name, address, dob) values('{name.get()}', {int(roll_num.get())}, {int(phone_num.get())}, '{father_name.get()}', '{mother_name.get()}', '{address.get()}', '{dob.get()}')")
                    fnct.logs("Data Submitted successfully.")
                    displayer.insert(base_builder.TOP, "Data Added to the record.")
                    exit()
                except Exception as e:
                    print(Fore.Red + "Error in Submitting record. To know more check the logs.")
                    fnct.logs(f"Error -> {e}")
                    exit()
            height = 280
            width = 350
            new_rec_base = tki.Tk()
            new_rec_base.geometry(f"{width}x{height}")
            new_rec_base.minsize(width, height)
            new_rec_base.maxsize(width, height)
            new_rec_base.title("Student Information System - New Record")
            tki.Label(new_rec_base, text="NEW RECORD", fg="black", font=("Abel", 20, 'bold')).pack()
            name = tki.StringVar
            roll_num = tki.StringVar
            phone_num = tki.StringVar
            father_name = tki.StringVar
            mother_name = tki.StringVar
            address = tki.StringVar
            dob = tki.StringVar

            tki.Label(new_rec_base, text="FULL NAME", font=(" ", 10, 'bold')).place(x=2, y=45)
            tki.Entry(new_rec_base, textvariable=name, relief='solid').place(x=200, y=45)

            tki.Label(new_rec_base, text="ROLL NUMBER", font=(" ", 10, 'bold')).place(x=2, y=70)
            tki.Entry(new_rec_base, textvariable=roll_num, relief='solid').place(x=200, y=70)

            tki.Label(new_rec_base, text="PHONE NUMBER", font=(" ", 10, 'bold')).place(x=2, y=95)
            tki.Entry(new_rec_base, textvariable=phone_num, relief='solid').place(x=200, y=95)

            tki.Label(new_rec_base, text="FATHER NAME", font=(" ", 10, 'bold')).place(x=2, y=120)
            tki.Entry(new_rec_base, textvariable=father_name, relief='solid').place(x=200, y=120)

            tki.Label(new_rec_base, text="MOTHER NAME", font=(" ", 10, 'bold')).place(x=2, y=145)
            tki.Entry(new_rec_base, textvariable=mother_name, relief='solid').place(x=200, y=145)

            tki.Label(new_rec_base, text="ADDRESS", font=(" ", 10, 'bold')).place(x=2, y=170)
            tki.Entry(new_rec_base, textvariable=address, relief='solid').place(x=200, y=170)

            tki.Label(new_rec_base, text="D.O.B", font=(" ", 10, 'bold')).place(x=2, y=195)
            tki.Entry(new_rec_base, textvariable=dob, relief='solid').place(x=200, y=195)

            tki.Button(new_rec_base, text='Submit', bg='#34a700', fg='white', padx=15, pady=5, font=(" ", 10, 'bold'), command=submit_rec).pack(side='bottom', pady=10)
            new_rec_base.mainloop()

        # Logo
        logo = base_builder.PhotoImage(file='image/logo.png')
        logo_printer = base_builder.Label(header_frm, image=logo, padx=5, pady=5)
        logo_printer.pack(side='left', anchor='nw', padx=20)

        # Welcome Text
        # base_builder.Label(header_frm, text="Welcome to Student Information System", fg="#5b5b5b", font=("Abel", 15, 'bold'), justify="center").pack(anchor='n')

        # Select Table
        sel_rec = base_builder.Button(menu_frm, text="Select Table", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"), command=view_tables)
        sel_rec.pack(pady=10)

        # Show Record
        show_rec = base_builder.Button(menu_frm, text="Show Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"), command=show_record)
        show_rec.pack(pady=10)
        # New record
        new_rec = base_builder.Button(menu_frm, text="New Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=20, font=("abel", 12, "bold"), command=new_record)
        new_rec.pack(pady=10)

        # Update Record
        upd_rec = base_builder.Button(menu_frm, text="Update Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"))
        upd_rec.pack(pady=10)

        # Delete Record
        del_rec = base_builder.Button(menu_frm, text="Delete Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"))
        del_rec.pack(pady=10)

        # Exit
        ext = base_builder.Button(menu_frm, text="Exit", fg='green', borderwidth=1, relief='solid', pady=2, padx=45, font=("abel", 12, "bold"), command=exit)
        ext.pack(pady=10)

        # Creater Name
        creater_name = base_builder.Label(menu_frm, text="Created By Matang Mehra", fg='blue', padx=15,
                                          font=("abel", 15, "bold"))
        creater_name.pack(side='bottom', anchor='s')

    # Configuration
    else:
        base.title("Student Information System - Configuration")
        # Logo
        logo = base_builder.PhotoImage(file='image/logo.png')
        logo_printer = base_builder.Label(base, image=logo, padx=5, pady=5)
        logo_printer.pack(side='left', anchor='nw', padx=20)
    base.mainloop()
except Exception as error:
    fnct.logs(f"Error -> {error}")
    print(Fore.RED + "Error while executing the program. To know more checkout the logs.")
    Style.RESET_ALL
