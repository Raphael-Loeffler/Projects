from random import choice
from string import ascii_uppercase

# TODO: Expand words list...
# TODO: Debug line 25 - 35

# TODO: in webbrowser_cli.py
# TODO: EXERCISES:
# TODO: 1. Get an input
# TODO: 2. Create an -html file. For example for input 'www.google.com' -> google.html


LIVES: int = 5
WORDS: list[str] = ["Simon", "Raphael", "Michalis", "Tina"]

def get_word(words: list[str]) -> str:
  word: str = choice(words)
  return word

def play() -> None:
  print("<explanation>")
  word: str = get_word(WORDS)
  letters_word: set[str] = set(word)
  abc: set[str] = set(ascii_uppercase)
  used_letters: set[str] = set()
  lives: int = LIVES
  
  while lives > 0 and len(letters_word) > 0:
    print(f"Lives: {lives}")
    print(f"Letters used: {''.join(used_letters)}")
    word_list_print: list[str] = [letter if letter in used_letters else '_' for letter in word]
    print(f"Word {' '.join(word_list_print)}\n")
    user_letter: str = input("Guess a letter: ").upper()
    if user_letter in abc - used_letters:
      used_letters.add(user_letter)
      if user_letter in letters_word:
        letters_word.remove(user_letter)
        print("Correct guess!")
      else:
        lives -= 1
        print("Wrong guess... Try again!")
    elif user_letter in used_letters:
      print("Already used...")
    else:
      print("Invalid character. Try again!")
    print("".join('_ ' for _ in word)+"\n")
  
  if lives == 0:
      print("LOST")
  else:
    print("WIN")


if __name__ == "__main__":
  play()