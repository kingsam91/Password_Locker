class Credentials:
    '''
    Class to generate credential for users
    '''
    
    credential_list = []

    def __init__(self, user_name, password, account_type):
        self.user_name = user_name
        self.password = password
        self.account_type = account_type

    def save_credentials(self):
        """
        save_contact method saves credentials objects into credential list
        """
        Credentials.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list

    @classmethod
    def delete_password(cls, username):
        for index, password in enumerate(cls.user_list):
            if password.username == username:
                print(index)
                return Password.user_list.pop(index)
            else:
                print("Username not found")
                return "Username not found!"