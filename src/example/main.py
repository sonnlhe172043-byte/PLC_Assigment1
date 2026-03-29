import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLCDNumber, QLabel, QFileDialog
#Please, ignore IDE warning
from components.lexica import MyLexer
from components.parsers import ASTParser
from components.ui_main import Ui_MainWindow
from datetime import datetime


def write_log(input_text, result, prefix, level="INFO", filename="logAssignment1.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {level} | Input: {input_text} | Result: {result} | Prefix: {prefix}\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(log_line)


def is_valid_expression(expr: str):
    tokens = expr.split()

    if len(tokens) % 2 == 0:
        return False

    for i in range(len(tokens)):
        if i % 2 == 0:
            if tokens[i] not in ['t', 'f']:
                return False
        else:
            if tokens[i] not in ['^', 'v']:
                return False

    return True

class MainWindow(QMainWindow):


    button_t: QPushButton
    button_f: QPushButton
    button_and: QPushButton
    button_or: QPushButton
    button_equal: QPushButton

    input_text: QLineEdit
    output_lcd: QLCDNumber
    Prefix: QLabel

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button
        self.ui.button_t.clicked.connect(lambda: self.push("t"))
        self.ui.button_f.clicked.connect(lambda: self.push("f"))
        self.ui.button_and.clicked.connect(lambda: self.push("^"))
        self.ui.button_or.clicked.connect(lambda: self.push("v"))

        self.ui.button_equal.clicked.connect(self.push_equal)

        # Delete button
        self.ui.button_delete.clicked.connect(self.delete_last_char)

        #
        self.ui.Prefix.setText("Prefix")

    def delete_last_char(self):
        tokens = self.ui.input_text.text().split()
        if tokens:
            tokens.pop()
            self.ui.input_text.setText(" ".join(tokens))

    def push(self, text: str):
        current_text = self.ui.input_text.text()

        if current_text:
            new_text = current_text + " " + text
        else:
            new_text = text

        self.ui.input_text.setText(new_text)

    def push_equal(self):
        print("Calculate")

        input_text = self.ui.input_text.text().strip()

        # empty input
        if not input_text:
            self.ui.output_text.setText("Empty")
            self.ui.Prefix.setText("Prefix")
            return

        # validation input
        if not is_valid_expression(input_text):
            self.ui.output_text.setText("Syntax Error")
            self.ui.Prefix.setText("Invalid Expression")
            return

        try:
            lexer = MyLexer()
            parser = ASTParser()

            root = parser.parse(lexer.tokenize(input_text))

            if root is None:
                raise ValueError("Re-input")

            root.run()
            result = root.value

            self.ui.output_text.setText("t" if result else "f")

            prefix_str = root.preval()
            self.ui.Prefix.setText(prefix_str)

            write_log(input_text, result, prefix_str)

            print(f"Final Value: {result}")
            print(f"Prefix: {prefix_str}")

        except Exception as e:
            print(f"Error: {e}")
            write_log(input_text, "Error", str(e))

            self.ui.output_text.setText("Error")
            self.ui.Prefix.setText("Check input")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())