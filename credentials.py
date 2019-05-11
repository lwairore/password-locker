class Credentials:

    """
    Credentials class purely deals with all information such as:
    user;name, account-name, and password before storing them upon user's ,choice.
    This class generates new instances of Credentials that 
    will have: username, account_name, password upon 
    instantiation.
    """
    def __init__(self, user_name, account_name, password):
        self.user_name = user_name
        self.account_name = account_name
        self.password = password
        