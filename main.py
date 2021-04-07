from colorama import init
from colorama import Fore, Back, Style
from functions import *

init()

phonebook = read_file()
while True :

    print(Back.CYAN)
    print(Fore.BLACK)
    print(
        '''
Select what you want to do with phonebook:
1. Add user
2. Delete user
3. Update user
4. Search user
5. Print phonebook
0. Exit'''
    )

    user_kod = input('Your choice?: ')
    print()  # print bool string

    # execution for user command
    if user_kod == '1' :
        add_user(phonebook)
    elif user_kod == '2' :
        delete_user(phonebook)
    elif user_kod == '3' :
        update_user(phonebook)
    elif user_kod == '4' :
        search_user(phonebook)
    elif user_kod == '5' :
        print_phonebook(phonebook)
    else :
        write_file(phonebook)
        print('Goodbye!')
        input()
        break
