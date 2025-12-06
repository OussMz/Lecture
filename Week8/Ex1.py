import bcrypt
import logging
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, "user_act_from_Ex1.log")

user_logger = logging.getLogger("user_logger")
user_logger.setLevel(logging.INFO)
user_file_handler = logging.FileHandler(log_path, mode="w")
user_file_handler.setLevel(logging.INFO)
user_file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
user_logger.addHandler(user_file_handler)

# user_logger = logging.getLogger("user_logger")
# user_logger.setLevel(logging.INFO)
# user_handler = logging.FileHandler("user_activity.log", mode="w")
# user_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
# user_logger.addHandler(user_handler)

class User:
    def __init__(self, username, password, privilege_level):
        self._username = username
        self.__password = password
        self.__hashed_password = self.hash_calculator(self.__password)
        self.authenticated = False
        self.__privilege_level = privilege_level
        self.__login_attempts_left = 3
        self.account_status = "active"

    @property 
    def username(self):
        if self.authenticated:
            return self._username
        else:
            user_logger.warning("Attempt to view username without authentication.")

    @username.setter
    def username(self, name):
        if self.authenticated:
            self._username = name
            user_logger.info(f"Username changed to '{self._username}'.")
            print(f"Username changed to '{self._username}'.")
        else:
            user_logger.warning(f"Attempt to change username without authentication.")
            print("Attempt to change username without authentication.")
    @property
    def password(self):
        user_logger.warning(f"Attempt to view password which is not allowed.")
        return "Attempt to view password which is not allowed."
    
    @password.setter
    def password(self, new_password):
        if self.authenticated:
            self.__password = new_password
            self.__hashed_password = self.hash_calculator(self.__password)
            user_logger.info(f"Password changed for user '{self._username}'.")
            print(f"Password changed for user '{self._username}'.")
        else:
            user_logger.warning(f"Attempt to change password without authentication.")
            print("Attempt to change password without authentication.")
        
    @property
    def privilege_level(self):
        if self.authenticated:
            return self.__privilege_level
        else:
            user_logger.warning(f"Attempt to view privilege level without authentication.")
            print("Attempt to view privilege level without authentication.")

    @privilege_level.setter
    def privilege_level(self, level):
        user_logger.warning(f"Attempt to change privilege level to {level} which is not allowed.")
        print(f"Attempt to change privilege level to {level} which is not allowed.")

    def hash_calculator(self, entered_password):
        encoded_password = entered_password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        return hashed_password
    
    def verify_password(self, entered_password):
        return bcrypt.checkpw(entered_password.encode(), self.__hashed_password)
    
    def authenticate(self, username, entered_password):
        if self.account_status == "locked":
            user_logger.warning(f"The account of '{self._username}' is locked due to many attempted logins.")
            print(f"Your account is locked '{self._username}' due to many attempted logins.")
        else:
            if username == self._username and self.verify_password(entered_password):
                self.authenticated = True
                user_logger.info(f"User '{self._username}' logged in successfully.")
                print(f"You logged in successfully {self._username}!")
                self.__reset_login_attempts()
            else:
                self.__login_attempts_left -= 1
                if self.__login_attempts_left == 0:
                    self.__lock_account()
                    user_logger.warning(f"Your account '{self._username}' is locked due to multiple failed login attempts.")
                    print(f"Your account '{self._username}' is locked due to multiple failed login attempts.")
                else:
                    user_logger.warning(f"Authentication failed '{self._username}', {self.__login_attempts_left} attempt(s) left.")
                    print(f"Authentication failed '{self._username}', {self.__login_attempts_left} attempt(s) left.")

    def display_info(self):
        if self.authenticated:
            print(f"Username: {self._username}, Privilege Level: {self.__privilege_level}, Account Status: {self.account_status}")
        else:
            user_logger.warning(f"Attempt to display user info without authentication.")
            print("User not authenticated. Cannot display info.")
    def __lock_account(self):
        self.account_status = "locked"
    def __reset_login_attempts(self):
        self.__login_attempts_left = 0





