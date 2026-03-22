
from components.ui_main import Ui_MainWindow

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLCDNumber, QLabel, QFileDialog

from components.lexica import MyLexer
from components.parsers import ASTParser  # giả sử đây là file chứa ASTParser
from components.memory import Memory
from components.ui_main import Ui_MainWindow
from datetime import datetime


def write_log(input_text, result, prefix, level="INFO", filename="logAssignment1.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {level} | Input: {input_text} | Result: {result} | Prefix: {prefix}\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(log_line)

class MainWindow(QMainWindow):

    # Type hint (giữ nguyên nếu bạn có)
    button_t: QPushButton
    button_f: QPushButton
    button_and: QPushButton
    button_or: QPushButton
    button_equal: QPushButton

    input_text: QLineEdit
    output_lcd: QLCDNumber
    Prefix: QLabel  # thêm nếu bạn dùng type hint

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các button
        self.ui.button_t.clicked.connect(lambda: self.push("t"))
        self.ui.button_f.clicked.connect(lambda: self.push("f"))
        self.ui.button_and.clicked.connect(lambda: self.push("^"))
        self.ui.button_or.clicked.connect(lambda: self.push("v"))

        self.ui.button_equal.clicked.connect(self.push_equal)

        # Kết nối button Delete mới
        self.ui.button_delete.clicked.connect(self.delete_last_char)

        # Giá trị ban đầu cho Prefix (tùy chọn)
        self.ui.Prefix.setText("Prefix")

    def delete_last_char(self):
        current_text = self.ui.input_text.text()
        if current_text:
            # Xóa ký tự cuối cùng
            new_text = current_text[:-1]
            self.ui.input_text.setText(new_text)
            print(f"deleted last symbol, : {new_text}")

    def push(self, text: str):
        current_text = self.ui.input_text.text()
        self.ui.input_text.setText(current_text + text)

    def push_equal(self):
        print("Calculate")



        input_text = self.ui.input_text.text().strip()  # ← biến input_text chỉ có ở đây

        if not input_text:
            self.ui.output_lcd.display(0)
            self.ui.Prefix.setText("Prefix")
            return

        try:
            lexer = MyLexer()
            parser = ASTParser()

            root = parser.parse(lexer.tokenize(input_text))  # ← dùng input_text ở đây
            if lexer.index < len(lexer.text):
                raise SyntaxError("Have to t/f first")

            if root is None:
                raise ValueError("Re-input")

            root.run()  # calculate value
            result = root.value

            self.ui.output_text.setText( "t" if result else "f")

            # prefix (n to_prefix / preval)
            prefix_str = root.preval()  # h root.preval() flexible
            self.ui.Prefix.setText(prefix_str)
            # ====== auto log ======
            write_log(input_text, result, prefix_str)

            print(f"Final Value: {result}")
            print(f"Prefix: {prefix_str}")

        except Exception as e:
            print(f"Error: {e}")
            write_log(input_text, "Error", e)
            self.ui.output_text.setText(0)
            self.ui.Prefix.setText(f"Lỗi: {str(e)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())