import tkinter as tk
from tkinter import ttk

# TODO:
# 1. Change the title of the application - Done
# 2. In the same app, I want to be able to convert different quantities - Done
# 3. Make it not resizable (hint: in/after window.geometry) - Done
# Extras:
# 1. (entry of miles) mi = (label for kilometers) km
# 2. The main window should appear in the middle of the screen. (for any screen)

class ConverterPack:
  def __init__(self, row, window, label, number_description, output_description, convert_type) -> None:
    self.window = window
    
    self.row: int = row
    self.label: str = label
    self.number_description_text: str = number_description
    self.output_description: str = output_description
    self.convert_type: str = convert_type
    
    for i in range(row):
      self.window.grid_rowconfigure(i, minsize=20)
  
  def run(self) -> None:
    self.window.grid_rowconfigure(self.row, minsize=20)
    self.window.grid_rowconfigure(self.row+1, minsize=20)
    self.window.grid_rowconfigure(self.row+2, minsize=20)
    
    self.title_label = ttk.Label(master=self.window, text=self.label, font="Calibri 14 bold")
    self.title_label.grid(row=self.row, column=0, sticky="w")
    
    self.entry_int = tk.IntVar()
    self.entry_field = ttk.Entry(master=self.window, textvariable=self.entry_int, width=12)
    self.entry_field.grid(row=self.row+1, column=0, sticky="w")
    
    self.number_description = ttk.Label(master=self.window, text=self.number_description_text, font="Calibri 12 bold")
    self.number_description.grid(row=self.row+1, column=0, padx=(90, 0), sticky="w")
    
    self.convert_button = ttk.Button(text="Convert", command=self.convert)
    self.convert_button.grid(row=self.row+1, column=0, padx=(164, 0), sticky="w")
  
  def convert(self) -> None:
    self.output_str = tk.StringVar()
    try:
      match self.convert_type:
        case "distance": self.output_str.set(f"{(self.entry_int.get() * 1.61):.02f}")
        case "currency": self.output_str.set(f"{(self.entry_int.get() * 25.05):.02f}")
        case "temperature": self.output_str.set(f"{(self.entry_int.get() * (9/5) + 32):.02f}")
        case "weight": self.output_str.set(f"{(self.entry_int.get() * 0.4535924):.02f}")
        case _: ...
    except:
      self.output_str.set("Something went wrong... Restart for proper use")
      self.output_description = ""
    
    self.output = ttk.Label(master=self.window, text=f"{self.output_str.get()} {self.output_description}", font="Calibri 12 bold")
    self.output.grid(row=self.row+2, column=0, padx=(0, 0), sticky="w")


class ConverterGUIApp:
  def run(self):
    window = tk.Tk()
    window.title("Converter")
    window.geometry("300x350")
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')
    
    distance_converter: ConverterPack = ConverterPack(0, window, "Distance Converter", "Miles", "Kilometers", "distance")
    currency_converter: ConverterPack = ConverterPack(3, window, "Currency Converter", "Euro", "Czk", "currency")
    temperature_converter: ConverterPack = ConverterPack(6, window, "Temperature Converter", "Celsius", "Fahrenheit", "temperature")
    weight_converter: ConverterPack = ConverterPack(9, window, "Weight Converter", "Pound", "Kilograms", "weight")
    
    distance_converter.run()
    currency_converter.run()
    temperature_converter.run()
    weight_converter.run()
    
    window.mainloop()


if __name__ == "__main__":
  app = ConverterGUIApp()
  app.run()
