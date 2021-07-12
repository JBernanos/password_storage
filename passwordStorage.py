import sys
from tkinter import *
from random import randint
from time import sleep

root = Tk()
root.title('Password Storage')
"""
    Just a simple menu, where user choose what to do.
"""


def menu():
    # try:
    #     option = int(input('==================================== \n1- NEW RECORD(AUTO GENERATED PASSWORD) \n2- NEW RECORD \n3- EDIT A RECORD \n4- DELETE A RECORD \n5- CONSULT YOUR RECORDS \n6- QUIT \nCHOOSE ONE OPTION: '))
    #     print('====================================')

    #     if option == 1:
    #         data()

    #     elif option == 2:
    #         add_record()

    #     elif option == 3:
    #         edit_record()

    #     elif option == 4:
    #         marker = 0  # this variable name need to be changed
    #         delete_record(marker)

    #     elif option == 5:
    #         show_records()

    #     elif option == 6:
    #         print('Shutting the program down, wait a second.')
    #         sleep(0.5)

    #     else:
    #         print('ERROR')
    #         menu()

    # except ValueError:
    #     print('Incorrect input, you will be redirected to menu.')
    #     sleep(0.5)
    #     menu()

    print('==================================== \n1- NEW RECORD(AUTO GENERATED PASSWORD) \n2- NEW RECORD' 
    '\n3- EDIT A RECORD \n4- DELETE A RECORD \n5- CONSULT YOUR RECORDS \n6- QUIT \nCHOOSE ONE OPTION: ')
    print('====================================')


"""
    In data() we have the data needed to create the password.
"""
def data():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = [
        '!', '?', '{', '[', '(', '}', ']', ')', '.', ',', '<', '>', '-', '+', '=', '*', '/']
    password, length = password_length()
    create_password(uppercase_letters, lowercase_letters, numbers,
                    special_characters, password, length)


"""
    In password_length() user enter the password length, this function force the length be greater than 8.
"""
def password_length():
    try:
        length = int(input('Choose the length for your password: '))

        if length < 8:
            print('The length of your password should be greater then 8.')
            password_length()

        else:
            password = ['0'] * length
            return password, length

    except ValueError:
        print('Incorrect input, you will be redirected to menu.')
        sleep(0.5)
        menu()


"""
    In create_password() a random password is generated, the password should have at least 2 values from each data type defined on data(), this validation is made by the counters(1~4).
    TODO: position variable should be increased inside the "insert" functions
"""
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


"""
    In list_to_string() the array is converted into a string(function avaliable in: https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/).
"""
def list_to_string(password):
    string = ""

    for ele in password:
        string += ele

    return string


"""
    In store_password() user will choose the record name and a login, after that we store all the data into a txt file(data.txt). 
"""
def store_password(password):
    print('====================================')
    record_name = str(input('Record Name: ')).upper()
    login = str(input('Login: '))

    with open('data.txt', 'a') as file:
        file.write(
            f'Record Name: {record_name} \nLogin: {login} \nPassword: {password} \n')
        file.write('====================================\n')

    sleep(0.5)
    menu()


"""
    The add_record() function is used to storage a record that is already created, the user need to enter a password, after that the function store_password() is called.
"""
def add_record():
    password = str(input('Password: '))
    store_password(password)


"""
    In edit_record() the record choosed by the user will be deleted, after that the option function is called.
"""
def edit_record():
    marker = 1  # this variable name need to be changed
    delete_record(marker)
    print('====================================')
    option()


"""
    In this function user choose between a AGP or his own password.
"""
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


"""
    In delete_record() user will choose the record to be deleted, and this record will be removed from data.txt.
"""
def delete_record(marker):
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
        print('Record successfully removed!')

    else:
        print('Record not found!')
        menu()

    if marker == 0:
        menu()


"""
    This function name and idea need to be rethought, the marker variable indicates if when delete_record is called
    the program needs to delete and edit that record or just delete it.
"""
def only_delete_record(): 
    marker = 0
    delete_record(marker)

"""
    In show_records() we show all the records in data.txt file to the user.
"""
def show_records():
    with open('data.txt', 'r') as file:
        print(file.read())

    sleep(0.5)
    menu()


"""
    In this function the Tkinter root will be closed, and the program will shut down.
"""
def exit_program():
    root.quit()
    print('\nShutting the program down, wait a second.')
    sleep(0.5)
    sys.exit()


# Defining the tkinter buttons
new_record_apg_btn = Button(root, text="NEW RECORD(APG)", command=data, padx=20, pady=10).grid(row=0, column=0)

new_record_btn = Button(root, text="NEW RECORD", command=add_record, padx=20, pady=10).grid(row=1, column=0)

edit_record_btn = Button(root, text="EDIT RECORD", command=edit_record, padx=20, pady=10).grid(row=2, column=0)

delete_record_btn = Button(root, text="DELETE RECORD", command=only_delete_record, padx=20, pady=10).grid(row=3, column=0)

show_record_btn = Button(root, text="SHOW RECORDS", command=show_records, padx=20, pady=10).grid(row=4, column=0)

exit_program_btn = Button(root, text="EXIT PROGRAM", command=exit_program, padx=20, pady=10).grid(row=5, column=10)

menu()

root.mainloop()
