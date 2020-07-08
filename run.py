#!/usr/bin/env python3.6
import string
import random

from user import User
from credentials import Credentials

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
def create_user(first,last,email):
    '''
    Function to create a new password
    '''

    new_user = User(first,last,email)
    return new_user

def save_user(user):
    '''
    Function saves user details
    '''
    
    user.save_user()

def create_credentials(user_name,password,account_type):
    '''
    Function to create a new credentials
    '''

    new_credentials = Credentials(user_name, password, account_type)
    return new_credentials


def save_credentials(credentials):
    '''
    Function saves user credentials
    '''

    credentials.save_credentials()

# def display_user_cred():

# def del_user_cred():



def main():
    print("Welcome to password locker.")


    while True:

        print("Use these short codes : cu - create a new user, cc - create user credentials, dc - display user credentials, dl - delete user, exit -exit the user list ")

        short_code = input().lower()

        if short_code == "exit":
            print("Adios...")
            break

        if short_code == "cu":
            print("create user")

            print("First name")
            first_name = input()

            print("Last name")
            last_name = input()
            
            print("Email")
            email = input()

            save_user(create_user(first_name,last_name, email))
            print ('\n')
            print(f"New user {first_name} {last_name} created")
            print('\n')

        elif short_code == 'cc':
                
            print("create credentials")

            print("account_type")
            account_type = input()

            print("user name")
            user_name = input()

            print("Enter password")
            password = input()

            save_credentials(create_credentials(user_name,password,account_type))
            print('\n')
            print(f"New credentials {account_type} {user_name} {password} ")
            



if __name__ == '__main__':
    main()    