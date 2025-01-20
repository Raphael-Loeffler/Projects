
"""
TODO handle cases: 1+ 2
                   1+2
                     1 + 2  <- Done
TODO: add %, //, **
TODO: also show expression -> input: 1 + 2
                              output: 1.0 + 2.0 = 3.0
"""

def add(first_number: float, second_number: float) -> float:
  return first_number + second_number

def subtract(first_number: float, second_number: float) -> float:
  return first_number - second_number

def divide(first_number: float, second_number: float) -> float:
  return first_number / second_number

def multiply(first_number: float, second_number: float) -> float:
  return first_number * second_number

def modulus(first_number: float, second_number: float) -> float:
  return first_number % second_number

def exponential(first_number: float, second_number: float) -> float:
  return first_number ** second_number

def floor_division(first_number: float, second_number: float) -> float:
  return first_number // second_number

def run() -> float:
  print("Python Calculator v2.1")
  print("Options:")
  print("""- Addition: +
- Subtraction: -
- Division: /
- Multiplication: *""")
  print("Example: 1 + 2")
  user_input: str = input("Provide the expression: ")
  first_number, operator, second_number = user_input.strip().split(" ")
  first_number: float = float(first_number)
  second_number: float = float(second_number)
  result = None
  match operator:
    case '+': result = add(first_number, second_number)
    case '-': result = subtract(first_number, second_number)
    case '/': result = divide(first_number, second_number)
    case '*': result = multiply(first_number, second_number)
    case '**': result = exponential(first_number, second_number)
    case '//': result = floor_division(first_number, second_number)
    case '%': result = modulus(first_number, second_number)
  return result



if __name__ == "__main__":
  result: float = run()
  print(result)