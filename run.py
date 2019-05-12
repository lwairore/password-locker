#!usr/bin/env python3.6
"""
#! shebang line determines the script's ability to be executed like an
standalone executable without typing python3.6
beforehand in the terminal.
"""
from credentials import Credentials
from user import User


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
    return Credentials.copy_account_name(account_name)

    


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
