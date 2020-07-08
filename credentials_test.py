import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        initiates initial data before they're run
        '''

        self.create_credentials = Credentials("kingsam", "1234567", "facebook")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run.
        '''

        Credentials.credential_list = []

    def test_save_credentials(self):
        '''
        tests saving new credentials 
        '''
        self.create_credentials.save_credentials()  
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_display_credentials(self):
        '''
        test case to see if app appends credentials list
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_list)

    def test_delete_credentials(self):
        '''
        test if one can delete credentials
        '''
        self.create_credentials.save_credentials()
        create_credentials = Credentials("Test","user","facebook") # new contact
        create_credentials.save_credentials()

        self.create_credentials.delete_credentials("facebook")# Deleting a contact object
        self.assertEqual(len(Credentials.credential_list),1)


    def test_init(self):
        '''
        Test if initialized objects are equal and properly initialized
        '''

        self.assertEqual(self.create_credentials.user_name, "kingsam")
        self.assertEqual(self.create_credentials.password, "1234567")
        self.assertEqual(self.create_credentials.account_type, "facebook")

   

if __name__ == '__main__':
    unittest.main()            