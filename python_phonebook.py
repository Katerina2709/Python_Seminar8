# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os
import shutil

FILE_PATH = 'phone_book1.txt'

# def full_write ():
#     with open(FILE_PATH, 'w', encoding = 'utf-8') as phonebook:
#         phonebook.write ('Андреев Александр Алексеевич 915-67-87\n')
#         phonebook.write ('Борисов Олег Константинович 921-54-83\n')
#         phonebook.write ('Валеев Петр Николаевич 922-09-13\n')

# full_write()

def full_read ():
    with open(FILE_PATH, 'r', encoding = 'utf-8') as phonebook:
        for line in phonebook:
            print(line.strip())

def add_new_contact ():
    with open(FILE_PATH, 'a', encoding = 'utf-8') as phonebook:
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ') 
        father_name = input('Введите отчество: ') 
        phone_number = input('Введите номер телефона: ') 
        phonebook.write(surname + ' ' + name + ' ' + father_name + ' ' + phone_number + '\n')
        print(f'\nДобавлена запись : {surname} {name} {father_name} {phone_number}\n')

def search_contact ():
    with open(FILE_PATH, 'r', encoding = 'utf-8') as phonebook:
        search_str = input('\nЧто ищем? ')
        for line in phonebook:
            if search_str in line:
                print(line.strip() + '\n')

def edit_contact ():
    with open(FILE_PATH, 'r', encoding = 'utf-8') as phonebook:
        phone_book = phonebook.readlines()
        for line in enumerate(phone_book):
             print(*line)  
        number = int(input("Введите номер контакта для редактирования: "))
        old = phone_book[number]
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ') 
        father_name = input('Введите отчество: ') 
        phone_number = input('Введите номер телефона: ') 
        phone_book[number] = ' '.join([surname, name, father_name, phone_number, '\b\n'])
        print(f'\nЗапись - {old} изменена на - {phone_book[number]}')
        with open(FILE_PATH, 'w', encoding = 'utf-8') as phonebook1:
            phonebook1.write(''.join(phone_book))

def delete_contact ():
    with open(FILE_PATH, 'r', encoding = 'utf-8') as phonebook:
        phone_book = phonebook.readlines()
        for line in enumerate(phone_book):
             print(*line)  
        number = int(input("Введите номер контакта, который будет удален: "))
        old_contact = phone_book.pop(number)
        print(f'\nЗапись - {old_contact} удалена')
        with open(FILE_PATH, 'w', encoding = 'utf-8') as phonebook1:
            phonebook1.write(''.join(phone_book))

def main_menu():
    print ('\n1 Показать все контакты') 
    print ('2 Добавить новый контакт') 
    print ('3 Найти контакт') 
    print ('4 Редактировать') 
    print ('5 Удалить контакт') 
    print ('6 Выход')
    return int(input('\nВыберите действие (номер): '))

while (choice_number := main_menu()) != 6:
    match choice_number:
        case 1:
            full_read()
        case 2:
            add_new_contact()
        case 3:
            search_contact()   
        case 4:
            edit_contact()
        case 5:
            delete_contact()     
        case 6:
            break
        case _:
            break
            
   
            



 


#