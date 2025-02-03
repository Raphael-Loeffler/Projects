from morse_constants import *

class MorseCodeTranslator:
    def translate(self) -> str:
        print(MENU_INSTRUCTIONS)
        user_input: str = input("Please take an option (press 1 or 2): ")
        match user_input:
            case '1': return(self.translate_morse_code(input("Please enter the morse code: ")))
            case '2': return(self.translate_letters(input("Please enter the word/sentence: ")))
            case _: return ERROR_MESSAGE
    
    def translate_morse_code(self, morse_code: str) -> str:
        output: str = ""
        for key in morse_code.split(" "):
            try:
                output += MORSE_TO_CHARS[key]
            except:
                output += "\\"
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
    morse_code_translator = MorseCodeTranslator()
    print(morse_code_translator.translate())


if __name__ == "__main__":
    run()