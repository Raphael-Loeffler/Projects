from argparse import ArgumentParser

EURO_TO_CZK: float = 25.2158
CZK_TO_EURO: float = 0.0397

parser = ArgumentParser(description="Currency Converter - Options")
parser.add_argument('-a', '--amount', type=float, help="Total amount of money", default=1.0)
parser.add_argument('-e', '--euro', type=bool, help="Change euro to czk if True", default=True)
parser.add_argument('-c', '--czk', type=bool, help="Change czk to euro if True", default=False)

arguments = parser.parse_args()

money: float = arguments.amount
print(f"{money=}")
print(f"{type(money)=}")

is_euro: bool = arguments.euro
print(f"{is_euro=}")
print(f"{type(is_euro)=}")

is_czk: bool = arguments.czk
print(f"{is_czk=}")
print(f"{type(is_czk)=}")

if is_euro:
  converted_amount = money * EURO_TO_CZK
elif is_czk:
  converted_amount = money * CZK_TO_EURO

if converted_amount and is_euro:
  print(f"{money} € = {converted_amount} czk")
elif converted_amount and is_czk:
  print(f"{money} czk = {converted_amount} €")
else:
  print("Something went wrong.")
