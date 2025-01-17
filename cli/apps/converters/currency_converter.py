from argparse import ArgumentParser

EURO_TO_CZK: float = 25.2158
CZK_TO_EURO: float = 0.0397

def boolean_string(s):
  return s == "True"

parser = ArgumentParser(description="Currency Converter - Options")
parser.add_argument('-a', '--amount', type=float, help="Total amount of money", default=1.0)
parser.add_argument('-e', '--euro', type=boolean_string, help="Change euro to czk if True", default=False)
parser.add_argument('-c', '--czk', type=boolean_string, help="Change czk to euro if True", default=False)

arguments = parser.parse_args()
money: float = arguments.amount
is_euro: bool = arguments.euro
is_czk: bool = arguments.czk

if is_euro:
  converted_amount = money * EURO_TO_CZK
elif is_czk:
  converted_amount = money * CZK_TO_EURO

if converted_amount and is_euro:
  print(f"{money:.02f} € = {converted_amount:.02f} czk")
elif converted_amount and is_czk:
  print(f"{money:.02f} czk = {converted_amount:.02f} €")
else:
  print("Something went wrong.")
