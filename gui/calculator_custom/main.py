from tkinter import Tk, Frame, Button, Label, E, NSEW


from constants import *

class Calculator_App:
    def __init__(self):
        self.window: Tk = Tk()
        self.window.title("Calculator")
        
        self.current_expression = ""
        self.total_expression = ""
        self.evaluation_expression = ""
        
        self.display_frame: Frame = Frame(master=self.window, height=100, bg=WHITE)
        self.display_frame.pack(expand=True, fill="both")
        
        self.total_label: Label = Label(master=self.window, text=self.total_expression, bg=LIGHT_GRAY, fg=LABEL_COLOR, anchor=E, padx=20)
        self.total_label.pack(expand=True, fill="both")
        
        self.current_label: Label = Label(master=self.window, text=self.current_expression, bg=LIGHT_GRAY, fg=LABEL_COLOR, font=BIG_FONT, anchor=E)
        self.current_label.pack(expand=True, fill="both")
        
        self.buttons_frame: Frame = Frame(master=self.window)
        self.buttons_frame.pack(expand=True, fill="both")
        
        self.root_type_stack = []
        
        self.buttons_list = self.create_buttons_list()
        
        for index_row, button_row in enumerate(self.buttons_list):
            for index_column, button_column in enumerate(button_row):
                self.create_button(button_column[0], button_column[1], button_column[2], button_column[3], index_row, index_column, button_column[-1])
    
    def create_buttons_list(self) -> list:
        return [[
                ['C', BIG_FONT, LABEL_COLOR, LIGHT_GRAY, self.clear],
                ['ϕ', BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d='ϕ', e=f"{PHI}": self.add_to_expressions(d, e,)],
                ['π', BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d='π', e=f"{PI}": self.add_to_expressions(d, e)],
                ["\u00F7", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="\u00F7", e='/': self.add_to_expressions_and_shift(d, e)],
                ["\u2190", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, self.delete],
            ], [
                ['7', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='7', e='7': self.add_to_expressions(d, e)],
                ['8', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='8', e='8': self.add_to_expressions(d, e)],
                ['9', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='9', e='9': self.add_to_expressions(d, e)],
                ["\u00D7", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="\u00D7", e='*': self.add_to_expressions_and_shift(d, e)],
                ["√x", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="√", e='(', r=2: self.add_root_expression(d, e, r)],
            ], [
                ['4', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='4', e='4': self.add_to_expressions(d, e)],
                ['5', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='5', e='5': self.add_to_expressions(d, e)],
                ['6', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='6', e='6': self.add_to_expressions(d, e)],
                ["-", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="-", e='-': self.add_to_expressions_and_shift(d, e)],
                ["∛x", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="∛", e='(', r=3: self.add_root_expression(d, e, r)],
            ], [
                ['1', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='1', e='1': self.add_to_expressions(d, e)],
                ['2', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='2', e='2',: self.add_to_expressions(d, e)],
                ['3', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='3', e='3': self.add_to_expressions_and_shift(d, e)],
                ["+", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="+", e='+': self.add_to_expressions_and_shift(d, e)],
                ["x'", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, self.end_root],
            ], [
                ['.', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='.', e='.': self.add_to_expressions(d, e)],
                ['0', BUTTONS_FONT, LABEL_COLOR, OFF_WHITE, lambda d='0', e='0': self.add_to_expressions(d, e)],
                ["=", BIG_FONT, LABEL_COLOR, LIGHT_BLUE, self.evaluate],
                ["%", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="%", e='%': self.add_to_expressions_and_shift(d, e)],
                ["x²", BIG_FONT, LABEL_COLOR, LIGHT_GRAY, lambda d="x²", e='**2': self.add_to_expressions(d, e)]
            ]
        ]
    
    def end_root(self) -> None:
        self.current_expression += "'"
        self.evaluation_expression += f")**{1/self.root_type_stack[-1]}"
        self.root_type_stack.pop()
        self.update()
    
    def add_root_expression(self, display_text: str, evaluation_text: str, root_type: int) -> None:
        self.current_expression += display_text
        self.evaluation_expression += evaluation_text
        self.root_type_stack.append(root_type)
        self.update()
    
    def delete(self) -> None:
        self.current_expression = self.current_expression[:-1]
        self.evaluation_expression = str(self.evaluation_expression)[:-1]
        self.update()
    
    def clear(self) -> None:
        self.current_expression = ""
        self.total_expression = ""
        self.evaluation_expression = ""
        self.update()
    
    def add_to_expressions(self, display_text: str, evaluation_text: str) -> None:
        self.current_expression += display_text
        
        self.evaluation_expression += evaluation_text
        self.update()
    
    def add_to_expressions_and_shift(self, display_text: str, evaluation_text: str) -> None:
        self.current_expression += display_text
        self.total_expression += self.current_expression
        self.current_expression = ""
        
        self.evaluation_expression += evaluation_text
        self.update()
    
    def evaluate(self) -> None:
        try:
            result: float = eval(f"{self.evaluation_expression}")
            self.current_expression = f"{round(result, 9):0g}" if self.evaluation_expression != "" else ""
        except:
            self.current_expression = "Error"
        
        self.total_expression = ""
        
        self.update_leave_error()
    
    def create_button(self, display_text, font, fg, bg, row, column, command) -> None:
        button: Button = Button(master=self.buttons_frame, text=display_text, bg=bg, fg=fg, font=font, borderwidth=0, command=command)
        button.grid(row=row, column=column, sticky=NSEW)
    
    def update(self) -> None:
        self.current_expression = self.current_expression.replace("Error", "")
        self.current_label.config(text=self.current_expression)
        self.total_label.config(text=self.total_expression)
    
    def update_leave_error(self) -> None:
        self.current_label.config(text=self.current_expression)
        self.total_label.config(text=self.total_expression)
    
    def run(self) -> None:
        self.window.mainloop()

def run() -> None:
    app: Calculator_App = Calculator_App()
    app.run()

if __name__ == "__main__":
    run()
