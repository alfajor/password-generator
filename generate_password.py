#!/usr/bin/env python3

import random
import string
import colored
from colored import stylize 

def set_length():
    while True:
        length = input(stylize('Enter a password length: ', colored.fg('green')) )
        try:
            int_value = int(length)
            return int_value
        except ValueError:
            print(stylize('Password length must be a number', colored.fg('red')))

def use_special_chars():
    make_it_special = str(input(stylize('Include special characters and digits? ', colored.fg('yellow')) ))
    special_chars = None

    if make_it_special.lower() == 'yes' or make_it_special.lower() == 'y': 
        special_chars = True 
    else: 
        special_chars = False

    return special_chars

def generate_password():
    password_length = set_length()
    is_special = use_special_chars()

    if is_special:
        result = string.ascii_letters + string.digits + string.punctuation
    else: 
        result = string.ascii_letters

    password = ''.join(random.choice(result) for i in range(password_length))

    print(stylize('\n' + 'Your password is: {}', colored.fg('light_gray')).format(stylize(password, colored.fg('cyan'))) )

    save_pass = str(input(stylize('Would you like to save to a file? ', colored.fg('magenta')) ))
    
    with open('passwords.txt', 'a+') as password_file:
        if save_pass.lower() == 'yes' or save_pass.lower() == 'y':
            print(stylize('\n' + 'SUCCESS! Your password has been saved to passwords.txt. Keep it safe!', colored.fg('orchid')))
            password_file.write(password + '\n')

            password_file.close()

generate_password()





