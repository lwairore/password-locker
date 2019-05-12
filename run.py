#!/usr/bin/env python3.6
"""
#! shebang line determines the script's ability to be executed like an
standalone executable without typing python3.6
beforehand in the terminal.
"""
from credentials import Credentials
from user import User
import getpass
import random
import time
import string


def create_new_credential(user_name, account_name, password):
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
    password_locker_username = input(
        "What user-name would you like to login with? ")
    print(end="\n")
    print("Create Password-Locker Password:")
    print("-" * 31)
    password_locker_login_password = getpass.getpass(
        "...And what password would you like to use? ")
    print("\nConfirm Password-Locker Password:")
    print("-" * 31)
    confirm_password_locker_login_password = getpass.getpass(
        "Please confirm your new password again? ")
    while True:
        if password_locker_login_password != confirm_password_locker_login_password:
            print("PASSWORD MISMATCH. Please confirm your password correctly!")
            confirm_password_locker_login_password = getpass.getpass(
                "Please confirm your new password again? ")
        else:
            print("Password successfully created! ")
            break
    print(end="\n")
    print("Account successfully created! Kindly, now login with \"lg\" shortcode.")
    short_code = input(
        "Almost there...Login shortcode \"lg\" - login \n ===>").lower()
    print(end="\n")
    if short_code == "lg" or login_short_code == "login":
        print("LOGIN")
        print("-" * 5)
        print("Username:")
        print("-" * 8)
        login_username = input("Please enter your Password-Locker username: ")
        login_password = getpass.getpass(
            "Please enter your Password-Locker password: ")
        while True:
            if (password_locker_username != login_username) or (password_locker_login_password != login_password):
                print("Incorrect username or password! ")
                login_username = input(
                    "Please enter your Password-Locker username again: ")
                login_password = getpass.getpass(
                    "Please enter your Password-Locker password again: ")
            else:
                print("Logging in...")
                break

        print(end="\n")
        short_code = input(
            "You can access: credentials via \"sc\" ==> ").lower()
        print(end="\n")
        if short_code == "sc":
            while True:
                print("CREDENTIALS")
                print("-" * 10)
                credential_short_code = input(
                    "To navigate through your credentials use the following short codes: \n cc - add new credential \n dc - display credentials \n delc - delete credential \n fc - find credential \n cp - copy credentials: \n ==> ").lower()
                if credential_short_code == "cc":
                    print(end="\n")
                    print("ADD NEW CREDENTIAL")
                    account_short_code = input(
                        "Is the account credentials arleady existing: \n y - for already exists \n n - new account credentials \n ==> ").lower()
                    if account_short_code == "y":
                        credential_account_name = input(
                            "What is the name of the account you want to add? ")
                        credential_user_name = input(
                            "What user-name do you use on {}? ".format(credential_account_name))
                        credential_password = input(
                            "What password do you use on {}? ".format(credential_account_name))
                        
                    else:
                        credential_account_name = input(
                            "What is the name of the account? ")
                        credential_user_name = input(
                            "What user-name do you want to use on {}? ".format(credential_account_name))
                        password_auto_generate_option = input(
                            "Would you like to have your password auto-generated? y/n: ").lower()
                        if password_auto_generate_option == "n":
                            password = input("Please enter your password: ")
                        else:
                            password_characters = input(
                                "Select password charcters: \n n - Password to purely contain numbers \n m - Alpha-numerics password \n ===> ").lower()
                            if password_characters == "n":
                                password_length = input(
                                    "What length of password would you like to have? ")
                                random_password = []
                                for i in range(0, int(password_length)):
                                    random_password.append(
                                        random.randint(0, 9))

                                def furnish(random_password):
                                    s = [str(i) for i in random_password]
                                    generated_password = int("".join(s))
                                    return generated_password
                                print(end="\n")
                                print("Your auto-generated numeric password of length {} is: {}".format(
                                    password_length, furnish(random_password)))
                                credential_password = furnish(random_password)
                            else:
                                alphabet = string.ascii_letters + string.digits
                                password_length = input(
                                    "What length of password would you like to have? ")
                                print("Setting up your password length...")
                                time.sleep(2)
                                password = "".join(random.choice(alphabet)for i in range(int(password_length)))
                                print("Generating password...")
                                time.sleep(.300)
                                print("Displaying password...")
                                time.sleep(.300)
                                print("Your auto-generated alpha-numeric password of length {} is:  {}".format(
                                    password_length, password))
                                credential_password = password
                    save_option = input(
                        "Would you like to add {}? y/n ".format(credential_account_name)).lower()
                    if save_option == "y":
                        save_new_credential(create_new_credential(
                            credential_user_name, credential_account_name, credential_password))
                        print("--" * 10)
                        print("{} account has been successfully saved!".format(
                            credential_account_name))
                    else:
                        print("{} account has been discarded. Switching to home.".format(
                            credential_account_name))

                elif credential_short_code == "dc":
                    print(end="\n")
                    if display_credentials():
                        print("List of your credentials: ")
                        print("-" * 28)
                        for credential in display_credentials():
                            print("Account-name: {}".format(credential.account_name))
                            print("Username    : {}".format(credential.user_name))
                            print("Password    : {}".format(credential.password))
                    else: 
                        print("You don't seem to have any credentials saved!")    
                elif credential_short_code == "fc":
                    print(end="\n")
                    print("FIND ACCOUNT DETAILS")
                    print("-" * 20)
                    search_by_account_name = input("Please enter the account you want to search for: \n ===> ")
                    if credential_exist(search_by_account_name):
                        found_credential = find_credential(search_by_account_name)
                        print("Search results")
                        print("*" * 15)
                        print("Account-name: {}".format(found_credential.account_name))
                        print("User-name   : {}".format(found_credential.user_name))
                        print("Password    : {}".format(found_credential.password))
                        print(end="\n")
                    else:
                        print("{} account does not exist! Are you sure you typed the account-name correctly?".format(search_by_account_name))
                elif credential_short_code == "cp":
                    print(end="\n") 
                    select_account_name = input("Please enter account-name to copy it's details? ")
                    if credential_exist(select_account_name):
                        copy_choices = input("What would you like to copy from {}? \n pd - password \n us - user-name \n ac - account-name \n ===> ".format(select_account_name)).lower()
                        if copy_choices == "us":
                            copy_user_name(select_account_name)
                            print("Usename successfully copied to the clipboard!")
                            print(end="\n")
                        elif copy_choices == "pd":
                            copy_password(select_account_name)
                            print("Password successfully copied to the clipboard!")
                            print(end="\n")
                        elif copy_choices == "ac":
                            copy_account_name(select_account_name)
                            print("Account-name successfully copied to the clipboard!")
                            print(end="\n")
                        else:
                            print("Option does not exist!")
                            print(end="\n")
                    else: 
                        print("{} account does not exist in your credentials!".format(select_account_name))
                        print(end="\n")
                        


    print(end="\n")


if __name__ == "__main__":
    """
    Only executes main() function if this module has not 
    been imported.
    """
    main()
