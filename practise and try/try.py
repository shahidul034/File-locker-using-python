#1 MD Shahidul Salim (Shakib)
# ROll: 1507034
# CSE,KUET


from tkinter import *
import os



def numtostr(st2):
    st = st2.split("_")
    ss = ""
    for x in st:
        ss += chr(int(x))
    return ss

def strtonum(st2):
    ss = ""
    for x in range(len(st2)):
        m = ord(st2[x])
        if x != len(st2) - 1:
            k = str(m)
            ss += (k + "_")
        else:
            ss += str(m)
    return ss



def en_elgamal(msg):
    msg = strtonum(msg)

    msg = msg.split("_")
    E1, E2, p = 5, 154504, 234527
    R = 456
    ss = ""
    for x in range(len(msg)):
        C2 = pow((pow(E2, R, p) * int(msg[x])), 1, p)
        if x != len(msg) - 1:
            ss += (str(C2) + "_")
        else:
            ss += str(C2)
    return ss


def de_elgamal(msg):
    msg = msg.split("_")
    E1, E2, p = 5, 154504, 234527
    d = 345
    R = 456
    ss = ""
    C1 = pow(E1, R, p)
    for x in msg:
        de_msg = pow((modInverse(pow(C1, d), p) * int(x)), 1, p)
        ss += chr(de_msg)
    return ss

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

def RSA():
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

    def rsa():
        import random
        p = nxtprimegen(random.randint(30, 1000))
        q = nxtprimegen(random.randint(40, 1010))
        # print("prime: ", p, " ", q)
        n = p * q
        # print("n: ",n)
        tor = (p - 1) * (q - 1)
        e = 2
        while (1):
            if math.gcd(e, tor) == 1:
                break
            else:
                e += 1
        # print("public key: ", e)
        d = modInverse(e, tor)
        if d == 1:
            print("no multiplicative_inverse")
            return

        # print("private key: ", d)
        return e, d, n

    e, d, n = rsa()
    return e, d, n


def Decrypt():
    k1, k2, e, d, n = verify
    k1, k2, e, d, n = de_elgamal(k1), de_elgamal(k2), de_elgamal(e), de_elgamal(d), de_elgamal(n)
    e = int(e)
    d = int(d)
    n = int(n)
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename(initialdir="C:\\Users\\Inception\\Desktop\\test\\" + (k1))
    f3 = open(filename, 'r')
    msg = f3.read()
    en = []
    de = []
    en2 = msg.split(" ")
    fio = en2.pop(len(en2) - 1)
    for x in en2:
        if len(x) > 0:
            en.append(int(x))
    for x in en:
        de.append(pow(x, d, n))
    bytearray(de[:4])
    stt = "C:\\Users\\Inception\\Desktop\\test\\" + (k1) + "\\" + fio
    f2 = open(stt, 'wb')
    f2.write(bytearray(de))
    f2.close()
    # print("decrypt msg: ", de)
    print("Decrypted sucessfully")


def strtonum(st2):
    ss = ""
    for x in range(len(st2)):
        m = ord(st2[x])
        if x != len(st2) - 1:
            k = str(m)
            ss += (k + "_")
        else:
            ss += str(m)
    return ss


def numtostr(st2):
    st = st2.split("_")
    ss = ""
    for x in st:
        ss += chr(int(x))
    return ss


def Encrypt():
    global fi
    k1, k2, e, d, n = verify
    k1, k2, e, d, n = de_elgamal(k1), de_elgamal(k2), de_elgamal(e), de_elgamal(d), de_elgamal(n)
    e = int(e)
    d = int(d)
    n = int(n)
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename(initialdir="C:\\Users\\Inception\\Desktop\\test\\" + "sample")
    dd = filename.split('/')
    fi = dd[len(dd) - 1]
    with open(filename, "rb") as image:
        f = image.read()
        msg = bytearray(f)
    en = []
    # print("msg: ", msg)
    for x in msg:
        en.append(pow(x, e, n))
    # print("\nencrypt msg: ", en)
    ss = ""
    fii = fi.split('.')
    stt = "C:\\Users\\Inception\\Desktop\\test\\" + k1 + "\\" + fii[0]
    f3 = open(stt, 'w')
    for x in en:
        ss += (str(x) + " ")
    ss += (fi)
    f3.write(ss)
    print("Encrypted sucessfully")
    os.remove(filename)


def file_show():
    k1, k2, e, d, n = verify
    k1, k2, e, d, n = de_elgamal(k1), de_elgamal(k2), de_elgamal(e), de_elgamal(d), de_elgamal(n)

    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename(initialdir="C:\\Users\\Inception\\Desktop\\test\\" + k1)
    f3 = open(filename, 'rb')
    ss = filename.split("/")
    ss2 = ss[len(ss) - 1]
    msg = f3.read()
    f2 = open("C:\\Users\\Inception\\Desktop\\" + ss2, 'wb')
    f2.write(msg)
    str_show("Save in desktop")


def encrypt_decrypt():
    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("300x250")
    Button(screen5, text="Encrypt", command=Encrypt).pack()
    Button(screen5, text="Decrypt", command=Decrypt).pack()
    Button(screen5, text="Show my file", command=file_show).pack()


def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("300x250")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=encrypt_decrypt).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    e, d, n = RSA()
    username_info = username.get()
    password_info = password.get()

    list_of_files = os.listdir("C:\\Users\\Inception\\Desktop\\test")

    if username_info in list_of_files:
        str_show("user already exist")
        # Label(screen1, text="user already exist", fg="green", font=("calibri", 11)).pack()

    else:
        dir_name = "C:\\Users\\Inception\\Desktop\\test\\" + username_info
        dirName = dir_name

        try:
            # Create target Directory
            os.mkdir(dirName)
        except FileExistsError:
            print("Directory ", dirName, " already exists")
        dirName = dirName + "\\" + username_info
        file = open(dirName, "w")
        file.write(en_elgamal(username_info) + "\n")
        file.write(en_elgamal(password_info) + "\n")
        file.write(en_elgamal(str(e)) + "\n")
        file.write(en_elgamal(str(d)) + "\n")
        file.write(en_elgamal(str(n)))
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
        login()


def delete8():
    screen8.destroy()



def str_show(ss):
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("msg")
    screen8.geometry("150x100")
    Label(screen8, text=ss).pack()
    Button(screen8, text="OK", command=delete8).pack()
def login_verify():
    global verify
    username1 = username_verify.get()
    password1 = password_verify.get()
    password1 = en_elgamal(password1)
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir("C:\\Users\\Inception\\Desktop\\test")

    if username1 in list_of_files:
        file1 = open("C:\\Users\\Inception\\Desktop\\test\\" + username1 + "\\" + username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Welcome Avengers End game secruity app")
    Label(text="Avengers End game", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()

