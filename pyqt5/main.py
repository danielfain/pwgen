import sys
import pyperclip
import string
import secrets
from PyQt5 import QtGui, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.title = 'pwgen'
        self.min = 0
        self.max = 64
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.view()

    def view(self):
        self.generate_password()
        self.close_app()

    def get_len(self):
        i, okPressed = QtWidgets.QInputDialog.getInt(self, self.title, "Characters:", 0, self.min, self.max, 1)
        if okPressed:
            return i
        else:
            self.close_app()

    def generate_password(self):
        al = string.ascii_letters + string.digits
        pyperclip.copy(''.join(secrets.choice(al) for i in range(self.get_len())))

    def close_app(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())
