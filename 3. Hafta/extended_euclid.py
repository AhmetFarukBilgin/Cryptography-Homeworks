def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
# Example usage:
gcd, x, y = extended_euclid(4895, 1452)
print(f"GCD: {gcd}, x: {x}, y: {y}")