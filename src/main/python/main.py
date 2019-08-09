import sys, csv, os, openpyxl
import driver
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
from fbs_runtime.application_context.PyQt5 import ApplicationContext

class window(QMainWindow):

    filename = "No file found"
    filename_standards = "No file found"
    data_type = ""
    def __init__(self):
        appctxt = ApplicationContext() 
        super(window, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle('BNY Mellon Fuzzy Match Tool')
        self.setWindowIcon(QIcon('bny_icon.png'))
        self.setStyleSheet('''.window{
            background-color: rgb(172, 134, 53)
        }
        ''')

        # add all widgets
        self.btn_1 = QPushButton('Standardize', self)
        self.btn_1.setStyleSheet('''.QPushButton{
            background-color: rgb(142, 146, 147)
        }
        ''')
        self.btn_2 = QPushButton('About', self)
        self.btn_2.setStyleSheet('''.QPushButton{
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
        self.quit.clicked.connect(QCoreApplication.instance().quit)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()

        self.initUI()
        self.home()

        exit_code = appctxt.app.exec_()   
        sys.exit(exit_code)

    def home(self):

        self.show()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.quit)
        left_layout.addStretch(5)
        left_layout.setSpacing(35)
        left_widget = QWidget()
        bny_logo = QLabel(self)
        pixmap = QPixmap('bny_logo.png')
        bny_logo.setPixmap(pixmap)
        left_layout.addWidget(bny_logo)
        left_widget.setLayout(left_layout)
        left_widget.setStyleSheet('''
        .QWidget {
            background-color: rgb(255, 255, 255);
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

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''
        QTabBar::tab{
        width: 0; height: 0; margin: 0; padding: 0; border: none;
        }
        ''')

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

    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Select a CSV file of data you would like to be standardized and select a CSV file of what the standards should be:'))

        comboBox = QComboBox(self)
        comboBox.addItem("Currencies")
        comboBox.addItem("Countries")
        comboBox.addItem("Languages")
        comboBox.setStyleSheet('''
        .QComboBox {
            text-align: center;
            }
            ''')
        comboBox.currentTextChanged.connect(self.combo_change)
        
        filename = "no file found"
        uploadButton = QPushButton('Upload Data CSV', self)
        uploadButton.resize(uploadButton.minimumSizeHint())
        uploadButton.move(200, 100)
        uploadButton.clicked.connect(self.open_file)

        uploadButtonStandards = QPushButton('Upload Standards CSV', self)
        uploadButtonStandards.resize(uploadButton.minimumSizeHint())
        uploadButtonStandards.move(200, 100)
        uploadButtonStandards.clicked.connect(self.open_file_standards)

        standardizeButton = QPushButton('Standardize', self)
        standardizeButton.resize(standardizeButton.minimumSizeHint())
        standardizeButton.move(350, 100)
        standardizeButton.clicked.connect(self.standardize)

        main_layout.addSpacing(25)
        main_layout.addWidget(comboBox)
        main_layout.addSpacing(25)
        main_layout.addWidget(uploadButton)
        main_layout.addSpacing(25)
        main_layout.addWidget(uploadButtonStandards)
        main_layout.addSpacing(25)
        main_layout.addWidget(standardizeButton)
        main_layout.addSpacing(500)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Fuzzy Matching Tool to be used to standardized data inputs into ISO standardized outputs\nBuilt with Python libraries PyQt and FuzzyWuzzy by Amruta Rao, Nicholas Rucker and Mac Guise'))
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

    def open_file (self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', '.')[0]

    def open_file_standards(self):
        self.filename_standards = QFileDialog.getOpenFileName(self, 'Open File', '.')[0]

    def combo_change(self, value):
        self.data_type = value

    def standardize(self):
        driver.main(self.data_type, self.filename, self.filename_standards)
        



def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()