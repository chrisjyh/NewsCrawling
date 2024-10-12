import sys

from PyQt5.QtWidgets import QApplication

from ui.uiForm import Ui_Form


def display():
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    display()