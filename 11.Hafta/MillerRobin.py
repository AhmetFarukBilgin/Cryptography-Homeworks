import random

def miller_rabin(n, k=10):
    """
    Miller–Rabin Primality Test
    n : test edilecek sayı
    k : güvenlik parametresi (tur sayısı)
    """

    # Küçük ve özel durumlar
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # n-1 = 2^r * d olacak şekilde ayrıştır
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # k adet rastgele taban ile test
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)   # a^d mod n

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # kesin bileşik

    return True  # büyük ihtimalle asal
