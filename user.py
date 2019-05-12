class User:
    """
    This class User will primarly act like a firewall
    between the user and their credentials.
    """

    users = []

    def __init__(self, name, login_password):
        """
        Initializes all the required parameters for 
        all users.
        """
