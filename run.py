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
    
    user.save_user_details()

def create_credentials(user_name,password,email):
    '''
    Function to create a new credentials
    '''

    new_credentials = Credentials(user_name, password, email)
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

        print("Use these short codes : cp - create a new password, dp - display passwords, dl - delete passwords, ex -exit the password list ")

        short_code = input().lower()
        



if __name__ == '__main__':
    main()    