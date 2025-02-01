from morse_constants import CHARS_TO_MORSE, MORSE_TO_CHARS

class Morse_Code_Translator:
    def translate(self) -> str:
        print("""1. Translate morse code into normal letters.
2. Translate normal letters into morse code.""")
        match input("Please take an option (press 1 or 2): "):
            case '1': return(self.translate_morse_code(input("Please enter the morse code: ")))
            case '2': return(self.translate_letters(input("Please enter the word/sentence: ")))
            case _: return "Something went wrong. Please only press 1 or 2."
    
    def translate_morse_code(self, morse_code: str) -> str:
        output: str = ""
        for key in morse_code.split(" "):
            output += MORSE_TO_CHARS[key]
        return output
    
    def translate_letters(self, letters: str) -> str:
        print("Note: Every \ stands for an not translatable character.")
        output: str = ""
        for key in list(letters.upper()):
            try:
                output += CHARS_TO_MORSE[key]
                if key != letters[-1]:
                    output += " "
            except:
                output += "\\"
                if key != letters[-1]:
                    output += " "
        return output

def run() -> None:
    morse_code_translator = Morse_Code_Translator()
    print(morse_code_translator.translate())


if __name__ == "__main__":
    run()