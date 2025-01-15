from argparse import ArgumentParser

def fahrenheit_to_celsius(temperature_fahrenheit: float) -> float:
  return float((temperature_fahrenheit - 32) * 5/9)

parser = ArgumentParser(description="Currency Converter - Options")
parser.add_argument('-f', '--fahrenheit', type=float, help="Temperature in Fahrenheit")

arguments = parser.parse_args()

temperature_f: float = arguments.fahrenheit
temperature_c: float = fahrenheit_to_celsius(temperature_f)

print(f"{temperature_f} F = {temperature_c:.02f} C")