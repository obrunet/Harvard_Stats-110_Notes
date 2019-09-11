import numpy as np
from math import factorial

def nPr(n, r):
    return factorial(n)/(factorial(n-r))


def nCr(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))


def enum_order_matters_no_replacement(n, r):
    
    n_new = n + r - 1
    
    return nCr(n_new, r)


def vandermonde(m, n, k):
    
    vander_sum = 0
    
    for i in range(k):
        vander_sum += nCr(m, i) * nCr(n, (k-i))
        
    return vander_sum


def bernouli(p, x=1):
    if x == 1:
        return p
    else:
        return 1-p


def binomial(n, p, k):
    return nCr(n, k) * p**k * (1-p)**(n-k)


def hypergeometic(w, b, n, k):
    return nCr(w, k)*nCr(b, (n-k))/nCr((w+b), n)


def Main():
    
    pass


if __name__ == '__main__':
    Main()
    