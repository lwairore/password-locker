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

    # def tearDown(self):
    #     User.users = []
