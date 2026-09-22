"""
Number Theory & Fast Polynomial Multiplication:
1. Number Theoretic Transform (NTT) modulo 998244353 in O(N log N)
2. Miller-Rabin Primality Test & Pollard's Rho Integer Factorization
"""

from typing import List
import random
import math

MOD = 998244353
G = 3

def ntt(a: List[int], invert: bool = False):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = pow(G, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        for i in range(0, n, length):
            w = 1
            for k in range(length // 2):
                u = a[i + k]
                v = (a[i + k + length // 2] * w) % MOD
                a[i + k] = (u + v) % MOD
                a[i + k + length // 2] = (u - v + MOD) % MOD
                w = (w * wlen) % MOD
        length <<= 1

    if invert:
        n_inv = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * n_inv) % MOD

def multiply_polynomials_ntt(p1: List[int], p2: List[int]) -> List[int]:
    n = 1
    while n < len(p1) + len(p2):
        n <<= 1
    a = p1 + [0] * (n - len(p1))
    b = p2 + [0] * (n - len(p2))
    ntt(a, False)
    ntt(b, False)
    c = [(a[i] * b[i]) % MOD for i in range(n)]
    ntt(c, True)
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c
