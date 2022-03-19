
class UserSession:

    logindb = None

    def __init__(self):
        self.logindb = dict()
        pass


    def login(self, username):
        self.logindb["username"] = username
        return True

    def setup_or_logout(self):
        self.logindb["username"] = None
        return True

    def check_login(self):
        if self.logindb["username"]:
            return True
        else:
            print(self.logindb["username"])
            return False
