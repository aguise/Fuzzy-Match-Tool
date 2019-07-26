import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore

class window(QMainWindow):
    def __init__(self):

        super(window, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle('Fuzzy Match Tool')
        self.home()

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)

        comboBox = QComboBox(self)
        comboBox.addItem("Currencies")
        comboBox.addItem("Countries")
        comboBox.addItem("Languages")
        comboBox.move(50, 250)
        comboBox.resize(120, 30)

        self.uploadButton = QPushButton('Upload', self)

        self.uploadButton.clicked.connect(self.open)

        self.show()

    def open (self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        print('Path file :', filename)

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()