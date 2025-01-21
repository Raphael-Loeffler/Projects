"""
What is a strong password:
-at least 6 characters... -> read about it
-Letters (a - A)
-Numbers(0-9)
-does not repeat characters
"""

class Check_password_strength:
    def __init__(self):
        self.password: str = ""
        self.lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    
    def check_strength(self, password: str) -> str:
        if (any(c in self.password for c in self.lower_case_letters)):
            return "passed"
        else:
            return "hund"

def main():
    password_strength_checker = Check_password_strength()
    print(password_strength_checker.check_strength("abc"))

if __name__ == "__main__":
    main()