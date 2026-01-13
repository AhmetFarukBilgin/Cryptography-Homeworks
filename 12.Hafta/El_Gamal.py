"""
ElGamal Kripto Sistemi - Eğitim Implementasyonu

ElGamal, Diffie–Hellman anahtar değişimine dayanan bir açık anahtarlı şifreleme sistemidir.
Taher ElGamal tarafından 1984 yılında geliştirilmiş, asimetrik kriptografi alanında önemli bir algoritmadır.

TEMEL PRENSİPLER:
─────────────────
1. Asal modül p ve generator g seçilir
2. Her kullanıcı gizli anahtar x seçer: x ∈ [2, p-2]
3. Açık anahtar y hesaplanır: y = g^x (mod p)
4. Şifreleme: Her mesaj için rastgele k seçilir
   - c₁ = g^k (mod p)
   - c₂ = m × y^k (mod p)
5. Çözme: c₂ × (c₁^x)^(-1) (mod p)

GÜVENLİK:
─────────
Ayrık Logaritma Problemi (DLP) zorluğuna dayanır:
- y = g^x (mod p) verilirse, x'i bulmak zordur
- Her mesaj için farklı k kullanıldığından, aynı mesaj farklı şifreli metinler verir (semantik güvenlik)

DİKKAT:
───────
Bu kod eğitim amaçlıdır. Üretim ortamında:
- cryptography veya PyCryptodome kütüphanelerini kullanın
- Çok daha büyük asal sayılar kullanın (2048+ bit)
- Güvenilir randomness kaynağı kullanın
"""

import random
from math import gcd


# ============================================================================
# BÖLÜM 1: Temel Matematik Fonksiyonları
# ============================================================================

def extended_gcd(a, b):
    """
    Genişletilmiş Öklid Algoritması
    
    Amaç: ax + by = gcd(a, b) denklemini sağlayan x ve y değerlerini bulur
    
    Parametreler:
        a, b: İki pozitif tam sayı
        
    Dönüş:
        (gcd, x, y): Tuple olarak gcd, x ve y değerleri
    """
    if b == 0:
        return a, 1, 0
    
    gcd_value, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_value, x, y


def mod_inverse(element, modulus):
    """
    Modüler Çarpma Tersini Hesapla
    
    Amaç: element × x ≡ 1 (mod modulus) denkleminde x değerini bulur
    
    Matematiksel Form:
        element^(-1) (mod modulus)
    
    Parametreler:
        element: Tersini almak istediğimiz sayı
        modulus: Modulus (genellikle asal p)
        
    Dönüş:
        Modüler ters (x öyle ki: element × x ≡ 1 (mod modulus))
        
    Hata:
        ValueError: Eğer gcd(element, modulus) != 1 ise modüler ters yoktur
    """
    gcd_value, x, _ = extended_gcd(element, modulus)
    
    if gcd_value != 1:
        raise ValueError(f"Hata: gcd({element}, {modulus}) = {gcd_value}. "
                        f"Modüler ters mevcut değil!")
    
    return x % modulus


def is_prime(number):
    """
    Asal Sayı Testi (Basit - Eğitim Amaçlı)
    
    Not: Gerçek uygulamalar için Miller–Rabin testleri kullanılmalı.
    
    Parametreler:
        number: Test edilecek sayı
        
    Dönüş:
        True: Asal
        False: Bileşik
    """
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True


