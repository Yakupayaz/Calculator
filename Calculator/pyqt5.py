import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt  

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit(self)
        self.result_display.setAlignment(Qt.AlignRight) 
        self.layout.addWidget(self.result_display)

        button_layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row in button_layout:
            row_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.handle_button_click)
                row_layout.addWidget(button)
            self.layout.addLayout(row_layout)

        self.central_widget.setLayout(self.layout)

        self.current_input = ""

    def handle_button_click(self):
        button = self.sender()
        if button.text() == "=":
            try:
                result = eval(self.current_input)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Hata")
            self.current_input = ""
        else:
            self.current_input += button.text()
            self.result_display.setText(self.current_input)

def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
