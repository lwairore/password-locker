import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    
    """
    Define a TestCredentials subclass that inherits properties and behaviours from
    unittest.TestCase superclass above.
    Below, define a setUp() method that instantiates new_credentials
    instance of class Credentials before any tests can be run
    """

    def setUp(self):
        self.creadentials_test = Credentials("lwairore", "Yahoo", "4280")



    