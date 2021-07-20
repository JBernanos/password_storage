import sys
from random import randint
from tkinter import *
from tkinter import messagebox

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '?', '{', '[', '(', '}', ']', ')', '.', ',', '<', '>', '-', '+', '=', '*', '/']


def not_agp_password():
    isRandom = False
    top_record_data(isRandom)


def agp_password():
    isRandom = True
    top_record_data(isRandom)


def top_record_data(isRandom):
    global top
    top = Toplevel()
    top['bg']='#fb0'

    record_name_label = Label(top, text="Record Name: ").grid(row=0, column=0)
    record_name = Entry(top, width=15)
    record_name.grid(row=0, column=1)

    login_label = Label(top, text="Login: ").grid(row=1, column=0)
    login = Entry(top, width=15)
    login.grid(row=1, column=1)

    if isRandom:
        password_label = Label(top, text="Password Size: ").grid(row=2, column=0)
        password_size = Entry(top, width=15)
        password_size.grid(row=2, column=1)
        submit_btn = Button(top, text="Submit", command=lambda: validate_password_size(password_size, top, record_name, login)).grid(row=3, column=0)
    
    else:
        password_label = Label(top, text="Password: ").grid(row=2, column=0)
        password = Entry(top, width=15)
        password.grid(row=2, column=1)
        submit_btn = Button(top, text="Submit", command=lambda: store_password(str(password.get()), record_name, login)).grid(row=3, column=0)


def validate_password_size(password_size, top, record_name, login):
    value = password_size.get()
    value = int(value)

    if value < 8:
        top.destroy()
        messagebox.showerror("[ERROR]", "Password Size should be greater or equal than 8!")
        top_record_data()
    
    else:
        password = [0] * value
        create_password(password, value, record_name, login)


def create_password(password, password_size, record_name, login):
    counter1 = counter2 = counter3 = counter4 = 0
    position = 0

    while counter1 < 2 or counter2 < 2 or counter3 < 2 or counter4 < 2 or position < password_size:
        option = randint(1, 4)

        if option == 1 and counter1 < 2:
            insert_upper_case_letters(password, position)
            counter1 += 1
            position += 1

        elif option == 2 and counter2 < 2:
            insert_lower_case_letters(password, position)
            counter2 += 1
            position += 1

        elif option == 3 and counter3 < 2:
            insert_numbers(password, position)
            counter3 += 1
            position += 1

        elif option == 4 and counter4 < 2:
            insert_special_characters(password, position)
            counter4 += 1
            position += 1

        elif counter1 >= 2 and counter2 >= 2 and counter3 >= 2 and counter4 >= 2:
            option = randint(1, 4)

            if option == 1:
                insert_upper_case_letters(password, position)
                position += 1

            elif option == 2:
                insert_lower_case_letters(password, position)
                position += 1

            elif option == 3:
                insert_numbers(password, position)
                position += 1

            elif option == 4:
                insert_special_characters(password, position)
                position += 1
                
    password = list_to_string(password)
    store_password(password, record_name, login)
    

def insert_upper_case_letters(password, position):
    elem = randint(0, 25)
    password[position] = uppercase_letters[elem]
    return password


def insert_lower_case_letters(password, position):
    elem = randint(0, 25)
    password[position] = lowercase_letters[elem]
    return password


def insert_numbers(password, position):
    elem = randint(0, 9)
    password[position] = numbers[elem]
    return password


def insert_special_characters(password, position):

    elem = randint(0, 16)
    password[position] = special_characters[elem]
    return password


def list_to_string(password):
    string = ""

    for ele in password:
        string += ele

    return string


def store_password(password, record_name, login):
    record_name = record_name.get()
    record_name = record_name.upper()
    login = login.get()

    top.destroy()

    with open('data.txt', 'a') as file:
        file.write(
            f'Record Name: {record_name} \nLogin: {login} \nPassword: {password} \n')
        file.write('====================================\n')

    messagebox.showinfo("[SUCCESS]", "Record Successfully Added")


def change_record():
    deleteRecord = False
    top_record_name(deleteRecord)


def delete_record():
    deleteRecord = True
    top_record_name(deleteRecord)


def top_record_name(deleteRecord):
    global top
    top = Toplevel()
    top['bg']='#fb0'

    if deleteRecord:
        record_name_label = Label(top, text="Record Name: ").grid(row=0, column=0)
        record_name = Entry(top, width=15)
        record_name.grid(row=0, column=1)

        submit_btn = Button(top, text="Submit", command=lambda: remove_record(str(record_name.get()))).grid(row=3, column=0)

    else:
        record_name_label = Label(top, text="Record Name: ").grid(row=0, column=0)
        record_name = Entry(top, width=15)
        record_name.grid(row=0, column=1)

        submit_btn = Button(top, text="Submit", command=lambda: edit_record(str(record_name.get()))).grid(row=3, column=0)
        

def remove_record(record_name):
    record_name = record_name.upper()
    record_on_data = 0
    counter = 0
    with open('data.txt', 'r') as file:
        lines = file.readlines()

    with open('data.txt', 'w') as file:
        for line in lines:
            if line.strip("\n") != f'Record Name: {record_name} ' and counter == 0:
                file.write(line)

            elif line.strip("\n") == f'Record Name: {record_name} ' and counter == 0:
                counter = 3
                record_on_data = 1

            elif line.strip("\n") != f'Record Name: {record_name} ' and counter != 0:
                counter -= 1

    if record_on_data == 1:
        sucess_msg()

    else:
        fail_msg()


def sucess_msg():
    messagebox.showinfo("Delete Record", "Record Sucesseful removed!")
    top.destroy()


def fail_msg():
    messagebox.showinfo("Delete Record", "Record not found!")
    top.destroy()


def show_records(): 
    top = Toplevel()
    top['bg']='#fb0'

    txtarea = Text(top, width=40, height=20)
    txtarea.pack(pady=20)
    
    file = "C:/Users/jpb/Desktop/JPB/RandomCodes/python/password_storage/data.txt" #change this
    file = open(file)
    data = file.read()
    txtarea.insert(END, data)
    file.close()
