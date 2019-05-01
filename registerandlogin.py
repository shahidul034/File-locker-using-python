from tkinter import *
import os

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
        p = nxtprimegen(random.randint(30,1000))
        q = nxtprimegen(random.randint(40,1010))
        print("prime: ", p, " ", q)
        n = p * q
        print("n: ",n)
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

    e, d, n = rsa()
    return e, d, n
def Decrypt():
    k1, k2, e, d, n = verify
    e = int(e)
    d = int(d)
    n = int(n)
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename()
    f3 = open(filename, 'r')
    msg = f3.read()
    en=[]
    de=[]
    en2 = msg.split(" ")
    fio=en2.pop(len(en2)-1)
    for x in en2:
        if len(x) > 0:
            en.append(int(x))
    for x in en:
        de.append(pow(x, d, n))
    bytearray(de[:4])
    stt = "C:\\Users\Inception\\Desktop\decrypt\\" + fio
    f2 = open(stt, 'wb')
    f2.write(bytearray(de))
    f2.close()
    #print("decrypt msg: ", de)
    print("Decrypted sucessfully")



def Encrypt():
    global fi
    #print("VV: ", verify)
    k1,k2,e,d,n=verify
    e=int(e)
    d=int(d)
    n=int(n)
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename()
    dd=filename.split('/')
    fi=dd[len(dd)-1]
    with open(filename, "rb") as image:
        f = image.read()
        msg = bytearray(f)
    en = []
    #print("msg: ", msg)
    for x in msg:
        en.append(pow(x, e, n))
    #print("\nencrypt msg: ", en)
    ss = ""
    fii=fi.split('.')
    stt="C:\\Users\Inception\\Desktop\encrypt\\"+fii[0]
    f3 = open(stt ,'w')
    for x in en:
        ss += (str(x) + " ")
    ss+=(fi)
    f3.write(ss)
    print("Encrypted sucessfully")



def encrypt_decrypt():
    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("300x250")
    Button(screen5, text="Encrypt", command=Encrypt).pack()
    Button(screen5, text="Decrypt", command=Decrypt).pack()


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
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =encrypt_decrypt).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()

  
def register_user():
  print("working")
  e,d,n=RSA()
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info+"\n")
  file.write(str(e) + "\n")
  file.write(str(d) + "\n")
  file.write(str(n))
  file.close()



  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  global verify
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    #print("verify: ",verify)
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

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Notes 1.0")
  Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
  
