#!/usr/bin/env python3
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit(self)
        self.text.setTabStopWidth(12)
        self.setCentralWidget(self.text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
