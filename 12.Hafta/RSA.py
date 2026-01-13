"""
RSA (Rivest–Shamir–Adleman) Kripto Sistemi - Eğitim Implementasyonu

Bu kod, RSA algoritmasının temel prensiplerini göstermek amacıyla yazılmıştır.
Gerçek kriptografik uygulamalar için production-ready kütüphaneleri (cryptography, PyCryptodome) kullanın.

RSA'nın Temel Prensibi:
- İki büyük asal sayı p ve q seçilir
- n = p * q hesaplanır
- phi(n) = (p-1)(q-1) hesaplanır  
- Açık üs e ve gizli üs d seçilir, öyle ki: e*d ≡ 1 (mod phi(n))
- Şifreleme: c = m^e (mod n)
- Çözme: m = c^d (mod n)
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
    
    Örnek:
        gcd, x, y = extended_gcd(35, 15)
        # gcd = 5, ve 35*x + 15*y = 5 doğrulanır
    """
    if b == 0:
        return a, 1, 0
    
    gcd_value, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_value, x, y


def mod_inverse(e, phi):
    """
    Modüler Çarpma Tersini Hesapla
    
    Amaç: e * x ≡ 1 (mod phi) denklemininde x değerini bulur
    
    Parametreler:
        e: Açık üs (genellikle 65537)
        phi: Euler's totient fonksiyonun değeri: (p-1)(q-1)
        
    Dönüş:
        Modüler ters olan d değeri (gizli üs)
        
    Hata:
        ValueError: Eğer gcd(e, phi) != 1 ise modüler ters yoktur
    """
    gcd_value, x, _ = extended_gcd(e, phi)
    
    if gcd_value != 1:
        raise ValueError(f"Hata: gcd({e}, {phi}) = {gcd_value}. Modüler ters mevcut değil!")
    
    return x % phi


def is_prime(number, trials=10):
    """
    Asal Sayı Testi (Fermat Tabanlı - Eğitim Amaçlı)
    
    Not: Gerçek uygulamalar için Miller–Rabin veya Baillie–PSW testleri kullanılmalı.
    Bu fonksiyon yalnızca eğitim amaçlı basit asal testi sağlar.
    
    Parametreler:
        number: Test edilecek sayı
        trials: Test tekrar sayısı (yüksek = daha güvenilir)
        
    Dönüş:
        True: Muhtemelen asal
        False: Kesinlikle bileşik
    """
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    # Basit bölünebilirlik kontrolü
    for divisor in range(3, min(int(number ** 0.5) + 1, 1000)):
        if number % divisor == 0:
            return False
    
    return True


def generate_prime(min_value=100, max_value=300):
    """
    Belirli aralıkta Rastgele Asal Sayı Üret
    
    Parametreler:
        min_value: Üretilecek asal sayının minimum değeri
        max_value: Üretilecek asal sayının maksimum değeri
        
    Dönüş:
        Asal sayı
    """
    while True:
        candidate = random.randint(min_value, max_value)
        if is_prime(candidate):
            return candidate


# ============================================================================
# BÖLÜM 2: RSA Anahtar Üretimi
# ============================================================================

