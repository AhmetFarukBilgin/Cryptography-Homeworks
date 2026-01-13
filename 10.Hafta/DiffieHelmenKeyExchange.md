# Diffie–Hellman Key Exchange (DHKE)

## 1. Amaç (Problem Tanımı)

İki taraf (Alice ve Bob):

- Önceden gizli anahtar paylaşmadan
- Dinlenen bir kanal üzerinden
- Aynı gizli anahtarı üretmek istiyor

**Güvenlik varsayımı:** Ayrık Logaritma Problemi (DLP) zordur.

---

## 2. Matematiksel Temel

**Açık parametreler:**

- Büyük asal: $p$
- Generator: $g$ (primitive root mod $p$)

**Gizli değerler:**

- Alice'in sekreti: $a$
- Bob'un sekreti: $b$

---

## 3. Algoritmanın Mantığı (Adım Adım)

### 3.1 Açık Anahtar Üretimi

**Alice:**
$$A = g^a \bmod p$$

**Bob:**
$$B = g^b \bmod p$$

### 3.2 Ortak Anahtar Hesaplaması

$$K = g^{ab} \bmod p$$

**Neden işe yarar?**

$$(B)^a = (A)^b = g^{ab} \bmod p$$

**Dinleyen Eve şunları görür:**

$g, p, A, B$

Ama $a$ veya $b$'yi hesaplayamaz (DLP zor olduğundan).

---

## 4. Diffie–Hellman Pseudo-Code

```
PUBLIC PARAMETERS:
    p ← large prime
    g ← generator (primitive root mod p)

ALICE:
    a ← random private key
    A ← g^a mod p
    send A to Bob

BOB:
    b ← random private key
    B ← g^b mod p
    send B to Alice

ALICE:
    K_A ← B^a mod p

BOB:
    K_B ← A^b mod p

ASSERT:
    K_A == K_B  // shared secret
```

**Not:** Bu anahtar genelde şu amaçlarla kullanılır:

- AES key
- HMAC key

---

## 5. Görsel Anlatım

```
          PUBLIC CHANNEL (EAVESDROPPED)
        ---------------------------------

        g, p are public parameters

Alice                                 Bob
------                                ------
Choose secret a                       Choose secret b
Compute A = g^a mod p                 Compute B = g^b mod p

        A ────────────────────────────>

        <──────────────────────────── B

Compute K = B^a mod p                Compute K = A^b mod p

        Shared Secret: K = g^(ab) mod p
```

**Saldırgan Eve'in görüştükleri:**

- $p, g, A, B$

**Ama yapamadığı:**

- $a$ veya $b$ hesaplayamaz (DLP'nin zorluğu nedeniyle)

---

## 6. Küçük Sayılarla Örnek (Öğretici)

**Parametreler:**

- $p = 23$
- $g = 5$

**Alice:**

- $a = 6$
- $A = 5^6 \bmod 23 = 8$

**Bob:**

- $b = 15$
- $B = 5^{15} \bmod 23 = 19$

**Ortak Anahtar Hesaplaması:**

Alice computes:
$$K = 19^6 \bmod 23 = 2$$

Bob computes:
$$K = 8^{15} \bmod 23 = 2$$

**Sonuç:** Aynı anahtar elde edildi. Dinleyen çıkaramaz.

---

## 7. Kriptanaliz Açısından Değerlendirme

### 7.1 Güçlü Yanlar

- Gizli anahtar paylaşımı yapılmaz
- Perfect Forward Secrecy (ephemeral DH ile)
- Matematiksel temeli sağlam

### 7.2 Zayıf Yanlar (Çok Önemli)

**Kimlik doğrulama yok** →
- Man-in-the-Middle saldırısı mümkün
- Eve kendisini Alice ve Bob olarak taklit edebilir

**Çözümler:**

- Signed DH
- TLS (sertifika ile)
- ECDHE + sertifika

---

## 8. DH vs ECDH (Karşılaştırma)

| Özellik | DH | ECDH |
|---------|----|----|
| Grup | $\mathbb{Z}_p^*$ | Elliptic Curve |
| Anahtar boyutu | Büyük | Küçük |
| DLP zorluğu | Orta | Yüksek |
| Güncel kullanım | Azalıyor | Standart |

---

## 9. Man-in-the-Middle (MITM) Saldırısı

### 9.1 Senaryosu

```
Alice                Eve                 Bob
------               ---                 -----

Generate a           
A = g^a mod p
     │─────────A───────┐
                       │ (Eve intercepts)
                       │ Generate c
                       │ A' = g^c mod p
                       │
                       A'───────────────>
                                        (Bob thinks A' is from Alice)

                       │<──B──────────────
                       │ (Eve intercepts)
                       │ Generate d
                       │ B' = g^d mod p
     <────B'──────────┐
(Alice thinks B' is from Bob)
```

### 9.2 Sonuç

- Alice ve Bob aynı anahtarı bellemez
- Eve her seçim ile iki anahtar üretir
- Trafik Eve tarafından tamamen kontrol edilir

**Koruma yolları:**

- Sertifikat tabanlı kimlik doğrulama
- Önceden paylaşılan anahtar (PSK)
- Digital signature

---

## 10. Pratik Uygulama Noktaları

### 10.1 Parametre Seçimi

- $p$ minimum 2048-bit asal
- $g$ primitive root mod $p$ olmalı
- RFC 7919 standart parametreleri kullanılabilir

### 10.2 Ephemeral DH (DHE)

- Her oturum farklı $a$ ve $b$ seçilir
- Perfect Forward Secrecy sağlanır
- Eski anahtarlar tehlikeye girmez

### 10.3 Modern Alternatif: Elliptic Curve DH (ECDH)

- Daha küçük parametre (256-bit vs 2048-bit)
- Hızlı hesaplama
- Aynı güvenlik seviyesi
- TLS 1.3'ün tercihi

---

## 11. Akademik Sonuç

Diffie–Hellman, kriptografide "gizli anahtar paylaşımı" problemini çözen ilk devrimci yöntemdir.

**Güvenliği:** Ayrık Logaritma Probleminin zorluğuna dayanır.

**Çağdaş Rol:** Modern protokollerin temelini oluşturur:

- TLS / HTTPS
- Signal (encrypted messaging)
- VPN sistemleri
- SSH

**Ama unutulmaması gereken:** Kimlik doğrulama mekanizması gerektiriyor. Saf hâliyle Man-in-the-Middle saldırısına açıktır.