import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QComboBox, QFileDialog, QPlainTextEdit, QLabel
from PyQt6.QtCore import Qt

from lsbEncode import encoderMain
from lsbDecode import decoderMain

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Encoding/Decoding")
        self.setFixedSize(333, 465)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setMenuWidget(centralWidget)
        self.windowTop()
        self.windowTopKeys()
        self.windowCenter()
        self.windowBottom()
        self.chooseImageButton.clicked.connect(self.openImage)
        self.comboBox.currentIndexChanged.connect(self.comboBoxChangeItems)
        self.chooseKeysFileButton.clicked.connect(self.openKeysFile)
        self.exit.clicked.connect(self.exitProgram)
        self.encodeOrDecode.clicked.connect(self.startWork)
    
    def windowTop(self):
        self.topLayout = QHBoxLayout()
        self.generalLayout.addLayout(self.topLayout)
        self.topLayout.setSpacing(3)
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Encrypt", "Decrypt"])
        self.imagePathLine = QLineEdit()
        self.imagePathLine.setReadOnly(True)
        self.imagePathLine.setText("")
        self.chooseImageButton = QPushButton("Image Browse...")
        self.comboBox.setFixedSize(75, 25)
        self.imagePathLine.setFixedSize(133, 25)
        self.chooseImageButton.setFixedSize(100, 25)
        self.topLayout.addWidget(self.comboBox)
        self.topLayout.addWidget(self.imagePathLine)
        self.topLayout.addWidget(self.chooseImageButton)
    
    def windowTopKeys(self):
        self.topLayoutKeys = QHBoxLayout()
        self.generalLayout.addLayout(self.topLayoutKeys)
        self.topLayoutKeys.setSpacing(1)
        self.keysPathLine = QLineEdit()
        self.keysPathLine.setReadOnly(True)
        self.keysPathLine.setText("")
        self.chooseKeysFileButton = QPushButton("Keys Browse...")
        self.keysPathLine.setFixedSize(183, 25)
        self.chooseKeysFileButton.setFixedSize(100, 25)
        self.keysPathLine.setEnabled(False)
        self.chooseKeysFileButton.setEnabled(False)
        self.topLayoutKeys.addWidget(self.keysPathLine)
        self.topLayoutKeys.addWidget(self.chooseKeysFileButton)

    def windowCenter(self):
        self.centerLayout = QVBoxLayout()
        self.generalLayout.addLayout(self.centerLayout)
        self.inputTextInfo = QLabel("Input text here:")
        self.messageFromOrToUser = QPlainTextEdit()
        self.messageFromOrToUser.setPlainText("")
        self.messageFromOrToUser.setFixedSize(315, 333)
        self.centerLayout.addWidget(self.inputTextInfo)
        self.centerLayout.addWidget(self.messageFromOrToUser)

    def windowBottom(self):
        self.bottomLayout = QHBoxLayout()
        self.generalLayout.addLayout(self.bottomLayout)
        self.exit = QPushButton("Exit")
        self.encodeOrDecode = QPushButton("Start Work")
        self.exit.setFixedSize(75, 25)
        self.encodeOrDecode.setFixedSize(75, 25)
        self.bottomLayout.addWidget(self.exit)
        self.bottomLayout.addWidget(self.encodeOrDecode)
        
    def openImage(self):
        self.imageFile = QFileDialog.getOpenFileName(self, "Choosen Image", None, "Image (*.png *.bmp *.jpg)")[0]
        self.imagePathLine.setText(self.imageFile)
    
    def switchName(self):
        pass
    
    def comboBoxChangeItems(self):
        if self.comboBox.currentIndex() == 0:
            self.keysPathLine.setEnabled(False)
            self.chooseKeysFileButton.setEnabled(False)
        elif self.comboBox.currentIndex() == 1:
            self.keysPathLine.setEnabled(True)
            self.chooseKeysFileButton.setEnabled(True)
    
    def openKeysFile(self):
        self.keysFile = QFileDialog.getOpenFileName(self, "Choosen Keys File", None, "Keys File (*.txt)")[0]
        self.keysPathLine.setText(self.keysFile)
    
    def exitProgram(self):
        QApplication.exit(0)
    
    def startWork(self):
        userText = self.messageFromOrToUser.toPlainText()

        if self.comboBox.currentIndex() == 0:
            if self.errors() == 0:
                self.messageFromOrToUser.setPlainText("Image file not chosen")
            elif self.errors() == 2:
                self.messageFromOrToUser.setPlainText("Input text please")
            else:
                encoderMain(self.imageFile, userText)
                self.messageFromOrToUser.setPlainText("Text is encoded\nImage and file with keys are in the program folder")
        if self.comboBox.currentIndex() == 1:
            if self.errors() == 0:
                self.messageFromOrToUser.setPlainText("Image file not chosen")
            elif self.errors() == 1:
                self.messageFromOrToUser.setPlainText("Keys file not chosen")
            else:
                self.messageFromOrToUser.setPlainText(decoderMain(self.imageFile, self.keysFile))
    
    def errors(self):
        if self.imagePathLine.displayText() == "":
            return 0
        elif self.comboBox.currentIndex() == 1:
            if self.keysPathLine.displayText() == "":
                return 1
        elif self.messageFromOrToUser.toPlainText() == "":
            return 2

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())