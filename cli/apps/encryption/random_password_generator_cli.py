from random import shuffle, choice
from string import ascii_letters, digits, punctuation


def generate_password(length: int) -> str:
  characters: list = list(ascii_letters + digits + punctuation)
  shuffle(characters)
  password_list: list = [choice(characters) for _ in range(length)]
  return "".join(password_list)

def run() -> str:
  length: int = int(input("Password length: "))
  password: str = ""
  if length > 0:
    return generate_password(length)
  return "Only positive password length is accepted"


if __name__ == "__main__":
  password = run()
  print(f"{password=}")