def is_generator(g, p):
    """
    g'nin p (asal) modunda generator olup olmadığını kontrol et
    
    Teorik Açıklama:
    g, Z_p* grubunun üreteci ise, g^k ≠ 1 (mod p) olur tüm 1 ≤ k < p-1 için.
    
    Parametreler:
        g: Kontrol edilecek eleman
        p: Asal modulus
        
    Dönüş:
        True: g bir generatördür
        False: g bir generatör değildir
    """
    if g >= p or g < 2:
        return False
    
    # Küçük asal faktörleri kontrol et
    # p-1 = 2 × q (q asal) durumunda
    if pow(g, (p - 1) // 2, p) == 1:
        return False
    
    return pow(g, p - 1, p) == 1


# ============================================================================
# BÖLÜM 2: ElGamal Parametreleri Kurulumu
# ============================================================================

def setup_system(p=467, g=2, verbose=True):
    """
    ElGamal Sistemi Parametrelerini Kur
    
    Parametreler:
        p: Asal modulus (küçük örnekler için 467 yeterli)
        g: Grup üreteci (primitive root mod p)
        verbose: Ayrıntılı çıktı yazdırılsın mı?
        
    Dönüş:
        (p, g): Sistemi kurmak için gerekli parametreler
    """
    if not is_prime(p):
        raise ValueError(f"{p} asal sayı değildir!")
    
    if not is_generator(g, p):
        raise ValueError(f"{g}, {p} modunda generator değildir!")
    
    if verbose:
        print("\n" + "="*70)
        print("ELGAMAL SİSTEMİ KURULUMU")
        print("="*70)
        print(f"\nSistem Parametreleri:")
        print(f"  p (Asal Modulus): {p}")
        print(f"  g (Generator):    {g}")
        print(f"  Grup Mertebesi:   {p-1}")
        print("="*70 + "\n")
    
    return p, g


# ============================================================================
# BÖLÜM 3: Anahtar Üretimi
# ============================================================================

def generate_keys(p, g, verbose=True):
    """
    ElGamal Açık ve Gizli Anahtarlarını Üret
    
    Adımlar:
        1. Gizli anahtar x ∈ [2, p-2] arasında seçilir
        2. Açık anahtar y = g^x (mod p) hesaplanır
    
    Matematiksel Form:
        Gizli anahtar: x ← Zₚ*
        Açık anahtar:  y = g^x mod p
    
    Parametreler:
        p: Asal modulus
        g: Generator
        verbose: Ayrıntılı çıktı yazdırılsın mı?
        
    Dönüş:
        public_key: (p, g, y) - Herkese açık
        private_key: x - Gizli tutulur
    """
    # Gizli anahtar seçimi
    private_key = random.randint(2, p - 2)
    
    # Açık anahtar hesaplaması: y = g^x (mod p)
    public_key_y = pow(g, private_key, p)
    
    public_key = (p, g, public_key_y)
    
    if verbose:
        print("\n" + "="*70)
        print("ELGAMAL ANAHTAR ÜRETİMİ")
        print("="*70)
        print(f"\n[Adım 1] Gizli Anahtar Seçimi:")
        print(f"  x ∈ [2, {p-2}] arasından rastgele seçildi")
        print(f"  x = {private_key}")
        
        print(f"\n[Adım 2] Açık Anahtar Hesaplaması:")
        print(f"  y = g^x mod p")
        print(f"  y = {g}^{private_key} mod {p}")
        print(f"  y = {public_key_y}")
        
        print(f"\n" + "="*70)
        print("SONUÇ - ANAHTARLAR")
        print("="*70)
        print(f"Açık Anahtar (Public Key):   (p={p}, g={g}, y={public_key_y})")
        print(f"Gizli Anahtar (Private Key): x = {private_key}")
        print(f"\nAçık anahtar herkese gösterilebilir.")
        print(f"Gizli anahtar kesinlikle gizli tutulmalıdır!")
        print("="*70 + "\n")
    
    return public_key, private_key


# ============================================================================
# BÖLÜM 4: Şifreleme
# ============================================================================

def encrypt(message, public_key, verbose=True):
    """
    ElGamal Şifreleme Fonksiyonu
    
    Adımlar:
        1. Şifreleme için rastgele k ∈ [2, p-2] seçilir
        2. c₁ = g^k (mod p) hesaplanır
        3. s = y^k (mod p) hesaplanır (paylaşılan gizli)
        4. c₂ = m × s (mod p) hesaplanır
    
    Matematiksel Form:
        Giriş: m (mesaj), (p, g, y)
        k ← Z*ₚ rastgele
        c₁ = g^k mod p
        c₂ = m × y^k mod p
        Çıkış: (c₁, c₂)
    
    Parametreler:
        message: Şifrelenecek mesaj (sayı, 0 < message < p)
        public_key: (p, g, y) tuple
        verbose: Ayrıntılı çıktı yazdırılsın mı?
        
    Dönüş:
        ciphertext: (c₁, c₂) tuple - Şifreli metin
    """
    p, g, public_key_y = public_key
    
    # Validasyon
    if message >= p or message <= 0:
        raise ValueError(f"Mesaj (m={message}) aralıkta [1, {p-1}] olmalıdır!")
    
    # Adım 1: Rastgele k seç (her şifreleme için farklı olmalı!)
    encryption_random = random.randint(2, p - 2)
    
    if verbose:
        print("\n" + "="*70)
        print("ELGAMAL ŞİFRELEME")
        print("="*70)
        print(f"\nGiriş Mesajı: m = {message}")
        print(f"Açık Anahtar: (p={p}, g={g}, y={public_key_y})")
    
    # Adım 2: c₁ = g^k (mod p)
    c1 = pow(g, encryption_random, p)
    
    if verbose:
        print(f"\n[Adım 1] Rastgele Sayı Seçimi:")
        print(f"  k = {encryption_random}")
        
        print(f"\n[Adım 2] c₁ = g^k mod p Hesaplaması:")
        print(f"  c₁ = {g}^{encryption_random} mod {p}")
        print(f"  c₁ = {c1}")
    
    # Adım 3: s = y^k (mod p) - paylaşılan gizli
    shared_secret = pow(public_key_y, encryption_random, p)
    
    if verbose:
        print(f"\n[Adım 3] Paylaşılan Gizli Hesaplaması:")
        print(f"  s = y^k mod p")
        print(f"  s = {public_key_y}^{encryption_random} mod {p}")
        print(f"  s = {shared_secret}")
    
    # Adım 4: c₂ = m × s (mod p)
    c2 = (message * shared_secret) % p
    
    if verbose:
        print(f"\n[Adım 4] c₂ = m × s mod p Hesaplaması:")
        print(f"  c₂ = {message} × {shared_secret} mod {p}")
        print(f"  c₂ = {c2}")
    
    ciphertext = (c1, c2)
    
    if verbose:
        print(f"\n" + "="*70)
        print("SONUÇ - ŞİFRELİ METİN")
        print("="*70)
        print(f"Ciphertext: (c₁={c1}, c₂={c2})")
        print("="*70 + "\n")
    
    return ciphertext


# ============================================================================
# BÖLÜM 5: Çözme
# ============================================================================

def decrypt(ciphertext, private_key, p, verbose=True):
    """
    ElGamal Çözme Fonksiyonu
    
    Adımlar:
        1. Şifreli metin (c₁, c₂) alınır
        2. s = c₁^x (mod p) hesaplanır (gönderici tarafından oluşturulan paylaşılan gizli)
        3. m = c₂ × s^(-1) (mod p) hesaplanır
    
    Matematiksel Form:
        Giriş: (c₁, c₂), x
        s = c₁^x mod p = (g^k)^x mod p = g^(kx) mod p
        m = c₂ × s^(-1) mod p
        
    Açıklama:
        - c₂ = m × y^k = m × (g^x)^k = m × g^(kx)
        - c₁^x = (g^k)^x = g^(kx)
        - Dolayısıyla: m = c₂ / c₁^x (mod p)
    
    Parametreler:
        ciphertext: (c₁, c₂) tuple
        private_key: x (gizli anahtar)
        p: Asal modulus
        verbose: Ayrıntılı çıktı yazdırılsın mı?
        
    Dönüş:
        plaintext: Orijinal mesaj (m)
    """
    c1, c2 = ciphertext
    x = private_key
    
    if verbose:
        print("\n" + "="*70)
        print("ELGAMAL ÇÖZME")
        print("="*70)
        print(f"\nGiriş (Şifreli Metin): (c₁={c1}, c₂={c2})")
        print(f"Gizli Anahtar: x = {x}")
        print(f"Modulus: p = {p}")
    
    # Adım 1: s = c₁^x (mod p)
    shared_secret = pow(c1, x, p)
    
    if verbose:
        print(f"\n[Adım 1] Paylaşılan Gizli Hesaplaması:")
        print(f"  s = c₁^x mod p")
        print(f"  s = {c1}^{x} mod {p}")
        print(f"  s = {shared_secret}")
    
    # Adım 2: Modüler ters hesapla: s^(-1) (mod p)
    s_inverse = mod_inverse(shared_secret, p)
    
    if verbose:
        print(f"\n[Adım 2] Modüler Ters Hesaplaması:")
        print(f"  s^(-1) mod p")
        print(f"  s^(-1) = {s_inverse}")
        print(f"  Doğrulama: {shared_secret} × {s_inverse} ≡ {(shared_secret * s_inverse) % p} (mod {p}) ✓")
    
    # Adım 3: m = c₂ × s^(-1) (mod p)
    plaintext = (c2 * s_inverse) % p
    
    if verbose:
        print(f"\n[Adım 3] Mesaj Çözme:")
        print(f"  m = c₂ × s^(-1) mod p")
        print(f"  m = {c2} × {s_inverse} mod {p}")
        print(f"  m = {plaintext}")
        
        print(f"\n" + "="*70)
        print("SONUÇ - ÇÖZÜLMÜŞ MESAJ")
        print("="*70)
        print(f"Plaintext: m = {plaintext}")
        print("="*70 + "\n")
    
    return plaintext


# ============================================================================
# BÖLÜM 6: Örnek Çalışma
# ============================================================================

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("# ELGAMAL KRİPTO SİSTEMİ - ÖRNEK UYGULAMA")
    print("#"*70)
    
    # Sistem kurulumu
    p = 467        # Asal sayı
    g = 2          # Generator
    p, g = setup_system(p, g, verbose=True)
    
    # Anahtar üretimi
    public_key, private_key = generate_keys(p, g, verbose=True)
    
    # Test mesajları
    test_messages = [42, 100, 123, 456]
    
    print("\n" + "="*70)
    print("ŞİFRELEME VE ÇÖZME TESTLERI")
    print("="*70)
    
    for idx, original_message in enumerate(test_messages, 1):
        print(f"\n{'─'*70}")
        print(f"TEST {idx}")
        print(f"{'─'*70}")
        
        # Şifrele
        ciphertext = encrypt(original_message, public_key, verbose=False)
        print(f"Orijinal Mesaj: {original_message}")
        print(f"Şifreli Metin:  (c₁={ciphertext[0]}, c₂={ciphertext[1]})")
        
        # Çöz
        decrypted_message = decrypt(ciphertext, private_key, p, verbose=False)
        print(f"Çözülen Mesaj:  {decrypted_message}")
        
        # Doğrulama
        is_correct = original_message == decrypted_message
        status = "✓ BAŞARILI" if is_correct else "✗ BAŞARISIZ"
        print(f"Durum:          {status}")
    
    print("\n" + "="*70)
    print("TÜM TESTLER TAMAMLANDI")
    print("="*70 + "\n")
    
    # Aynı mesajın iki kez şifrelenmesinin farklı çıktı verdiğini göster
    print("\n" + "="*70)
    print("SÖZSELLİK (SEMANTIK GÜVENLİK) GÖSTERIMI")
    print("="*70)
    print("\nAynı mesaj farklı k değerleri nedeniyle farklı şifreli metinler verir:")
    print("(Bu, ElGamal'ın deterministik olmayan olmasıdır)\n")
    
    test_msg = 99
    print(f"Şifrelenecek Mesaj: {test_msg}\n")
    
    for i in range(3):
        ct = encrypt(test_msg, public_key, verbose=False)
        print(f"  Şifreleme {i+1}: (c₁={ct[0]}, c₂={ct[1]})")
    
    print("\n" + "="*70 + "\n")
