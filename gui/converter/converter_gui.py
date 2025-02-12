import tkinter as tk
from tkinter import ttk


class ConverterGUIApp:
  def run(self) -> None:
    pass

window = tk.Tk()
window.title("Distance Converter")
window.geometry("300x150")

def convert():
  print(f"output_str={output_str.get()}")           #output_str=first output
  print(f"entry_int={entry_int.get()}")             #entry_int=10
  output_str.set(f"{entry_int.get() * 1.61} km")    #16.1 km
  print(f"output_str={output_str.get()}")           #output_str=16.1 km

# Constant text
title_label = ttk.Label(master=window, text="Miles to kilometers", font="Calibri 14 bold")
title_label.pack(pady=10)

input_frame = ttk.Frame(master=window)
input_frame.pack(pady=10)
entry_int = tk.IntVar()
entry_field = ttk.Entry(master=input_frame, textvariable=entry_int)
entry_field.pack(side="left", padx=10)
convert_button = ttk.Button(master=input_frame, text="Convert", command=convert)
convert_button.pack(side="left")

output_str = tk.StringVar()
output_label = ttk.Label(master=window, text="", font="Calibri 10", textvariable=output_str)
output_label.pack(pady=10)

window.mainloop()

if __name__ == "__main__":
  app = ConverterGUIApp()
  app.run()
  print("Main")

# TODO:
# 1. Change the title of the application
# 2. In the same app, I want to be able to convert different quantities
# 3. Make it not resizable (hint: in/after window.geometry)
# Extras:
# 1. (entry of miles) mi = (label for kilometers) km
# 2. The main window should appear in the middle of the screen. (for any screen)