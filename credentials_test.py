import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        initiates initial data before they're run
        '''

        self.create_credentials = Credentials("kingsam", "1234567", "facebook")

    def test_init(self):
        '''
        Test if initialized objects are equal and properly initialized
        '''

        self.assertEqual(self.create_credentials.user_name, "kingsam")
        self.assertEqual(self.create_credentials.password, "1234567")
        self.assertEqual(self.create_credentials.account_type, "facebook")

if __name__ == '__main__':
    unittest.main()            