import random
from math import gcd
#  Pollard’s Rho Algorithm for Discrete Logarithm
def pollards_rho_dlp(g, h, p):
    """
    Solve g^x = h (mod p) using Pollard's Rho
    Assumes p is prime
    """

    def f(x, a, b):
        if x % 3 == 0:
            return (x * g) % p, (a + 1) % (p - 1), b
        elif x % 3 == 1:
            return (x * h) % p, a, (b + 1) % (p - 1)
        else:
            return (x * x) % p, (2 * a) % (p - 1), (2 * b) % (p - 1)

    # Initial values
    x1, a1, b1 = 1, 0, 0
    x2, a2, b2 = f(x1, a1, b1)

    while x1 != x2:
        x1, a1, b1 = f(x1, a1, b1)
        x2, a2, b2 = f(*f(x2, a2, b2))

    r = (b2 - b1) % (p - 1)
    if gcd(r, p - 1) != 1:
        raise ValueError("Failure: gcd != 1")

    x = ((a1 - a2) * pow(r, -1, p - 1)) % (p - 1)
    return x
#--------------
p = 23
g = 5
h = 8   # 5^6 mod 23

x = pollards_rho_dlp(g, h, p)
print("Discrete log x =", x)
print("Verification: g^x mod p =", pow(g, x, p))
#--------------
#  Pohlig–Hellman Algorithm
#helper function to factor n
from collections import Counter

def factorize(n):
    factors = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] += 1
    return factors
# Pohlig-Hellman algorithm
def pohlig_hellman(g, h, p):
    """
    Solve g^x = h (mod p) using Pohlig-Hellman
    Assumes p is prime
    """

    n = p - 1
    factors = factorize(n)
    congruences = []

    for q, e in factors.items():
        modulus = q ** e
        x_q = 0
        g_inv = pow(g, -1, p)

        for k in range(e):
            exp = n // (q ** (k + 1))
            gk = pow(g, exp, p)
            hk = pow(h * pow(g_inv, x_q, p), exp, p)

            # brute force small subgroup
            for d in range(q):
                if pow(gk, d, p) == hk:
                    x_q += d * (q ** k)
                    break

        congruences.append((x_q, modulus))

    # Chinese Remainder Theorem
    x = 0
    M = n

    for a_i, m_i in congruences:
        M_i = M // m_i
        inv = pow(M_i, -1, m_i)
        x += a_i * M_i * inv

    return x % M
#--------------
# Example usage:
p = 29     # p - 1 = 28 = 2^2 * 7
g = 2
h = 18

x = pohlig_hellman(g, h, p)
print("Discrete log x =", x)
print("Verification: g^x mod p =", pow(g, x, p))
#--------------
