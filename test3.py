import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    de_key=0
    filename=""
    n=0

    def __init__(self):
        super().__init__()
        self.title = 'Welcome to Shakib secruity app'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 400
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 60)
        self.textbox2.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 100)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)



        self.button2 = QPushButton('Enter', self)
        self.button2.move(20, 140)
        self.button2.clicked.connect(self.openFileNameDialog)

        self.button3 = QPushButton('Decrypt', self)
        self.button3.move(20, 180)
        self.button3.clicked.connect(self.decrypt)
        self.show()


    def decrypt(self):
        en = []
        de = []
        f3 = open(self.filename, 'r')
        str2=f3.read()
        en2 = str2.split(" ")
        for x in en2:
            if len(x) > 0:
                en.append(int(x))
        for x in en:
            de.append(pow(x, self.de_key, self.n))
        bytearray(de[:4])
        f2 = open(r'C:\Users\Inception\Desktop\pic\decypt_now.jpg', 'wb')
        f2.write(bytearray(de))
        f2.close()
        print("decrypt msg: ", de)




    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        self.de_key=int(textboxValue)
        textboxValue2 = self.textbox2.text()
        self.n = int(textboxValue2)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.filename = fileName

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())