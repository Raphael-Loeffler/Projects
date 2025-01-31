#What is a strong password:
#-at least 12 characters - Done
#-Letters (a - A) - Done
#-Numbers(0-9) - Done
#-Special characters - Done
#-does not repeat characters - Done

class Password_Strength_Checker:
    def __init__(self):
        self.password: str = input("Input the password to check: ")
    
    def check_if_repeats(self, password: str) -> bool:
        for size in range(3, int(len(password)/2)+1):
            for index in range(len(password) - size * 2 + 1):
                if password[index : index + size] == password[index + size : index + size * 2]:
                    return True
        return False
    
    def all_types_present(self, password: str) -> bool:
        lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
        upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_characters = "~``!@}#$%^&*()_-+={|[]:';<>,./?"
        return self.check_str(password, special_characters) and self.check_str(password, lower_case_letters) and self.check_str(password, upper_case_letters) and self.check_str(password, numbers)
    
    def check_str(self, main_string: str, search_string: str) -> bool:
        #Checks if theres at least one character from search_string in main_string
        contains: bool = False
        for c in main_string:
            for s in search_string:
                if c == s:
                    contains = True
                    exit
        return contains
    
    def check_strength(self) -> str:
        if not len(self.password) > 11:
            return "The password is too short."
        if not self.all_types_present(self.password):
            return "The password needs to contain upper and lowercase letters, as well as numbers and special characters."
        if self.check_if_repeats(self.password):
            return "The password should not repeat."
        return "The password is strong."

def run():
    password_strength_checker = Check_password_strength()
    print(password_strength_checker.check_strength())

if __name__ == "__main__":
    run()