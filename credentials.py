class Credential:
    """
    a class to generate credential for users
    """
    pass
    credential_list = []

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credentials(self):
        """
        save_contact method saves credentials objects into credential list
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list