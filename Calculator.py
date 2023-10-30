import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.current_input = ""
        self.create_ui()

    def create_ui(self):
        # Entry widget for user input
        self.entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=50, pady=50, ipadx=40, ipady=10)

        # Button layout and labels with spacing
        button_labels = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/",
            "."
        ]

        # Create grid of buttons with padding
        row_val = 1
        col_val = 0
        for label in button_labels:
            button = self.create_button(label)
            button.grid(row=row_val, column=col_val, sticky="nsew", padx=10, pady=10, ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights for proper resizing
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)

    def create_button(self, label):
        button = tk.Button(self.root, text=label, font=("Helvetica", 18))
        button.bind("<Button-1>", self.button_click)
        return button

    def button_click(self, event):
        text = event.widget.cget("text")

        if text == "=":
            try:
                result = eval(self.current_input)
                self.clear_input()
                self.insert_text(result)
            except Exception as e:
                self.clear_input()
                self.insert_text("Error")
        elif text == "C":
            self.clear_input()
        else:
            self.insert_text(text)

    def clear_input(self):
        self.current_input = ""
        self.entry.delete(0, tk.END)

    def insert_text(self, text):
        self.current_input += str(text)
        self.entry.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
