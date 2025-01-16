from argparse import ArgumentParser

class Converter:
  def __init__(self, celsius: float, fahrenheit: float):
    self.celsius = celsius
    self.fahrenheit = fahrenheit
  def convert(self) -> str:
    if self.celsius == None and self.fahrenheit != None:
      return f"{self.fahrenheit:.02f} °F = {(self.fahrenheit - 32) * 5/9:.02f} °C"
    elif self.fahrenheit == None and self.celsius != None:
      return f"{self.celsius:.02f} °C = {self.celsius * 9/5 + 32:.02f} °F"
    else:
      print("Only use one flag! -> temperature_converter_object_oriented.py -c=10")
      return "Not: -> temperature_converter_object_oriented.py -c=10 -f=10"


parser = ArgumentParser(description="Currency Converter - Options")
parser.add_argument('-f', '--fahrenheit', type=float, help="Convert Fahrenheit in Celsius", default=None)
parser.add_argument('-c', '--celsius', type=float, help="Convert celsius in Fahrenheit", default=None)
converter = Converter(parser.parse_args().celsius, parser.parse_args().fahrenheit)
print(converter.convert())