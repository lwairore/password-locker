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
        self.credentials_test = Credentials("lwairore", "Yahoo", "4280")

    def tearDown(self):
        """
        tearDown() method will empty credentials class variable after every 
        test.
        """
        Credentials.credentials = []

    def test_save_individual_credential(self):
        """
        This method will take take in an instance that 
        it will later on use that instance to call save_credential() method
        that will also pass in that instance as self.Finally, these method
        will use assertEqual to assertain if the length of credentials class variable is
        equal to one(1)        
        """
        self.credentials_test.save_credential()
        self.assertEqual(len(Credentials.credentials), 1)

    def test_save_multiple_credentials(self):
        """
        This method test to assertain if a save_credential() method can
        save append multiple instances to Credential's class variable by comparing it's actual
        length to assertain if it's equal to three(3)
        This method takes in an instance.
        """
        self.credentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        self.assertEqual(len(Credentials.credentials), 3)

    def test_delete_individual_credential(self):
        """
        This method tests to check if delete_credential if called on specific
        instance is capable of removing that instance from credentials class variable list
        """
        self.credentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        test_sharon_credential.delete_individual_credential()
        self.assertEqual(len(Credentials.credentials), 2)

    def test_delete_all_credentials(self):
        """
        This method tests to see if by calling delete_multiple_credentials()
        method does empty the class variable, credentials
        """
        self.credentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        test_sharon_credential.delete_all_credentials()
        self.assertEqual(len(Credentials.credentials), 0)
    
    def test_find_credential_by_account_name(self):
        """
        This method attempts to search credentials detail via accountname.
        """
        self.credentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        found_credential = Credentials.find_account_name("Gmail")
        self.assertEqual(found_credential.account_name, test_sharon_credential.account_name)

    def test_credential_exist(self):
        """
        This method takes in account-name and searches in 
        the class variable credentials of Credentials class and returns a bool value true if it
        exists and False if it doesn't exist
        """
        self.credentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        credential_exists = Credentials.credential_exists("Bingo")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        """
        This method calls save_credential() method on; credentials_test, test_lucas_credential,test_sharon_credential
        and asserts the return value returnedby calling display_credentials() class method is the same value
        with that that is contained on credentials class variable
        """
        self.credentials_test.save_credential()
        test_lucas_credential = Credentials("Lucas Abraham", "Bingo", "0712")
        test_lucas_credential.save_credential()
        test_sharon_credential = Credentials("Sharoon", "Gmail", "8901")
        test_sharon_credential.save_credential()
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials)



if __name__ == "__main__":
    """
    Checks if this file is being run as the main file
    or has been imported.
    """
    unittest.main()
