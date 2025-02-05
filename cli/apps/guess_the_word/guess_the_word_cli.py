from random import choice
from string import ascii_uppercase



LIVES: int = 5
WORDS = [
    "apple", "banana", "orange", "grape", "cherry", "mango", "peach", "lemon", "pear", "plum",
    "table", "chair", "couch", "shelf", "desk", "lamp", "mirror", "window", "door", "carpet",
    "house", "apartment", "cabin", "castle", "garage", "garden", "kitchen", "bedroom", "bathroom", "roof",
    "dog", "cat", "rabbit", "horse", "elephant", "lion", "tiger", "monkey", "giraffe", "zebra",
    "ocean", "river", "lake", "pond", "waterfall", "stream", "beach", "island", "shore", "harbor",
    "cloud", "rain", "storm", "thunder", "lightning", "snow", "wind", "hurricane", "tornado", "fog",
    "music", "guitar", "piano", "violin", "trumpet", "drums", "flute", "saxophone", "song", "melody",
    "car", "bus", "bicycle", "motorcycle", "train", "airplane", "helicopter", "boat", "ship", "submarine",
    "computer", "keyboard", "mouse", "screen", "laptop", "printer", "speaker", "microphone", "camera", "phone",
    "book", "magazine", "newspaper", "novel", "dictionary", "journal", "poem", "story", "letter", "document",
    "school", "teacher", "student", "classroom", "homework", "exam", "library", "lesson", "notebook", "pencil",
    "fire", "earth", "water", "air", "metal", "wood", "stone", "sand", "glass", "plastic",
    "happiness", "sadness", "anger", "fear", "love", "hate", "surprise", "curiosity", "pride", "guilt",
    "day", "night", "morning", "afternoon", "evening", "sunrise", "sunset", "midnight", "dawn", "dusk",
    "city", "village", "town", "country", "capital", "suburb", "street", "avenue", "square", "market",
    "doctor", "nurse", "police", "firefighter", "teacher", "engineer", "scientist", "chef", "pilot", "artist",
    "bread", "butter", "cheese", "egg", "meat", "fish", "vegetable", "fruit", "soup", "salad",
    "smile", "laugh", "cry", "yawn", "wink", "hug", "kiss", "wave", "shout", "whisper",
    "fast", "slow", "big", "small", "tall", "short", "hot", "cold", "bright", "dark",
    "jump", "run", "walk", "sit", "stand", "dance", "swim", "climb", "fly", "crawl",
    "circle", "square", "triangle", "rectangle", "oval", "cube", "sphere", "pyramid", "diamond", "star",
    "simon", "raphael", "michalis", "tina", "dog", "cat", "codemanufaktur", "python", "java"
]

def get_word(words: list[str]) -> str:
  word: str = choice(words)
  return word

def play() -> None:
  print("<explanation>")
  word: str = get_word(WORDS).upper()
  letters_word: set[str] = set(word.upper())
  abc: set[str] = set(ascii_uppercase)
  used_letters: set[str] = set()
  lives: int = LIVES
  
  while lives > 0 and len(letters_word) > 0:
    print(f"Lives: {lives}")
    print(f"Letters used: {''.join(used_letters)}")
    word_list_print: list[str] = [letter if letter in used_letters else '_' for letter in word]
    print(f"Word: {' '.join(word_list_print)}\n")
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
  
  print(f"Letters used: {''.join(used_letters)}")
  print(f"Word: {word}")
  if lives == 0:
      print("LOST")
  else:
    print("WIN")


if __name__ == "__main__":
  play()