class Credentials:

    """
    Credentials class purely deals with all information such as:
    user;name, account-name, and password before storing them upon user's ,choice.
    This class generates new instances of Credentials that 
    will have: username, account_name, password upon 
    instantiation.
    """
    credentials = []

    def __init__(self, user_name, account_name, password):
        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credential(self):
        """
        This method takes in an instance and appends it
        to the class variable, credentials.
        """
        __class__.credentials.append(self)

    def delete_individual_credential(self):
        """
        This method takes in an instance that it's called on
        and calls in the remove method on class variable, credentials
        with that particular instance passed as a parameter
        """
        __class__.credentials.remove(self)

    def delete_all_credentials(self):
        """
        This method empties the class variable, credentials when it is called.
        """
        __class__.credentials = []

    @classmethod
    def find_account_name(cls, account_name):
        """
        This class method takes in class and account_name.
        This method uses a for loop to loop throught the content of class
        variable, credentials and finally checks if either of the values
        that are returned are equal to account_name passed in.
        """
        for credential in cls.credentials:
            if credential.account_name == account_name:
                return credential


    @classmethod
    def credential_exists(cls, account_name):
        """
        This class method compares the account_name received from an instance 
        with all account_name keys on class variable, credentials.
        Returns a bool value if there is a match, True
        """
        for credential in cls.credentials:
            if credential.account_name == account_name:
                return True

    @classmethod
    def display_credentials(cls):
        return cls.credentials