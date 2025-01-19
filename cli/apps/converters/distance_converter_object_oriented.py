from argparse import ArgumentParser

class Converter:
  def __init__(self):
    self.parser = ArgumentParser(description="Distance Converter - Options")
    self.parser.add_argument('-k', '--kilometers', type=float, default=None)
    self.parser.add_argument('-m', '--miles', type=float, default=None)
  
  def convert(self) -> str:
    if self.parser.parse_args().kilometers == None and self.parser.parse_args().miles != None:
      return f"{self.parser.parse_args().miles:.02f} mil = {(self.parser.parse_args().miles / 1.60834):.02f} km"
    elif self.parser.parse_args().kilometers != None and self.parser.parse_args().miles == None:
      return f"{self.parser.parse_args().kilometers:.02f} km = {(self.parser.parse_args().kilometers * 1.60834):.02f} mil"
    else:
      return """Only use one flag! -> distance_converter_object_oriented.py --kilometers=10")
Not: -> distance_converter_object_oriented.py --kilometers=10 --miles=10"""

if __name__ == "__main__":
  converter = Converter()
  print(converter.convert())