def generate_rsa_keys(verbose=True):
    """
    RSA Açık ve Gizli Anahtarlarını Üret
    
    Adımlar:
        1. İki farklı asal sayı p ve q seç
        2. n = p * q hesapla
        3. phi(n) = (p-1)(q-1) hesapla
        4. Açık üs e seç (genellikle 65537)
        5. Gizli üs d hesapla: e*d ≡ 1 (mod phi(n))
    
    Parametreler:
        verbose: Ayrıntılı çıktı yazdırılsın mı?
        
    Dönüş:
        (public_key, private_key): Tuple
        public_key = (e, n) - Herkese açık kullanılır
        private_key = (d, n) - Gizli tutulur
    """
    
    if verbose:
        print("\n" + "="*60)
        print("RSA ANAHTAR ÜRETİMİ")
        print("="*60)
    
    # Adım 1: İki farklı asal sayı seç
    p = generate_prime()
    q = generate_prime()
    
    while p == q:
        q = generate_prime()
    
    if verbose:
        print(f"\n[Adım 1] Asal sayılar seçildi:")
        print(f"  p = {p}")
        print(f"  q = {q}")
    
    # Adım 2: n hesapla
    n = p * q
    
    if verbose:
        print(f"\n[Adım 2] n = p × q hesaplandı:")
        print(f"  n = {p} × {q} = {n}")
    
    # Adım 3: phi(n) hesapla
    phi = (p - 1) * (q - 1)
    
    if verbose:
        print(f"\n[Adım 3] φ(n) = (p-1)(q-1) hesaplandı:")
        print(f"  φ(n) = ({p}-1)({q}-1) = {phi}")
    
    # Adım 4: Açık üs e seç
    # Genellikle e = 65537 kullanılır, ama küçük n'ler için uygun olmayabilir
    e = 65537
    
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    
    if verbose:
        print(f"\n[Adım 4] Açık üs e seçildi:")
        print(f"  e = {e}")
        print(f"  gcd(e, φ(n)) = {gcd(e, phi)} ✓ (1 olması gerekiyordu)")
    
    # Adım 5: Gizli üs d hesapla
    d = mod_inverse(e, phi)
    
    if verbose:
        print(f"\n[Adım 5] Gizli üs d hesaplandı:")
        print(f"  d = {d}")
        print(f"  Doğrulama: e × d mod φ(n) = {(e * d) % phi} ✓")
    
    public_key = (e, n)
    private_key = (d, n)
    
    if verbose:
        print(f"\n" + "="*60)
        print("SONUÇ - ANAHTARLAR")
        print("="*60)
        print(f"Açık Anahtar (Public Key):   (e, n) = {public_key}")
        print(f"Gizli Anahtar (Private Key): (d, n) = {private_key}")
        print(f"\nAçık anahtar herkese gösterilebilir.")
        print(f"Gizli anahtar kesinlikle gizli tutulmalıdır!")
        print("="*60 + "\n")
    
    return public_key, private_key


# ============================================================================
# BÖLÜM 3: Şifreleme ve Çözme
# ============================================================================

def encrypt(plaintext_message, public_key):
    """
    RSA Şifreleme Fonksiyonu
    
    Formül: c = m^e (mod n)
    
    Parametreler:
        plaintext_message: Şifrelenecek mesaj (sayı)
        public_key: (e, n) tuple
        
    Dönüş:
        Şifreli metin (ciphertext)
    """
    e, n = public_key
    
    if plaintext_message >= n:
        raise ValueError(f"Mesaj ({plaintext_message}) n'den ({n}) küçük olmalıdır!")
    
    ciphertext = pow(plaintext_message, e, n)
    return ciphertext


def decrypt(ciphertext_message, private_key):
    """
    RSA Çözme Fonksiyonu
    
    Formül: m = c^d (mod n)
    
    Parametreler:
        ciphertext_message: Çözülecek şifreli metin
        private_key: (d, n) tuple
        
    Dönüş:
        Orijinal mesaj (plaintext)
    """
    d, n = private_key
    
    plaintext = pow(ciphertext_message, d, n)
    return plaintext


# ============================================================================
# BÖLÜM 4: Örnek Çalışma
# ============================================================================

if __name__ == "__main__":
    print("\n" + "#"*60)
    print("# RSA KRİPTO SİSTEMİ - ÖRNEK UYGULAMA")
    print("#"*60)
    
    # Anahtar üretimi
    public_key, private_key = generate_rsa_keys(verbose=True)
    
    # Test mesajları
    test_messages = [42, 65, 123]
    
    print("\n" + "="*60)
    print("ŞIFRELEME VE ÇÖZME TESTI")
    print("="*60)
    
    for original_message in test_messages:
        print(f"\n[Test Mesajı] {original_message}")
        
        # Şifrele
        encrypted_message = encrypt(original_message, public_key)
        print(f"  Şifreli metin: {encrypted_message}")
        
        # Çöz
        decrypted_message = decrypt(encrypted_message, private_key)
        print(f"  Çözülen metin: {decrypted_message}")
        
        # Doğrulama
        is_correct = original_message == decrypted_message
        status = "✓ BAŞARILI" if is_correct else "✗ BAŞARISIZ"
        print(f"  Durum: {status}")
    
    print("\n" + "="*60)
    print("PROCESS TAMAMLANDI")
    print("="*60 + "\n")
