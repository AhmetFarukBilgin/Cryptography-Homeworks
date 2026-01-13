def generalized_crt(congruences):
    """
    congruences = [(a1, n1), (a2, n2), ...]
    returns (x, N) or None
    """
    a, n = congruences[0]

    for ai, ni in congruences[1:]:
        result = crt_pair(a, n, ai, ni)
        if result is None:
            return None
        a, n = result

    return a, n
def crt_pair(a1, n1, a2, n2):
    g, s, t = extended_gcd(n1, n2)

    # Çözüm var mı?
    if (a2 - a1) % g != 0:
        return None  # no solution

    lcm = n1 * n2 // g

    # Birleştirilmiş çözüm
    x = (a1 + (a2 - a1) // g * s % (n2 // g) * n1) % lcm
    return x, lcm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
#Case1 Klasik CRT
print(generalized_crt([
    (2, 3),
    (3, 5),
    (2, 7)
]))
#Case2 Aralarında Asal Olmayan Modüller
print(generalized_crt([
    (2, 4),
    (6, 8)
]))
#Case3 Çözüm Olmayan Durum
print(generalized_crt([
    (1, 4),
    (3, 6)
]))
#Case4 Daha büyük sayılar
print(generalized_crt([
    (123, 1000),
    (623, 1500),
    (2123, 2500)
]))
