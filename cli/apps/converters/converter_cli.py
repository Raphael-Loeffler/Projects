from argparse import ArgumentParser

def rest_is_none(target, arguments) -> bool:
    for arg in vars(arguments):
        if arg != target:
            value = getattr(arguments, arg)
            if value != None:
                return False
    return True

def run() -> None:
    parser = ArgumentParser(description="Converter - Options")
    parser.add_argument('-kg', '--kilograms', type=float, help="Convert kilograms to pounds", default=None)
    parser.add_argument('-lb', '--pounds', type=float, help="Convert pounds to kilograms", default=None)
    parser.add_argument('-f', '--fahrenheit', type=float, help="Convert Fahrenheit in Celsius", default=None)
    parser.add_argument('-c', '--celsius', type=float, help="Convert celsius in Fahrenheit", default=None)
    parser.add_argument('-k', '--kilometers', type=float, help="Convert kilometers to miles", default=None)
    parser.add_argument('-m', '--miles', type=float, help="Convert miles to kilometers", default=None)
    parser.add_argument('-e', '--euro', type=float, help="Convert euro to czech koruna", default=None)
    parser.add_argument('-czk', '--czech_koruna', type=float, help="Convert czech koruna to euro", default=None)
    
    arguments = parser.parse_args()
    
    if arguments.kilograms != None and rest_is_none("kilograms", arguments):
        print(f"{arguments.kilograms:.02f} kg = {(arguments.kilograms * 2.204623):.02f} lb")
    elif arguments.pounds != None and rest_is_none("pounds", arguments):
        print(f"{arguments.pounds:.02f} lb = {(arguments.pounds / 2.204623):.02f} kg")
    elif arguments.fahrenheit != None and rest_is_none("fahrenheit", arguments):
        print(f"{arguments.fahrenheit:.02f} f = {((arguments.fahrenheit - 32) * 5/9):.02f} c")
    elif arguments.celsius != None and rest_is_none("celsius", arguments):
        print(f"{arguments.celsius:.02f} c = {(arguments.celsius  * 9/5 + 32):.02f} f")
    elif arguments.kilometers != None and rest_is_none("kilometers", arguments):
        print(f"{arguments.kilometers:.02f} km = {(arguments.kilometers / 1.60834):.02f} mil")
    elif arguments.miles != None and rest_is_none("miles", arguments):
        print(f"{arguments.miles:.02f} mil = {(arguments.miles * 1.60834):.02f} km")
    elif arguments.euro != None and rest_is_none("euro", arguments):
        print(f"{arguments.euro:.02f} euro = {(arguments.euro * 25.2158):.02f} czk")
    elif arguments.czech_koruna != None and rest_is_none("czech_koruna", arguments):
        print(f"{arguments.czech_koruna:.02f} czk = {(arguments.czech_koruna / 25.2158):.02f} euro")

if __name__ == "__main__":
    run()