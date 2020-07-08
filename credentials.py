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
    def delete_credentials(cls, account_type):
        for index, xxx in enumerate(cls.credential_list):
            print(f" From loop: {xxx.account_type}, from user: {account_type}")
            if xxx.account_type == account_type:
                Credentials.credential_list.pop(index)
            else:    
                print("Credentials not found")
            return Credentials.credential_list    
            # else:
            #     print("Credentials not found")
            #     return "Credentials not found!"