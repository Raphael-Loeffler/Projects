#What is a strong password:
#-at least 12 characters - Done
#-Letters (a - A) - Done
#-Numbers(0-9) - Done
#-TODO: does not repeat characters

def check_str(main_string: str, search_string: str) -> bool:
    #Checks if theres at least one character from search_string in main_string
    contains: bool = False
    for c in main_string:
        for s in search_string:
            if c == s:
                contains = True
                exit
    return contains
"""
def check_if_repeats_recursive(password: str) -> bool:
    if len(password) < 2:
        return False
    elif password[:int(len(password)/2)] == password[int(len(password)/2):]:
        return True
    else:
        return check_if_repeats(password[:int(len(password)/2)]) or check_if_repeats(password[int(len(password)/2):])
"""

def check_if_repeats(password: str) -> bool:
    ...

def all_types_present(password: str) -> bool:
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "\"~``!@}#$%^&*()_-+={|[]:';<>,./?\""
    return check_str(password, special_characters) and check_str(password, lower_case_letters) and check_str(password, upper_case_letters) and check_str(password, numbers)

class Check_password_strength:
    def __init__(self, password):
        self.password: str = password
    
    def check_strength(self) -> str:
        if not len(self.password) > 11:
            return "The password is too short."
        if not all_types_present(self.password):
            return "The password needs to contain upper and lowercase letters, as well as numbers and special characters."
        return "The password is strong."

def main():
    password_strength_checker = Check_password_strength("")
    print(password_strength_checker.check_strength())

if __name__ == "__main__":
    #main()
    ...