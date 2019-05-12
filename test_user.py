import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    This class tests only initialization method of User classs
    """

    def setUp(self):
        """
        This method simply preinitializes new_user instance befor
        any test can be run.
        """
        self.new_user = User("john", "8754lope")

    def tearDown(self):
        """
        This method empties users class variable of class User.
        """
        User.users = []

    def test_init(self):
        """
        This method does the actually asserting by checking for equality
        between the value of name and login_password keys with the expeted values.
        """
        self.assertEqual(self.new_user.name, "john")
        self.assertEqual(self.new_user.login_password, "8754lope")


if __name__ == "__main__":
    """
    Checks if where this module is ran. Executes the module if it's 
    run as main.
    """
    unittest.main()