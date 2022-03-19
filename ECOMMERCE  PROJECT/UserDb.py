

class UserDb:

    def __init__(self):
        self.user_db = dict()

    def add_user(self, username, password):
        if username not in self.user_db.keys():
            self.user_db[username] = password
            print(str(username) + " added successfully!")
        else:
            print("Username already exists. Please choose another username.")

    def is_user(self, username, password):
        if username in self.user_db.keys() and self.user_db[username] == password:
            return True
        else:
            return False
