import sys
from time import sleep
from random import randint
from tkinter import *
from tkinter import messagebox


def data():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = [
        '!', '?', '{', '[', '(', '}', ']', ')', '.', ',', '<', '>', '-', '+', '=', '*', '/']
    password_length()
    create_password(uppercase_letters, lowercase_letters, numbers,
                    special_characters, password, length)


def test(password_size):
    int(password_size)
    password = [] * password_size
    var = password_size
    print(var)
    print('AAAAA')

def password_length():

    top = Toplevel()
    top['bg'] = '#fb0'

    text_label = Label(top, text="Password Size:").grid(row=0, column=0) 
    password_size = Entry(top, width=30).grid(row=0, column=1)
    submit_btn = Button(top, text="Submit").grid(row=0, column=2)
    password = [] * password_size

    test(password_size)
     




def create_password(uppercase_letters, lowercase_letters, numbers, special_characters, password, length):
    counter1 = counter2 = counter3 = counter4 = 0
    position = 0

    while counter1 < 2 or counter2 < 2 or counter3 < 2 or counter4 < 2 or position < length:
        option = randint(1, 4)

        if option == 1 and counter1 < 2:
            insert_upper_case_letters(uppercase_letters, password, position)
            counter1 += 1
            position += 1

        elif option == 2 and counter2 < 2:
            insert_lower_case_letters(lowercase_letters, password, position)
            counter2 += 1
            position += 1

        elif option == 3 and counter3 < 2:
            insert_numbers(numbers, password, position)
            counter3 += 1
            position += 1

        elif option == 4 and counter4 < 2:
            insert_special_characters(special_characters, password, position)
            counter4 += 1
            position += 1

        elif counter1 >= 2 and counter2 >= 2 and counter3 >= 2 and counter4 >= 2:
            option = randint(1, 4)

            if option == 1:
                insert_upper_case_letters(
                    uppercase_letters, password, position)
                position += 1

            elif option == 2:
                insert_lower_case_letters(
                    lowercase_letters, password, position)
                position += 1

            elif option == 3:
                insert_numbers(numbers, password, position)
                position += 1

            elif option == 4:
                insert_special_characters(
                    special_characters, password, position)
                position += 1

    password = list_to_string(password)
    store_password(password)


def insert_upper_case_letters(uppercase_letters, password, position):
    elem = randint(0, 25)
    password[position] = uppercase_letters[elem]
    return password


def insert_lower_case_letters(lowercase_letters, password, position):
    elem = randint(0, 25)
    password[position] = lowercase_letters[elem]
    return password


def insert_numbers(numbers, password, position):
    elem = randint(0, 9)
    password[position] = numbers[elem]
    return password


def insert_special_characters(special_characters, password, position):
    elem = randint(0, 16)
    password[position] = special_characters[elem]
    return password


def list_to_string(password):
    string = ""

    for ele in password:
        string += ele

    return string


def store_password(password):
    print('====================================')
    record_name = str(input('Record Name: ')).upper()
    login = str(input('Login: '))

    with open('data.txt', 'a') as file:
        file.write(
            f'Record Name: {record_name} \nLogin: {login} \nPassword: {password} \n')
        file.write('====================================\n')

    sleep(0.5)


def add_record():
    password = str(input('Password: '))
    store_password(password)


def edit_record(): # TODO: Rewrite this function, to not use delete_record.
    delete_record()
    print('====================================')
    option()


def option():
    choose = int(
        input('1- Auto Generated Password \n2- Type your own password \nChoose:'))
    if choose == 1:
        data()

    elif choose == 2:
        add_record()

    else:
        print('Invalid option!')
        choose = 0
        option()

    
def delete_record():
    record_name = str(
        input('Enter the name of the record to be deleted: ')).upper()
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

def fail_msg():
    messagebox.showinfo("Delete Record", "Record not found!")


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
