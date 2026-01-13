def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)
import random

def diffie_hellman_verbose():
    print("🔐 DIFFIE–HELLMAN KEY EXCHANGE (STEP-BY-STEP)\n")

    # 1️⃣ Public parameters
    p = 23   # Prime modulus (toy example)
    g = 5    # Generator

    print("📢 PUBLIC PARAMETERS (known to everyone)")
    print(f"Prime (p)       = {p}")
    print(f"Generator (g)   = {g}\n")

    # 2️⃣ Alice generates private key
    a = random.randint(1, p - 2)
    print("👩 Alice")
    print(f"Private key (a) = {a}")

    # Alice computes public key
    A = pow(g, a, p)
    print(f"Public key A = g^a mod p = {g}^{a} mod {p} = {A}\n")

    # 3️⃣ Bob generates private key
    b = random.randint(1, p - 2)
    print("👨 Bob")
    print(f"Private key (b) = {b}")

    # Bob computes public key
    B = pow(g, b, p)
    print(f"Public key B = g^b mod p = {g}^{b} mod {p} = {B}\n")

    # 4️⃣ Public key exchange
    print("📡 PUBLIC KEY EXCHANGE")
    print(f"Alice sends A = {A} to Bob")
    print(f"Bob sends B   = {B} to Alice\n")

    # 5️⃣ Shared secret computation
    print("🔑 SHARED SECRET COMPUTATION")

    alice_shared = pow(B, a, p)
    print(f"Alice computes: K = B^a mod p = {B}^{a} mod {p} = {alice_shared}")

    bob_shared = pow(A, b, p)
    print(f"Bob computes:   K = A^b mod p = {A}^{b} mod {p} = {bob_shared}\n")

    # 6️⃣ Verification
    print("✅ VERIFICATION")
    if alice_shared == bob_shared:
        print(f"Shared secret MATCHES: K = {alice_shared}")
    else:
        print("❌ Shared secrets DO NOT match!")

    print("\n🕵️ What an attacker sees:")
    print(f"p = {p}, g = {g}, A = {A}, B = {B}")
    print("❌ Cannot compute private keys (Discrete Logarithm Problem)")

# Run the demonstration
diffie_hellman_verbose()
