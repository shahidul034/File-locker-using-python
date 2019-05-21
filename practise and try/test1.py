# MD Shahidul Salim (Shakib)
# ROll: 1507034
# CSE,KUET

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import math



def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x

def nxtprimegen(n):
    m = n
    n = n + 100
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            if p > m:
                return p
            else:
                val = p

    return val


def rsa(p,q):
    p=nxtprimegen(p)
    q=nxtprimegen(q)
    print("prime: ", p, " ", q)
    n = p * q
    print("n: ", n)
    tor = (p - 1) * (q - 1)
    e = 2
    while (1):
        if math.gcd(e, tor) == 1:
            break
        else:
            e += 1
    print("public key: ", e)
    d = modInverse(e, tor)
    if d == 1:
        print("no multiplicative_inverse")
        return

    print("private key: ", d)
    return e, d, n



class App(QMainWindow):
    n=0
    e=0
    d=0
    pp=0
    qq=0
    filename=""
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
        self.label = QLabel("Enter  1st prime number: " , self)
        self.label.move(20, 10)
        self.label.resize(280, 40)


        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 40)
        self.textbox.resize(280, 40)

        self.label = QLabel("Enter  2nd prime number: ", self)
        self.label.move(20, 70)
        self.label.resize(280, 40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 110)
        self.textbox2.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Key generate', self)
        self.button.move(20, 150)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)



        self.button2 = QPushButton('Open your file', self)
        self.button2.move(20, 190)
        self.button2.clicked.connect(self.openFileNameDialog)

        self.button3 = QPushButton('Encrypt', self)
        self.button3.move(20, 240)
        self.button3.clicked.connect(self.encrypt)
        self.show()


    def encrypt(self):
        with open(self.filename, "rb") as image:
            f = image.read()
            msg = bytearray(f)
        en = []
        de = []
        print("msg: ", msg)
        for x in msg:
            en.append(pow(x, self.e, self.n))
        print("\nencrypt msg: ", en)
        ss = ""
        f3 = open(r'C:\Users\Inception\PycharmProjects\File locker\pic\encrypt_file', 'w')
        for x in en:
            ss += (str(x) + " ")

        f3.write(ss)



    @pyqtSlot()
    def on_click(self):
        p = self.textbox.text()
        self.pp=int(p)
        q = self.textbox2.text()
        self.qq = int(q)
        self.e, self.d, self.n = rsa(self.pp,self.qq)



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