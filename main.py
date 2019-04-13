from tkinter import *
def RSA(filename):

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
        p = nxtprimegen(int(input("Enter 1st number: ")))
        q = nxtprimegen(int(input("Enter 2nd number: ")))
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


    with open(filename, "rb") as image:
        f = image.read()
        msg = bytearray(f)
    en = []
    de = []
    print("msg: ", msg)
    for x in msg:
        en.append(pow(x, e, n))
    print("\nencrypt msg: ", en)
    ss = ""
    f3 = open(r'C:\Users\Inception\Desktop\pic\encrypt_file', 'w')
    for x in en:
        ss += (str(x) + " ")

    f3.write(ss)
    en2 = ss.split(" ")
    en.clear()
    for x in en2:
        if len(x) > 0:
            en.append(int(x))
    for x in en:
        de.append(pow(x, d, n))
    bytearray(de[:4])
    f2 = open(r'C:\Users\Inception\Desktop\pic\tt.txt', 'wb')
    f2.write(bytearray(de))
    f2.close()
    print("decrypt msg: ", de)
def file_take():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()
    filename = askopenfilename()
    RSA(filename)
    return filename

window = Tk()
lbl = Label(window, text="Enter a file: ")

lbl.grid(column=0, row=0)
window.title("Welcome to Shakib Secruity app")

window.geometry('500x300')

btn = Button(window, text="file",command=file_take)
btn.grid(column=1, row=0)
window.mainloop()



