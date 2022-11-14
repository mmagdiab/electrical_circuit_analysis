from PyQt5 import QtCore, QtGui, QtWidgets
from branch import *
from ui import *


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    Ui(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
