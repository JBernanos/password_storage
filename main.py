from functions import *

root = Tk()
root.title('Password Storage')

print('========================================\n'
    '1- NEW RECORD(AUTO GENERATED PASSWORD)\n'
    '2- NEW RECORD\n' 
    '3- EDIT A RECORD\n'
    '4- DELETE A RECORD\n'
    '5- CONSULT YOUR RECORDS\n'
    '6- QUIT\n'
    'CHOOSE ONE OPTION: ')
print('========================================')

new_record_apg_btn = Button(root, text="NEW RECORD(APG)", command=data, padx=20, pady=10).grid(row=0, column=0)

new_record_btn = Button(root, text="NEW RECORD", command=add_record, padx=20, pady=10).grid(row=1, column=0)

edit_record_btn = Button(root, text="EDIT RECORD", command=edit_record, padx=20, pady=10).grid(row=2, column=0)

delete_record_btn = Button(root, text="DELETE RECORD", command=delete_record, padx=20, pady=10).grid(row=3, column=0)

show_record_btn = Button(root, text="SHOW RECORDS", command=show_records, padx=20, pady=10).grid(row=4, column=0)

exit_program_btn = Button(root, text="EXIT PROGRAM", command=exit_program, padx=20, pady=10).grid(row=5, column=0)

root.mainloop()