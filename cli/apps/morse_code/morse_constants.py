MENU_INSTRUCTIONS: str = """
Morse Code Engine

Options:
[1] Encrypt
[2] Decrypt

"""

ERROR_MESSAGE: str = "Invalid option! Enter 1 for encryption or 2 for decryption. Please try again!"

CHARS_TO_MORSE: dict = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..','M':'--',
    'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', " ": "SPACE",
}

MORSE_TO_CHARS: dict = {v: k for k, v in CHARS_TO_MORSE.items()}