#!/usr/bin/env python3.6
"""
#! shebang line determines the script's ability to be executed like an
standalone executable without typing python3.6
beforehand in the terminal.
"""
from credentials import Credentials
from user import User
import getpass


def create_new_credential(user_name, account_name, passsword):
    """
    This function return a new instance when it is called.
    """
    new_credential = Credentials(user_name, account_name, password)
    return new_credential


def create_new_user(name, login_password):
    """
    This function takes two arguments based on the user inputs;
    name and login_password. 
    Returns new_user instance when called.
    """
    new_user = User(name, login_password)
    return new_user


def save_new_credential(new_credential):
    """
    This function calls save_credential() method of class Credential
    on new_credential instance.
    """
    new_credential.save_credential()


def find_credential(account_name):
    """
    This function takes in one argument, account_name.
    Calls find_account_name() class method of Credential on Credential and passing
    to it account_name argument. 
    Returns an instance of that account_name if the account_name
    matched any account_names on class variable, credentials.
    """
    return Credentials.find_account_name(account_name)


def credential_exist(account_name):
    """
    This function takes in account_name as its argument.
    Calls credential_exist() class method on Credential
    class and takes in account_name as its argument.
    Returns a bool value, True if account_name matches any in 
    class atrribute credentials.
    """
    return Credentials.credential_exists(account_name)


def copy_account_name(account_name):
    """
    This function copies account_name to the clipboard by calling
    copy_account_name() class method and by passing to it the account_name that 
    the user ishes to copy.
    """
    return Credentials.copy_account_name(account_name)


def copy_user_name(account_name):
    """
    This function copies a username of the respective account_name if
    any is found.
    """
    return Credentials.copy_user_name(account_name)


def copy_password(account_name):
    """
    This function copies password of respective account-name.
    """
    return Credentials.copy_password(account_name)


def display_credentials():
    """
    These function calls display_credentials() class method on Credentials.
    These function returns all the instances key values when called.
    """
    return Credentials.display_credentials()


def delete_individual_credential(new_credential):
    """
    This function deletes any new_credential instance that is
    instantiated. By passing the instance to delete_credential() class method of class Credentials.
    Returns a NoneType when called. 
    """
    new_credential.delete_credential()


def delete_all_credentials(new_credential):
    """
    This function deletes all credentials if called.
    Requires atleast one argument new_credential for it to 
    execute.
    """
    new_credential.delete_all_credentials()


def main():
    """ 
    This function contains the main functionality ie. creating user and credentials,\
    deleting credentials, etc.
    """
    print("EVERYONE NEEDS A PASSWORD MANAGER")
    print("_" * 33)
    print("Just above every website wants you to create a user account and log in with a \npassword, from fan-fiction discussion sites to megabanks. When you have a \nhundred or more of these, the human memory can't keep up. One simple \nsolution is to just the simplest words and phrases as passwords, \nsomething associated with the site, like \"mybank\" for your \nonline bank. Another is to gin up just one strong, \ncomplicated password and use it everywhere. We have \na name for folks who rely on either of these two techniques. \nWe call them victims, victims of identity theft. The smart user \ndoesn't fall for either of these traps, instead relying on a password manager \nto create and remember a strong, unique password for every website.\n")
    real_name = input(
        "What name would you like me to call Sir/Madam, can get quite annoying \nme calling you \"user\" each time you login, don't you agree: ")
    if real_name:
        print("--->HELLO, {}. That sounds proper now!".format(real_name))
    else:
        real_name = "User"
        print("--->\"User\" name shall it be!")
    print(end="\n")
    print("CREATE ACCOUNT")
    print("-" * 14)
    print("Please setup with us you Password-Locker inorder for us to 100 percent guarantee you \nthat it will be only you who will only be able to see your credentials.\n")
    print("Create Password-Locker Username:")
    print("-" * 31)
    password_locker_username = input("What user-name would you like to login with? ")
    print(end="\n") 
    print("Create Password-Locker Password:")
    print("-" * 31)
    password_locker_login_password = getpass.getpass("...And what password would you like to use? ")
    print("\nConfirm Password-Locker Password:")
    print("-" * 31)
    confirm_password_locker_login_password = getpass.getpass("Please confirm your new password again? ")
    while True:
        if password_locker_login_password != confirm_password_locker_login_password:
            print("PASSWORD MISMATCH. Please confirm your password correctly!")
            confirm_password_locker_login_password = getpass.getpass("Please confirm your new password again? ")
        else:
            print("Password successfully created! ")
            break 
    print(end="\n")
    print("Account successfully created! Kindly, now login with \"lg\" shortcode.")
    short_code = input("Almost there...Login shortcode \"lg\" - login ").lower()
    print(end="\n")
    if short_code == "lg" or login_short_code == "login":
        print("LOGIN")
        print("-" * 5)
        print("Username:")
        print("-" * 8)
        login_username = input("Please enter your Password-Locker username: ")
        login_password = getpass.getpass("Please enter your Password-Locker password: ")
        while True:
            if (password_locker_username != login_username) or (password_locker_login_password != login_password):
                print("Incorrect username or password! ")
                login_username = input("Please enter your Password-Locker username again: ")
                login_password = getpass.getpass("Please enter your Password-Locker password again: ")
            else:
                print("Logging in...")
                break 

        print(end="\n")
        short_code = input("You can access: credentials via \"sc\" ==> ").lower()
        print(end="\n")
        if short_code == "sc":
           while True:
               print("CREDENTIALS")
               print("-" * 10)
               credential_short_code = input("To navigate through your credentials use the following short codes: \n cc - add new credential \n delc delete credential \n fc - find credential \n cp - copy credentials: \n ==> ").lower()
                              
         


            



    print(end="\n")
    
        
    

if __name__ == "__main__":
    """
    Only executes main() function if this module has not 
    been imported.
    """
    main()
