def modInverse(a, m) :
	m0 = m
	y = 0
	x = 1
	if (m == 1) :
		return 0
	while (a > 1) :

		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t

	if (x < 0) :
		x = x + m0

	return x


def strtonum(st2):
    ss=""
    for x in range(len(st2)):
        m=ord(st2[x])
        if x!=len(st2)-1:
            k=str(m)
            ss+=(k+"_")
        else:
            ss+=str(m)
    return ss
def numtostr(st2):
    st=st2.split("_")
    ss=""
    for x in st:
        ss+=chr(int(x))
    return ss
def en_elgamal(msg):
    msg = strtonum(msg)

    msg=msg.split("_")
    E1, E2, p= 5, 154504, 234527
    R =456
    ss=""
    for x in range(len(msg)):
        C2 = pow((pow(E2, R, p) * int(msg[x])), 1, p)
        if x!=len(msg)-1:
            ss+=(str(C2)+"_")
        else:
            ss+=str(C2)
    return ss

def de_elgamal(msg):
    msg=msg.split("_")
    E1, E2, p = 5, 154504, 234527
    d= 345
    R = 456
    ss=""
    C1 = pow(E1, R, p)
    for x in msg:
        de_msg = pow((modInverse(pow(C1, d), p) * int(x)), 1, p)
        ss+=chr(de_msg)
    return ss
mm="tere435liya34534"

print(en_elgamal(mm))
k=en_elgamal(mm)
print(de_elgamal(k))

