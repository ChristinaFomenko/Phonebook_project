from colorama import init
from colorama import Fore, Back, Style
import os
import csv

init()


def add_user(dictionary: dict) :
    print(Fore.BLACK)
    print(Back.YELLOW)
    name = input('Enter name for abonent: ')
    phone = input('Enter phone number for abonent: ')
    if name in dictionary :
        print(Fore.BLACK)
        print(Back.GREEN)
        print('This abonent already exist: Name: {} - Phone: {}'.format(name, dictionary[name]))
    else :
        dictionary[name] = phone
        print('New abonent "{}" is created'.format(name))
    return dictionary


def delete_user(dictionary: dict) :
    print(Fore.BLACK)
    print(Back.YELLOW)
    name = input('Enter name for abonent: ')
    if name in dictionary :
        dictionary.pop(name)
        print(Fore.BLACK)
        print(Back.RED)
        print('Abonent "{}" is deleted'.format(name))
    else :
        print('Sorry, this abonent not exist')
    return dictionary


def update_user(dictionary: dict) :
    name = input('Enter name for abonent: ')
    phone = input('Enter New phone number for abonent: ')
    if name in dictionary :
        dictionary[name] = phone
        print(Fore.BLACK)
        print(Back.GREEN)
        print('Abonent "{}" is updated'.format(name))
    else :
        print('Sorry, this abonent not exist')
    return dictionary


def search_user(dictionary: dict) :
    print(Fore.BLACK)
    print(Back.YELLOW)
    search_value = input('Enter name or phone number for abonent: ')
    name_in_dict = False
    for key, value in dictionary.items() :
        if key.lower() == search_value.lower() or value == search_value :
            print(Back.YELLOW)
            print(Fore.BLACK)
            print('Name: "{}" - Number: "{}"'.format(key, value))
            name_in_dict = True
            return dictionary
        if name_in_dict == False :
            print('Sorry, this abonent not exist')
        return dictionary


def print_phonebook(dictionary: dict) :
    print(Back.GREEN)
    print(Fore.BLACK)
    for key, value in dictionary.items() :
        print('Phonebook Numbers: ' + '\n' + 'Name: "{}" - Number: "{}"'.format(key, value))
    return dictionary


def read_file() :
    check_file = os.path.exists('./phonebook.txt')
    if check_file is True :
        with open('phonebook.txt') as file :
            phonebook_from_file = csv.reader(file, delimiter=",")
            phonebook = {}
            for abonent in phonebook_from_file :
                if len(abonent) > 0 :
                    phonebook[abonent[0]] = abonent[1]
        return phonebook
    else :
        return dict()


def write_file(dictionary: dict) :
    with open('phonebook.txt', 'w') as file :
        writing_file = csv.writer(file)
        for name, number in dictionary.items() :
            writing_file.writerow([name, number])
            print(name, number)