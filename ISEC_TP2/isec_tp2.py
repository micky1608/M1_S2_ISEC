
import numpy as np

##########################################################################################################################

def poly_binary_add(A,B):
    res = np.polyadd(A,B)
    res = np.remainder(res,2)
    return np.poly1d(res)

##########################################################################################################################

def poly_binary_mul(A,B):
    res = np.polymul(A,B)
    res = np.remainder(res,2)
    return np.poly1d(res)

##########################################################################################################################

def EEA(A,B):
    # R = Ri
    # RP = R(i+1)
    # RS = R(i+2)

    R = A
    U = np.poly1d([1])
    V = np.poly1d([0])

    RP = B
    UP = np.poly1d([0])
    VP = np.poly1d([1])

    while RP.order != 0:
        quotient,remainder = np.polydiv(R,RP)

        Q = np.remainder(quotient,2)

        RS = np.poly1d(np.remainder(remainder , 2))
        US = np.poly1d(U - poly_binary_mul(Q,UP))
        VS = np.poly1d(V - poly_binary_mul(Q,VP))

        R = RP
        RP = RS

        U = UP
        UP = US

        V = VP
        VP = VS

    return np.remainder(UP,2),np.remainder(VP,2)

##########################################################################################################################

def inv_mod(A,P):
    if A.order == 0 and A.coef[0] == 0:
        return [0]
    U,V = EEA(A,P)
    return U

##########################################################################################################################

def aes_sbox(alpha , m):
    inv_alpha = inv_mod(alpha , m)

    if(len(inv_alpha) < 8):
        inv_alpha = np.hstack((np.zeros(8-len(inv_alpha)) , inv_alpha))

    A = np.matrix([ [1,0,0,0,1,1,1,1],
                    [1,1,0,0,0,1,1,1],
                    [1,1,1,0,0,0,1,1],
                    [1,1,1,1,0,0,0,1],
                    [1,1,1,1,1,0,0,0],
                    [0,1,1,1,1,1,0,0],
                    [0,0,1,1,1,1,1,0],
                    [0,0,0,1,1,1,1,1] ] )


    Y = [1, 1, 0, 0, 0, 1, 1, 0]

    res = np.array(((np.dot(A,list(reversed(inv_alpha))) + Y) % 2).T)

    b = 0

    for i in range(len(res)):
        b += pow(2, i) if res[i] == 1 else 0

    return b

###################################################################################################################################

def aes_sbox_inv(beta,m):

    M = np.matrix([[0, 0, 1, 0, 0, 1, 0, 1],
                   [1, 0, 0, 1, 0, 0, 1, 0],
                   [0, 1, 0, 0, 1, 0, 0, 1],
                   [1, 0, 1, 0, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0, 0, 1, 0],
                   [0, 0, 1, 0, 1, 0, 0, 1],
                   [1, 0, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 0, 1, 0, 1, 0]])

    Y = [1,0,1,0,0,0,0,0]

    beta = beta.coef

    if (len(beta) < 8):
        beta = np.hstack((np.zeros(8 - len(beta)), beta))

    beta = list(reversed(beta))

    temp = np.poly1d(list(reversed(np.squeeze(np.asarray((np.dot(M,beta) + Y) % 2)))))

    inv = inv_mod(temp,m)

    b = 0

    for i in range(len(inv)):
        b += pow(2, len(inv)-1-i) if inv[i] == 1 else 0

    return b

###################################################################################################################################

def pol_from_hexa(h1,h2):
    h = h1*16+h2
    mask = 128
    binary_array = []

    for i in range(8):
         binary_array.append(1 if h & mask else 0)
         mask = mask >> 1

    return np.poly1d(binary_array)

###################################################################################################################################

def show_hexa_table(table):
    for i in range(0x10):
        for j in range(0x10):
            print(hex(int(table[i][j])) , end=' ' if j!=0xF else '\n')



###################################################################################################################################




alpha = np.poly1d([1,1,0,1,1,0,0,1])
m = np.poly1d([1,0,0,0,1,1,0,1,1])

AES_table = np.zeros((16,16))
AES_inv_table = np.zeros((16,16))

for i in range(0x10):
    for j in range(0x10):
        AES_table[i][j] = aes_sbox(pol_from_hexa(i,j) , m)
        AES_inv_table[i][j] = aes_sbox_inv(pol_from_hexa(i, j), m)


show_hexa_table(AES_table)
print("\n**********************************************************************************************\n")
show_hexa_table(AES_inv_table)

