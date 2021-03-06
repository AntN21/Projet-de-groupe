import numpy as np
import random as rd

def Binomiale(p):
    if rd.random() < p:
        return 1
    else:
        return 0

def loi_uniforme(K):
    res = np.ones(K)/K
    return res

def W_SSBM(K, a, b):
    res = np.zeros((K,K))
    for i in range(K):
        for j in range(K):
            if i == j:
                res[i, j] = a
            else:
                res[i, j] = b
    return res


def tirage(PI):
    s=0
    U=rd.random()
    i=-1
    while U>s:
        s+=PI[i]
        i+=1
    return i

n=10
K=2
PI=loi_uniforme(K)

def gen(n,K,a,b,PI):
    A=np.zeros((n,n))
    X=[tirage(PI) for i in range(n)]
    W=W_SSBM(K, a, b)
    for i in range(n):
        for j in range(n):
            if (i<j):
                A[i,j]+=Binomiale(W[X[i],X[j]])
    A=A+np.transpose(A)

    return A
print(gen(n,K,0.25,0.75,PI))
