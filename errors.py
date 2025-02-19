from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox





class ErrorMessageBox:
    def __init__(self, error_message):
        
        message_box = QMessageBox()
        message_box.setWindowTitle("Error Message")
        message_box.setText(error_message)
        message_box.setIcon(QMessageBox.Critical)
        message_box.setAttribute(Qt.WA_DeleteOnClose)
        ok_button = message_box.button(QMessageBox.Ok)
        if ok_button:
            ok_button.clicked.connect(self.deleteLater)
        
        message_box.destroyed.connect(lambda: print("Error Message Destroyed!"))
        message_box.exec_()


class InvalidInputError(ErrorMessageBox):
    def __init__(self):
        super().__init__(f"Invalid Value! Enter a number.")


class InvalidAValueError(ErrorMessageBox):
    def __init__(self):
        super().__init__("The coefficient of x² must be not equal 0.")


if __name__ == "__main__":
    pass