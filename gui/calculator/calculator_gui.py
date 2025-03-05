from tkinter import Tk, Frame, Button, Label, NSEW, E
from constants import *
from math import pi

"""
  TODO List
  1. Complete create_clear_button() - Done
  TODO!
  2. Complete create_square_button() x\u00b2
  3. Complete create_sqrt_button() \u221ax
  4. In evaluate() avoid errors ...
  5. Add button for pi
  6. Add button for phi (golden ratio)
  7. Add button x^3
  8. Add button x^(1/3) - 3er wurzel
  9. Add button for module operator : %
"""


class Calculator:
  def __init__(self):
    self.window: Tk = Tk()
    self.window.title("CMF Calculator")
    self.window.resizable(0, 0)
    
    SCREEN_WITH: int = self.window.winfo_screenwidth()
    SCREEN_HEIGHT: int = self.window.winfo_screenheight()
    APP_X: int = (SCREEN_WITH - APP_WIDTH) // 2
    APP_Y: int = (SCREEN_HEIGHT - APP_HEIGHT) // 2
    
    self.window.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{APP_X}+{APP_Y}") # "width x height + x_point + y_point"
    self.expression_eval: str = ""
    self.current_expression: str = ""
    self.total_expression: str = ""
    self.root_type: list = list()
    self.digits: dict = {
      7: (1, 1), 8: (1, 2), 9: (1, 3),
      4: (2, 1), 5: (2, 2), 6: (2, 3),
      1: (3, 1), 2: (3, 2), 3: (3, 3),
      '.': (4, 1), 0:(4, 2)
    }
    self.operations: dict = {
      "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+", "\u00D7 \u00D7": "² "
    }
    self.display_frame: Frame = self.create_display_frame()
    self.total_label, self.current_label = self.create_display_labels()
    self.buttons_frame: Frame = self.create_buttons_frame()
    self.create_buttons()
  
  def bind_keys(self) -> None:
    ...
  
  def add_to_expression(self,value) -> None:
    self.current_expression += str(value)
    self.expression_eval += str(value)
    self.update_current_label()
  
  def create_buttons(self) -> None:
    self.buttons_frame.rowconfigure(0, weight=1)
    for i in range(1, 5):
      self.buttons_frame.rowconfigure(i, weight=1)
      self.buttons_frame.columnconfigure(i, weight=1)
    self.create_digit_buttons()
    self.create_operator_buttons()
    self.create_clear_button()
    self.create_square_button()
    self.create_open_sqrt_button()
    self.create_open_curt_button()
    self.create_close_root_button()
    self.create_equals_button()
    self.create_pi_button()
  
  def create_pi_button(self) -> None:
    button: Button = Button(master=self.buttons_frame, text="π", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.pi)
    button.grid(row=0, column=5, sticky=NSEW)
  
  def pi(self) -> None:
    self.current_expression += "π"
    self.expression_eval += f"{pi}"
    self.update_current_label()
  
  def create_open_sqrt_button(self) -> None:
    button: Button = Button(width=1,master=self.buttons_frame, text=OPEN_SQRT_CONFIG_TEXT, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.open_sqrt)
    button.grid(row=1, column=5, sticky=NSEW)
  
  def create_open_curt_button(self) -> None:
    button: Button = Button(width=1,master=self.buttons_frame, text=OPEN_CURT_CONFIG_TEXT, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.open_curt)
    button.grid(row=2, column=5, sticky=NSEW)
  
  def create_open_cuberoot_button(self) -> None:
    self.cuberoot_button: Button = Button(width=1,master=self.buttons_frame, text=OPEN_SQRT_CONFIG_TEXT, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.open_sqrt)
  
  def create_close_root_button(self) -> None:
    self.sqrt_button: Button = Button(width=1,master=self.buttons_frame, text=CLOSE_ROOT_CONFIG_TEXT, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.close_root)
    self.sqrt_button.grid(row=3, column=5, sticky=NSEW)
  
  def open_sqrt(self) -> None:
    self.expression_eval += "("
    self.current_expression += OPEN_SQRT_EXPRESSION
    self.root_type.append(2)
    
    self.update_current_label()
  
  def open_curt(self) -> None:
    self.expression_eval += "("
    self.current_expression += OPEN_CURT_EXPRESSION
    self.root_type.append(3)
    
    self.update_current_label()
  
  def close_root(self) -> None:
    self.expression_eval += f")**{1 / self.root_type[-1]}"
    self.current_expression += CLOSE_ROOT_EXPRESSION
    self.root_type.pop()
    self.total_expression += self.current_expression
    self.current_expression = ""
    self.update_current_label()
    self.update_total_label()
  
  def create_square_button(self) -> None:
    button: Button = Button(master=self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.square)
    button.grid(row=0, column=2, sticky=NSEW)
  
  def square(self) -> None:
    self.current_expression += "²"
    self.expression_eval += "**2"
    self.total_expression += self.current_expression
    self.current_expression = ""
    self.update_current_label()
    self.update_total_label()
  
  def clear(self) -> None:
    self.current_expression = ""
    self.total_expression = ""
    self.expression_eval = ""
    self.update_current_label()
    self.update_total_label()
  
  def create_clear_button(self) -> None:
    button: Button = Button(master=self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, cursor="hand2", command=self.clear)
    button.grid(row=0, column=1, sticky=NSEW)
  
  def add_operator(self, operator, symbol) -> None:
    self.update_current_label()
    self.expression_eval += operator
    self.total_expression += f"{self.current_expression}{symbol}"
    self.current_expression = ""
    self.update_current_label()
    self.update_total_label()
  
  def evaluate(self) -> None:
    try:
      self.current_expression = f"{eval(self.expression_eval)}" if self.expression_eval != "" else ""
    except:
      self.current_expression = "Error"
    self.total_expression = ""
    self.total_expression_eval = ""
    self.update_current_label()
    self.update_total_label()
  
  def create_equals_button(self) -> None:
    button: Button = Button(master=self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.evaluate)
    button.grid(row=4, column=3, columnspan=2, sticky=NSEW)
  
  def create_operator_buttons(self) -> None:
    i = 0
    for operator, symbol in self.operations.items():
      button: Button = Button(master=self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, cursor="hand2", command=lambda x=operator, y=symbol: self.add_operator(x, y))
      button.grid(row=i, column=4, sticky=NSEW)
      i += 1
  
  def create_digit_buttons(self) -> None:
    for digit, position in  self.digits.items():
      button: Button = Button(master=self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=BUTTONS_FONT, borderwidth=0, cursor="hand2", command=lambda x=digit: self.add_to_expression(x))
      button.grid(row=position[0], column=position[1], sticky=NSEW)
  
  def update_total_label(self) -> None:
    self.total_label.config(text=self.total_expression)
  
  def update_current_label(self) -> None:
    try:
      self.current_expression = f"{round(float(self.current_expression), 10):g}"
    except:
      ...
    
    self.current_label.config(text=self.current_expression)
  
  def create_buttons_frame(self) -> Frame:
    buttons_frame: Frame = Frame(master=self.window)
    buttons_frame.pack(expand=True, fill="both")
    return buttons_frame
  
  def create_display_labels(self) -> tuple[Label]:
    total_label: Label = Label(master=self.window, text=self.total_expression, bg=LIGHT_GRAY, fg=LABEL_COLOR, anchor=E, padx=20)
    total_label.pack(expand=True, fill="both")
    
    current_label: Label = Label(self.window, text=self.current_expression, bg=LIGHT_GRAY, fg=LABEL_COLOR, font=BIG_FONT, anchor=E)
    current_label.pack(expand=True, fill="both")
    
    return total_label, current_label
  
  def create_display_frame(self) -> Frame:
    display_frame: Frame = Frame(master=self.window, height=100, bg=WHITE)
    display_frame.pack(expand=True, fill="both")
    return display_frame
  
  def run(self) -> None:
    self.window.mainloop()

if __name__ == "__main__":
  calculator_app: Calculator = Calculator()
  calculator_app.run()