from functions import *

root = Tk()
root.title('Password Storage')

root['bg']='#fb0'
root.geometry('400x300')
root.columnconfigure(0, weight=1)   
root.rowconfigure(0, weight=1)      

container = Frame(root)
container.grid(row=0, column=0)

def exit_program():
    root.quit()
    print('\nShutting the program down, wait a second.')
    sleep(0.5)
    sys.exit()


new_record_apg_btn = Button(container, text="NEW RECORD(APG)", command=data, padx=20, pady=10, width=20).grid(row=0, column=0)

new_record_btn = Button(container, text="NEW RECORD", command=add_record, padx=20, pady=10, width=20).grid(row=1, column=0)

edit_record_btn = Button(container, text="EDIT RECORD", command=edit_record, padx=20, pady=10, width=20).grid(row=2, column=0)

delete_record_btn = Button(container, text="DELETE RECORD", command=delete_record, padx=20, pady=10, width=20).grid(row=3, column=0)

show_record_btn = Button(container, text="SHOW RECORDS", command=show_records, padx=20, pady=10, width=20).grid(row=4, column=0)

exit_program_btn = Button(container, text="EXIT PROGRAM", command=exit_program, padx=20, pady=10, width=20   ).grid(row=5, column=0)

root.mainloop()