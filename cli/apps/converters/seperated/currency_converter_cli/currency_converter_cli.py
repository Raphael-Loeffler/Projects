from argparse import ArgumentParser

class Converter:
  def __init__(self):
    self.parser = ArgumentParser(description="Currency Converter - Options")
    self.parser.add_argument('-e', '--euro', type=float, default=None)
    self.parser.add_argument('-c', '--czk', type=float, default=None)
  
  def convert(self) -> str:
    if self.parser.parse_args().euro == None and self.parser.parse_args().czk != None:
      return f"{self.parser.parse_args().czk:.02f} czk = {(self.parser.parse_args().czk * 0.0397):.02f} euro"
    elif self.parser.parse_args().euro != None and self.parser.parse_args().czk == None:
      return f"{self.parser.parse_args().euro:.02f} euro = {(self.parser.parse_args().euro * 25.2158):.02f} czk"
    else:
      return """Only use one flag! -> currency_converter_object_oriented.py --euro=10")
Not: -> currency_converter_object_oriented.py --euro=10 --czk=10"""

if __name__ == "__main__":
  converter = Converter()
  print(converter.convert())