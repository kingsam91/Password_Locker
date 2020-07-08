import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        initiates test initial data before they're run
        '''

        self.create_user = User("Sam", "King", "sam@gmail.com")

    # def tearDown(self):
    #     '''
    #     hfkjdhfjkfhjkhjk
    #     '''

    #     User.user_list = []    

    def test_init(self):
        '''
        Test if initialized objects are equal
        '''

        self.assertEqual(self.create_user.first, "Sam")
        self.assertEqual(self.create_user.last, "King")
        self.assertEqual(self.create_user.email, "sam@gmail.com")

if __name__ == '__main__':
    unittest.main()            