import random

import numpy as np


def EEA(A,B):
    # R = Ri
    # RP = R(i+1)
    # RS = R(i+2)

    R = A
    U = 1
    V = 0

    RP = B
    UP = 0
    VP = 1

    while RP != 0:
        Q = int(R/RP)
        RS = R - Q*RP
        US = U - Q*UP
        VS = V - Q*VP

        R = RP
        RP = RS

        U = UP
        UP = US

        V = VP
        VP = VS

    return U,V

#######################################################################################################################

def inv(a,P):
    u,v = EEA(a,P)
    return u if u>0 else u+P

#######################################################################################################################

# N is the number of iterations
def Fermat_Test(p):
    N = 1000
    for i in range(N):

        while True:
            a = random.randint(2,p-2)
            if np.gcd(a,p) == 1:
                break

        b = pow(a,p-1)%p
        if b != 1:
            return False

    return True

#######################################################################################################################

# return (N,e,d,p,q)
# N must be composed of k bits
# Suppose that k is even
def RSA(k):

    while True:
        p = random.getrandbits(int(k/2))
        if p>3 and Fermat_Test(p):
            break

    while True:
        q = random.getrandbits(int(k/2))
        if q>3 and Fermat_Test(q) and q != p:
            break

    N = p*q
    phi = (p-1)*(q-1)

    while True:
        e = random.randint(1 , phi-1)
        if np.gcd(e,phi) == 1:
            break


    d = inv(e,phi)

    return N,e,d,p,q

#######################################################################################################################

def RSA_cipher(m,N,e):
    return pow(m,e)%N

#######################################################################################################################

def RSA_decipher(c,N,d):
    return pow(c,d)%N

N,e,d,p,q = RSA(10)

print("N : ",N)
print("e : ",e)
print("d : ",d)
print("p : ",p)
print("q : ",q)



m = 123456789 % N

c = RSA_cipher(m,N,e)
m2 = RSA_decipher(c,N,d)

print("m : ",m," c : ",c, " m2 : ",m2)


