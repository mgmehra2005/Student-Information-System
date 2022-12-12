import etc._funct_ as fnct
import tkinter as base_builder
from colorama import Fore, Style
import os
from time import sleep
try:
    # Body Base
    fnct.logs("Program Started")
    base = base_builder.Tk()
    icon_image = base_builder.PhotoImage(file='image/logo.png')
    base.iconphoto(True, icon_image)
    if "config.py" in os.listdir():
        base.geometry("13600x720")
        base.minsize(967, 554)
        base.title("Student Information System")

        # Header Frame
        header_frm = base_builder.Frame(base, relief='solid', borderwidth=0)
        header_frm.pack(side='top', anchor='nw', fill='x')

        # Display Frame
        display_frm = base_builder.Frame(base, relief='solid', borderwidth=0, width=80)
        display_frm.pack(side='right', anchor='n', fill='y', pady=0, padx=2)

        # Menu Frame
        menu_frm = base_builder.Frame(base, borderwidth=2, relief='solid', padx=0)
        menu_frm.pack(side='left', anchor='w', fill='y', pady=10, padx=1)

        # Displayer Box
        scroll = base_builder.Scrollbar(display_frm)
        scroll.pack(side='right', fill='y')
        displayer = base_builder.Text(display_frm, height=90, width=132, fg='green', relief='solid',
                                      borderwidth=2, padx=4, pady=5,
                                      yscrollcommand=scroll.set)
        displayer.pack(side='right', anchor='e', pady=10, padx=0)
        scroll.config(command=displayer.yview)

        # Option Frame
        option_frm = base_builder.Frame(header_frm, relief='solid', borderwidth=0, width=1070, height=95)
        option_frm.place(x=285, y=5)

        # ----------------------------------------------------------------------------------------------------------------------

        # Functions

        open_box = lambda: displayer.config(state='normal')

        close_box = lambda: displayer.config(state='disabled')

        def display_clear():
            open_box()
            displayer.delete("1.0", "end")

        def frame_clear(frame):
            for width in frame.winfo_children():
                width.destroy()

        def view_tables():
            """ List all the tables from sql database. """
            from tabulate import tabulate
            fnct.logs("Clicked on view table.")
            display_clear()
            frame_clear(option_frm)
            open_box()

            def table_select():
                open_box()
                global table
                table = choicevalue.get()
                display_clear()
                displayer.insert(base_builder.END, f"\n {table} selected successfully")
                close_box()
                fnct.logs("Table selected successfully.")

            tables = fnct.dbs_agent("show tables;")
            displayer.insert(base_builder.END, f"{tabulate(tables, tablefmt='fancy_grid')}")
            close_box()
            fnct.logs("Table displayed successfully")
            base_builder.Label(option_frm, text="Select Record", font=(" ", 13, 'bold')).place(x=10, y=5)
            choicevalue = base_builder.StringVar()
            base_builder.Entry(option_frm, textvariable=choicevalue, relief='solid', borderwidth=1).place(x=10, y=35)
            base_builder.Button(option_frm, text='Submit', relief='solid', fg='green', command=table_select, padx=10, pady=2).place(x=145, y=25)


        def show_record():
            open_box()
            try:
                """ Displays all the data of a record. """
                from tabulate import tabulate
                display_clear()
                frame_clear(option_frm)
                header = ["ID", "Name", "Roll No.", "Phone No.", "Address", "Mother Name", "Father Name", "DOB"]
                record = fnct.dbs_agent(f"select * from {table};")
                displayer.insert(base_builder.END, f'{tabulate(record, headers=header, tablefmt="fancy_grid")}')
                close_box()
                fnct.logs("Record displayed successfully.")
            except Exception as e:
                fnct.logs(f"Error -> {e}")
                print(Fore.RED + "Error while displaying records. To know more checkout the logs.")
                Style.RESET_ALL

        def new_record():
            frame_clear(option_frm)
            display_clear()
            def submit_rec():
                from tabulate import tabulate
                open_box()
                insert_agent = fnct.dbs_agent(f"insert into {table} (Name,Roll_num, phone_num, father_name, mother_name, address, dob) values('{name.get()}', '{roll_num.get()}', '{phone_num.get()}', '{father_name.get()}', '{mother_name.get()}', '{address.get()}', '{dob.get()}');")
                fnct.logs("Data Recorded Successfully.")
                header = ["ID", "Name", "Roll No.", "Phone No.", "Address", "Mother Name", "Father Name", "DOB"]
                data_box =[[name.get(), roll_num.get(), phone_num.get(), father_name.get(), mother_name.get(), address.get(), dob.get()]]
                displayer.insert(base_builder.END, f'{tabulate(data_box, headers=header, tablefmt="fancy_grid")}')
                displayer.insert(base_builder.END, '\nData Recorded Successfully.\n')

            name = base_builder.StringVar()
            roll_num = base_builder.StringVar()
            phone_num = base_builder.StringVar()
            father_name = base_builder.StringVar()
            mother_name = base_builder.StringVar()
            address = base_builder.StringVar()
            dob = base_builder.StringVar()

            base_builder.Label(option_frm, text="FULL NAME : ", font=(" ", 10, 'bold')).place(x=5, y=2)
            base_builder.Entry(option_frm, textvariable=name, relief='solid').place(x=95, y=4)

            base_builder.Label(option_frm, text="ROLL NUMBER : ", font=(" ", 10, 'bold')).place(x=225, y=2)
            base_builder.Entry(option_frm, textvariable=roll_num, relief='solid').place(x=335, y=4)

            base_builder.Label(option_frm, text="PHONE NUMBER : ", font=(" ", 10, 'bold')).place(x=460, y=2)
            base_builder.Entry(option_frm, textvariable=phone_num, relief='solid').place(x=580, y=4)

            base_builder.Label(option_frm, text="FATHER NAME : ", font=(" ", 10, 'bold')).place(x=710, y=2)
            base_builder.Entry(option_frm, textvariable=father_name, relief='solid').place(x=820, y=4)

            base_builder.Label(option_frm, text="MOTHER NAME : ", font=(" ", 10, 'bold')).place(x=5, y=40)
            base_builder.Entry(option_frm, textvariable=mother_name, relief='solid').place(x=115, y=42)

            base_builder.Label(option_frm, text="ADDRESS : ", font=(" ", 10, 'bold')).place(x=250, y=40)
            base_builder.Entry(option_frm, textvariable=address, relief='solid').place(x=325, y=42)
            # #
            base_builder.Label(option_frm, text="D.O.B : ", font=(" ", 10, 'bold')).place(x=460, y=40)
            base_builder.Entry(option_frm, textvariable=dob, relief='solid').place(x=510, y=42)

            base_builder.Button(option_frm, text='Submit', bg='#34a700', fg='white', padx=15, pady=5, font=(" ", 10, 'bold'), command=submit_rec).place(x=950, y=2)

        def update_rec():
            show_record()
            frame_clear(option_frm)
            def update_rec():
                open_box
                from tabulate import tabulate
                frame_clear(option_frm)
                display_clear()

                if name.get() == 1:
                    fnct.dbs_agent(f"update {table} set Name = '{name_up.get()}' where id = {student_id.get()};")
                if phone_number.get() == 1:
                    fnct.dbs_agent(f"update {table} set phone_num = '{phone_num_up.get()}' where id = {student_id.get()};")
                if roll_number.get() == 1:
                    fnct.dbs_agent(f"update {table} set roll_num = '{roll_num_up.get()}' where id = {student_id.get()};")
                if address.get() == 1:
                    fnct.dbs_agent(f"update {table} set address = '{address_up.get()}' where id = {student_id.get()};")
                if mother_name.get() == 1:
                    fnct.dbs_agent(f"update {table} set mother_name = '{mother_name_up.get()}' where id = {student_id.get()};")
                if father_name.get() == 1:
                    fnct.dbs_agent(f"update {table} set father_name = '{father_name_up.get()}' where id = {student_id.get()};")
                if dob.get() == 1:
                    fnct.dbs_agent(f"update {table} set dob = '{dob_up.get()}' where id = {student_id.get()};")

                try:
                    to_updt = fnct.dbs_agent(f'Select * from {table} where ID = {student_id.get()};')
                    header = ["ID", "Name", "Roll No.", "Phone No.", "Address", "Mother Name", "Father Name", "DOB"]
                    displayer.insert(base_builder.END, f'{tabulate(to_updt, headers=header, tablefmt="fancy_grid")}')
                    fnct.logs("Data updated successfully.")
                    close_box()
                except Exception as error_toupdt:
                    print(Fore.RED + "There is an error occurring. Please Check logs for more information.")
                    fnct.logs(f"Error -> {error_toupdt}")

            def select_rec():
                open_box()
                from tabulate import tabulate

                frame_clear(option_frm)
                display_clear()

                global name_up
                global roll_num_up
                global phone_num_up
                global address_up
                global mother_name_up
                global father_name_up
                global dob_up

                name_up = base_builder.StringVar()
                roll_num_up = base_builder.StringVar()
                phone_num_up = base_builder.StringVar()
                address_up = base_builder.StringVar()
                mother_name_up = base_builder.StringVar()
                father_name_up = base_builder.StringVar()
                dob_up = base_builder.StringVar()
                try:
                    updt_in = fnct.dbs_agent(f'Select * from {table} where ID = {student_id.get()};')
                    header = ["ID", "Name", "Roll No.", "Phone No.", "Address", "Mother Name", "Father Name", "DOB"]
                    displayer.insert(base_builder.END, f'{tabulate(updt_in, headers=header, tablefmt="fancy_grid")}')
                    close_box()
                except Exception as error_updt:
                    print(Fore.RED + "There is an error. Please check logs for more information.")
                    fnct.logs(f"Error -> {error_updt}")

                if name.get() == 1:
                    base_builder.Label(option_frm, text="FULL NAME : ", font=(" ", 10, 'bold')).place(x=5, y=2)
                    base_builder.Entry(option_frm, textvariable=name_up, relief='solid').place(x=95, y=4)
                if phone_number.get() == 1:
                    base_builder.Label(option_frm, text="PHONE NUMBER : ", font=(" ", 10, 'bold')).place(x=225, y=2)
                    base_builder.Entry(option_frm, textvariable=phone_num_up, relief='solid').place(x=345, y=4)
                if roll_number.get() == 1:
                    base_builder.Label(option_frm, text="ROLL NUMBER : ", font=(" ", 10, 'bold')).place(x=480, y=2)
                    base_builder.Entry(option_frm, textvariable=roll_num_up, relief='solid').place(x=600, y=4)
                if address.get() == 1:
                    base_builder.Label(option_frm, text="ADDRESS : ", font=(" ", 10, 'bold')).place(x=750, y=2)
                    base_builder.Entry(option_frm, textvariable=address_up, relief='solid').place(x=835, y=4)
                if mother_name.get() == 1:
                    base_builder.Label(option_frm, text="MOTHER NAME : ", font=(" ", 10, 'bold')).place(x=5, y=40)
                    base_builder.Entry(option_frm, textvariable=mother_name_up, relief='solid').place(x=115, y=42)
                if father_name.get() == 1:
                    base_builder.Label(option_frm, text="FATHER NAME : ", font=(" ", 10, 'bold')).place(x=250, y=40)
                    base_builder.Entry(option_frm, textvariable=father_name_up, relief='solid').place(x=380, y=42)
                if dob.get() == 1:
                    base_builder.Label(option_frm, text="DOB : ", font=(" ", 10, 'bold')).place(x=520, y=40)
                    base_builder.Entry(option_frm, textvariable=dob_up, relief='solid').place(x=580, y=42)
                base_builder.Button(option_frm, text="UPDATE", font=(' ', 11, 'bold'), bg='#34a700', fg='white', command=update_rec).place(x=800, y=40)

            base_builder.Label(option_frm, text='ID of the student : ', font=(' ', 10,'bold')).place(x=2, y=2)
            student_id = base_builder.StringVar()
            student_id_entry = base_builder.Entry(option_frm, textvariable=student_id, relief='solid', borderwidth=1)
            student_id_entry.place(x=2, y=25)
            base_builder.Label(option_frm, text='Select field to update', font=(' ', 10, 'bold')).place(x=180, y=2)

            # Entry variables
            name = base_builder.IntVar()
            roll_number = base_builder.IntVar()
            phone_number = base_builder.IntVar()
            address = base_builder.IntVar()
            mother_name = base_builder.IntVar()
            father_name = base_builder.IntVar()
            dob = base_builder.IntVar()

            # Check Buttons
            base_builder.Checkbutton(option_frm, text='Name', variable=name).place(x=180, y=25)
            base_builder.Checkbutton(option_frm, text='Roll Number', variable=roll_number).place(x=350, y=25)
            base_builder.Checkbutton(option_frm, text='Phone Number', variable=phone_number).place(x=500, y=25)
            base_builder.Checkbutton(option_frm, text='Address', variable=address).place(x=650, y=25)
            base_builder.Checkbutton(option_frm, text='Mother Name', variable=mother_name).place(x=180, y=50)
            base_builder.Checkbutton(option_frm, text='Father Name', variable=father_name).place(x=350, y=50)
            base_builder.Checkbutton(option_frm, text='DOB', variable=dob).place(x=500, y=50)

            base_builder.Button(option_frm, text='SUBMIT', font=(' ', 11, 'bold'), bg='#34a700', fg='white', command=select_rec).place(x=800, y=15)

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

        upd_rec = base_builder.Button(menu_frm, text="Update Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"), command=update_rec)
        upd_rec.pack(pady=10)

        # Delete Record
        del_rec = base_builder.Button(menu_frm, text="Delete Record", fg='green', borderwidth=1, relief='solid', pady=2, padx=15, font=("abel", 12, "bold"))
        del_rec.pack(pady=10)

        # Exit
        ext = base_builder.Button(menu_frm, text="Exit", fg='green', borderwidth=1, relief='solid', pady=2, padx=45, font=("abel", 12, "bold"), command=quit)
        ext.pack(pady=10)

        # Creater Name
        creater_name = base_builder.Label(menu_frm, text="Created By Matang Mehra", fg='blue', padx=15,
                                          font=("abel", 15, "bold"))
        creater_name.pack(side='bottom', anchor='s')

    # Configuration File Missing Error
    else:
        base.title("Student Information System - Configuration Error")
        base.geometry("400x100")
        base_builder.Label(base, text="Configuration file is missing.", fg='red', font=(' ', 12, 'bold')).pack(side='top', pady=5)
        base_builder.Button(base, text='Exit', relief='solid', borderwidth=1, pady=2, padx=15, command=quit, fg='blue').pack(anchor='se', side='bottom', pady=5, padx=10)
    base.mainloop()
except Exception as error:
    fnct.logs(f"Error -> {error}")
    print(Fore.RED + "Error while executing the program. To know more checkout the logs.")
    Style.RESET_ALL
    sleep(4)
    exit()
