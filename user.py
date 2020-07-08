class User:

    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self, first,last,email):
        self.first = first
        self.last = last
        self.email = email

    def save_user(self):
        """
        save_contact method saves contact objects into user_list
        """

        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the class list
        """

        return cls.user_list