import sys
import pyperclip
import string
import secrets
from PyQt5 import QtGui, QtWidgets, QtCore


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pwgen')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.menu()
        self.view()

    def menu(self):
        menu_bar = QtWidgets.QMenuBar()
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu('File')

        exit = QtWidgets.QAction(' &Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Close the application')
        exit.triggered.connect(self.close_app)
        file_menu.addAction(exit)

    def view(self):
        gen_btn = QtWidgets.QPushButton('Generate', self)
        gen_btn.resize(gen_btn.sizeHint())
        gen_btn.move(100, 100)
        gen_btn.clicked.connect(self.generate_password)

        self.show()

    def generate_password(self):
        al = string.ascii_letters + string.digits
        pyperclip.copy(''.join(secrets.choice(al) for i in range(16)))

    def close_app(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())
