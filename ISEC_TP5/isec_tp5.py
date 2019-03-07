
import numpy as np
import random

# find a generator of the group Z/pZ
# a generator is that gcd(g,p) = 1
def group_generator(P):
    g = random.randint(3,P)
    while np.gcd(g,P) != 1:
        g = random.randint(2, P)

    return g


####################################################################################################################################

def random_prime(lim):
    p = 0
    while True:
        p = random.randint(3,lim)
        if Fermat_Test(p):
            break
    return p

####################################################################################################################################

def Fermat_Test(p):
    N = 100

    if p==2:
        return True

    if p%2 == 0:
        return False

    for i in range(N):
        #while True:
        a = random.randint(2,p-2)
            #if np.gcd(a,p) == 1:
                #break
        b = pow(a,p-1)%p
        if b != 1:
            return False

    return True

####################################################################################################################################

def generate_key():
    lim = 10000
    p = random_prime(lim)
    g = group_generator(p)
    x = random.randint(2,p-2)
    print("x : ",x)
    y = pow(g,x) % p
    return p,g,y

####################################################################################################################################

p,g,y = generate_key()

print("Public key ->\tp : ",p,"\tg : ",g,"\ty : ",y)