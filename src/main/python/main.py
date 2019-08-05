import sys
import csv
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle('BNY Mellon Fuzzy Match Tool')
        self.setWindowIcon(QIcon(os.getcwd() + "\src\main\icons\bny_mellon.png"))
        self.setStyleSheet('''.window{
            background-color: rgb(142, 146, 147)
        }
        ''')

        # add all widgets
        self.btn_1 = QPushButton('Standardize', self)
        self.btn_1.setStyleSheet('''.QPushButton{
            background-color: rgb(142, 146, 147)
        }
        ''')
        self.btn_2 = QPushButton('Standardize and Evaluate', self)
        self.btn_2.setStyleSheet('''.QPushButton{
            background-color: rgb(142, 146, 147)
        }
        ''')
        self.btn_3 = QPushButton('About', self)
        self.btn_3.setStyleSheet('''.QPushButton{
            background-color: rgb(142, 146, 147)
        }
        ''')
        self.quit = QPushButton('Quit', self)
        self.quit.setStyleSheet('''.QPushButton{
            background-color: rgb(142, 146, 147)
        }
        ''')

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.quit.clicked.connect(QCoreApplication.instance().quit)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()

        self.initUI()
        self.home()

    def home(self):

        self.show()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.quit)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setStyleSheet('''
        .QWidget {
            background-color: rgb(175, 134, 53);
        }
        ''')

        bny_logo = QLabel(self)
        pixmap = QPixmap(os.getcwd() + "\src\main\icons\bny_logo.png")
        bny_logo.setPixmap(pixmap)
        left_layout.addWidget(bny_logo)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    
    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Select the type of data you are inputting and then browse the computer for a CSV file of data that needs to be standardized: '))
        main_layout.addStretch(5)

        comboBox = QComboBox(self)
        comboBox.addItem("Currencies")
        comboBox.addItem("Countries")
        comboBox.addItem("Languages")
        comboBox.setStyleSheet('''
        .QComboBox {
            text-align: center;
            }
            ''')

        standardize_button = QPushButton('Standardize', self)
        standardize_button.resize(standardize_button.minimumSizeHint())
        standardize_button.move(350, 100)

        uploadButton = QPushButton('Upload', self)
        uploadButton.resize(uploadButton.minimumSizeHint())
        uploadButton.move(200, 100)

        uploadButton.clicked.connect(self.open)

        main_layout.addWidget(comboBox)
        main_layout.addWidget(standardize_button)
        main_layout.addWidget(uploadButton)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 2'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Fuzzy Match Tool'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 4'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def open (self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.')

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.tableWidgetDATA = QTableWidget(self)
        self.listWidgetID = QListWidget(self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.listWidgetID)
        self.layout().addWidget(self.tableWidgetDATA)



def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()