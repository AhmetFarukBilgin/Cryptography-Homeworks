# Kriptolojide Rastgele Sayı Üreteçlerinin (RNG) Önemi

## 1. Giriş: Kriptografinin Gizli Kahramanı

Kriptografik sistemler genellikle şu algoritmalar üzerinden anlatılır:

- AES
- RSA
- ECC
- Hash fonksiyonları

Ancak pratikte en çok hata yapılan yer, algoritmalar değil **rastgele sayı üretimidir**.

Temel eşitlik:

$$\text{Güçlü Algoritma} + \text{Zayıf RNG} = \text{Tamamen Kırılabilir Sistem}$$

---

## 2. Kriptolojide "Rastgelelik" Ne Demektir?

Kriptografide rastgelelik şunları gerektirir:

- **Tahmin edilemezlik** (unpredictability)
- Yeniden üretilemezlik
- İstatistiksel düzensizlik
- Gizli durum (internal state) sızıntısına dayanıklılık

**Önemli:** "Uniform dağılım" tek başına yeterli değildir. Saldırganın bir sonraki çıktıyı tahmin edememesi esastır.

---

## 3. RNG Türleri ve Kriptografik Ayrım

### 3.1 Pseudo-Random Number Generator (PRNG)

**Özellikler:**

- Deterministik
- Seed'e bağlı
- Aynı seed → aynı çıktı

**Kriptografik olmayan PRNG örnekleri:**

- rand()
- Linear Congruential Generator

Kripto için kesinlikle yetersizdir.

### 3.2 Cryptographically Secure PRNG (CSPRNG)

Bir RNG'nin kriptografik olması için gereken özellikler:

**Forward security:**
- Bugünkü çıktı bilinirse geçmiş tahmin edilemez

**Backward security:**
- İç durum sızsa bile gelecek korunur

**State compromise resistance**

**Örnekler:**

- /dev/urandom
- Fortuna
- ChaCha20-based DRBG
- NIST SP 800-90 DRBG'ler

### 3.3 True Random Number Generator (TRNG)

Fiziksel süreçlere dayanır:

- Termal gürültü
- Zamanlama jitter'ı
- Kuantum olayları

**Pratik kullanım:**

- Genellikle entropy kaynağı olarak kullanılır
- CSPRNG seed'ini besler

---

## 4. Kriptolojide RNG Nerelerde Kullanılır?

### 4.1 Anahtar Üretimi

AES, RSA, ECC sistemlerinde:

- Zayıf anahtar = brute force değil, tahmin saldırısı

**Gerçek vaka - Debian OpenSSL (2008):**

- Beklenen: $2^{32}$ olası anahtar
- Gerçek: $2^{15}$ olası anahtar
- Sonuç: Tüm SSH ve SSL anahtarları kırıldı

### 4.2 Nonce ve IV Üretimi

Algoritmalarda:

- AES-GCM
- ChaCha20-Poly1305

**Kritik nokta:** Nonce tekrar ederse:

- Anahtar sızıntısı
- Plaintext recovery

Not: Nonce gizli olmasına gerek yok, ama tahmin edilemez olmalı.

### 4.3 Dijital İmzalar (En Kritik Nokta)

ECDSA / DSA sistemleri:

- k rastgele seçilmezse → private key açığa çıkar

**Gerçek vakalar:**

- PlayStation 3 ECDSA hack
- Bitcoin cüzdan hırsızlıkları

Tek bir kötü random sayı ömür boyu anahtar kaybına yol açabilir.

### 4.4 Padding ve Masking

- RSA-OAEP
- Side-channel karşı önlemler

Random padding yoksa:
- Deterministik yapı
- Chosen ciphertext attack

---

## 5. RNG Zayıflıklarının Kriptanalitik Sonuçları

### 5.1 Matematiksel Olarak Güçlü Algoritma Çöker

**AES örneği:**

- Matematiksel olarak sağlam
- Ama: Aynı IV + aynı key → stream cipher davranışı
- Problem AES değil, RNG'dir

### 5.2 RNG = Gizli Anahtarın Kendisi

Birçok protokolde:

$$\text{Güvenlik} \approx \text{entropy(RNG)}$$

Sonuç:

- RNG zayıfsa
- Anahtar uzunluğu anlamsız hale gelir

---

## 6. RNG ve Teorik Güvenlik

### 6.1 Kerckhoffs Prensibi

Klasik ilke: "Sistemin güvenliği anahtarın gizliliğine dayanır."

Ama:

- Anahtar RNG ile üretilir
- RNG kırılırsa: Kerckhoffs çöker

### 6.2 Provable Security ve Random Oracle Model

Kriptografik kanıtlar:

- "Rastgele oracle" varsayar
- Gerçek hayatta: Bu oracle = RNG

Eğer RNG kötü ise: Teorik güvenlik pratikte yok olur.

---

## 7. Legacy Sistemlerde Neden Hâlâ Sorun?

Sorunlu alanlar:

- Embedded cihazlar
- IoT cihazları
- Boot sırasında entropy yetersizliği

**Sonuç:** Aynı seed → aynı anahtar

**Örnek:** Mirai benzeri botnet'ler RNG zayıflığından faydalandı.

---

## 8. AES, DES ve RNG İlişkisi

| Algoritma | RNG'ye Bağımlılık |
|-----------|-------------------|
| DES | Görece düşük |
| AES | Yüksek (nonce/IV) |
| Stream cipher | Kritik |
| ECC | Hayati |

**Sonuç:** Modern kripto RNG'ye daha bağımlıdır.

---

## 9. Teorik vs Pratik Güvenlik

### 9.1 Algoritmaların Gücü

- AES: Matematiksel olarak güvenli
- RSA: Sayı teorisi tarafından korunur
- ECC: Ayrık logaritma problemi tarafından korunur

**Ama:** Bunların hepsi RNG'nin güvenini varsayar.

### 9.2 RNG Başarısızlığının Sessizliği

RNG hataları:

- Sessiz (fark edilmesi zor)
- Felaket seviyesinde (tamamen kırılabilir)
- Geri dönüşsüz (anahtarlar çalınmış olur)

---

## 10. Sonuç: Kriptografinin En Zayıf Halkası

Çarpıcı ama doğru gerçek:

Kriptografi, matematikten çok rastgeleliğe dayanır.

- Algoritmalar genellikle kırılmaz
- RNG hataları: Tamamen sistem çöküşüne neden olur

Bu yüzden:

**RNG, kriptografik sistemin en zayıf halkasıdır.**

---

## 11. En İyi Uygulamalar

Kriptografik RNG seçerken:

- Standart CSPRNG kullanın (örn. NIST SP 800-90)
- Entropy kaynağı yeterli midir kontrol edin
- Seed'in güvenliğini sağlayın
- Periyodik entropy refresh yapın
- Embedded sistem: TRNG + CSPRNG kombinasyonu tercih edin
