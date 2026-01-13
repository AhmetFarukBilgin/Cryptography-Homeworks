# Ayrık Logaritma Problemi İçin İleri Algoritmalar
## Pollard's Rho ve Pohlig–Hellman Algoritmaları

## 1. Giriş

Ayrık Logaritma Problemi (DLP):

$$g^x \equiv h \pmod{p}$$

ifadesinde $x$'in bulunması problemidir ve modern açık anahtarlı kriptografinin (DH, ElGamal, DSA, ECC) temel güvenlik varsayımını oluşturur.

Bu raporda iki önemli algoritma incelenmektedir:

- **Pollard's Rho** – Genel amaçlı, probabilistik
- **Pohlig–Hellman** – Grup yapısına bağlı, deterministik

---

## 2. Pollard's Rho Algoritması

### 2.1 Temel Fikir

Pollard's Rho algoritması:

- Ayrık logaritma için rastgele yürüyüş (random walk) kullanır
- Doğum günü paradoksuna dayanır
- Bellek kullanımı çok düşüktür

**Temel hedef:**

$$g^{a_1} h^{b_1} \equiv g^{a_2} h^{b_2} \pmod{p}$$

Buradan:

$$g^{a_1 - a_2} \equiv h^{b_2 - b_1} \Rightarrow x = \frac{a_1 - a_2}{b_2 - b_1} \pmod{p-1}$$

### 2.2 Matematiksel Yapı

Bir durum fonksiyonu tanımlanır:

$$X_i = g^{a_i} h^{b_i} \bmod p$$

ve deterministik ama rastgele görünümlü bir fonksiyonla güncellenir.

**Çakışma (collision) bulunduğunda:**

- Aynı $X$
- Farklı $(a, b)$

elde edilir ve logaritma çözülür.

### 2.3 Zaman ve Bellek Karmaşıklığı

| Özellik | Değer |
|---------|-------|
| Zaman | $O(\sqrt{p})$ |
| Bellek | $O(1)$ |
| Tür | Probabilistik |
| Grup | Genel |

**Önemli:** ECC'de bilinen en iyi genel saldırıdır.

### 2.4 Pollard's Rho – Pseudo-Code

```
INPUT: g, h, p

Define function f(x, a, b):
    if x ∈ S1:
        x = x * g mod p
        a = (a + 1) mod (p-1)
    elif x ∈ S2:
        x = x * h mod p
        b = (b + 1) mod (p-1)
    else:
        x = x * x mod p
        a = (2a) mod (p-1)
        b = (2b) mod (p-1)
    return (x, a, b)

Initialize:
    x1, a1, b1 ← random
    x2, a2, b2 ← f(x1, a1, b1)

While x1 ≠ x2:
    (x1, a1, b1) ← f(x1, a1, b1)
    (x2, a2, b2) ← f(f(x2, a2, b2))

Solve:
    x = (a1 - a2) * inverse(b2 - b1) mod (p-1)
```

### 2.5 Kriptanalitik Yorum

- ECC güvenliği tamamen Pollard's Rho'ya dayanır
- Paralelleştirilebilir
- Yan kanal saldırıları ile hızlandırılabilir
- Anahtar boyu doğrudan bu algoritmaya göre seçilir

---

## 3. Pohlig–Hellman Algoritması

### 3.1 Temel Fikir

Eğer grup mertebesi:

$$|G| = n = \prod p_i^{e_i}$$

şeklinde küçük asal çarpanlara ayrılabiliyorsa, DLP:

- Küçük alt problemlere bölünür
- Sonuçlar CRT ile birleştirilir

**Kritik nokta:** Bu algoritma DLP'yi değil, grubu kırar.

### 3.2 Matematiksel Mantık

Amaç: $x \bmod p_i^{e_i}$ değerlerini ayrı ayrı bulmak.

Her biri küçük olduğu için:

- Brute force
- BSGS

kullanılabilir.

**Son adım:**

$$x \equiv x_i \pmod{p_i^{e_i}} \Rightarrow x \bmod n \text{ (CRT)}$$

### 3.3 Zaman Karmaşıklığı

| Faktör | Etki |
|--------|------|
| Küçük asal çarpan | Çok hızlı |
| Büyük asal çarpan | Algoritma etkisiz |
| Worst-case | Brute force |

**Güvenlik için:** Grup mertebesi büyük asal olmalı.

### 3.4 Pohlig–Hellman – Pseudo-Code

```
INPUT: g, h, p
n = order of g

Factor n = ∏ p_i^e_i

For each factor p_i^e_i:
    Compute:
        g_i = g^(n / p_i^e_i) mod p
        h_i = h^(n / p_i^e_i) mod p

    Solve:
        g_i^x_i = h_i mod p

    Store:
        x ≡ x_i mod p_i^e_i

Combine all x_i using Chinese Remainder Theorem
Return x
```

### 3.5 Kriptanalitik Yorum

- Zayıf parametre seçimi tam kırılmaya yol açar
- Eski DH sistemleri bu yüzden çökmüştür
- Safe prime kullanımı zorunlu hale gelmiştir

---

## 4. Pollard's Rho vs Pohlig–Hellman

| Özellik | Pollard's Rho | Pohlig–Hellman |
|---------|--------------|----------------|
| Tür | Probabilistik | Deterministik |
| Bellek | Çok düşük | Orta |
| Grup bağımlılığı | Yok | Var |
| ECC'ye etkisi | Kritik | Önemsiz |
| En iyi kullanım | Genel saldırı | Zayıf grup |

---

## 5. Kriptoloji Açısından Sonuç

Ayrık logaritmanın zorluğu, algoritmadan çok grup seçimine bağlıdır.

**ECC sistemi:**
- Pollard's Rho'ya dayanır
- 256-bit yeterli güvenlik sağlar

**DH sistemi:**
- Pohlig–Hellman'a karşı korunmalıdır
- 2048-bit minimum

**Modern sistemler gerektiriyor:**

- Büyük asal mertebe
- Cofactor kontrolü
- Safe prime kullanımı

---

## 6. Akademik Kapanış

**Pollard's Rho:** En iyi genel DLP saldırısıdır. Tüm grup yapılarında çalışır ve ECC güvenliğinin temelini oluşturur.

**Pohlig–Hellman:** Yanlış parametre seçimini affetmez. Grup mertebesinin çarpan yapısı kritiktir.

**Sonuç:** Güvenli kriptografi = matematik + algoritma + uygulama

Her bileşende hata felaket seviyesinde zafiyet yaratır.
