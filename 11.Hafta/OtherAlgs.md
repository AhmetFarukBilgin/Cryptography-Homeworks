# Asallık Testi Algoritmaları
## (Miller–Rabin ve Solovay–Strassen Hariç)

## 1. Giriş: Kriptografide Asallık Testinin Rolü

Asallık testleri kritik altyapıyı oluşturur:

- RSA anahtar üretimi
- Diffie–Hellman grup seçimi
- ECC parametreleri
- Hash-to-prime yapıları

**Kriptografide asıl amaç:**

"Yanlışlıkla asal olmayan sayıyı asal sanmamak"

Bu nedenle:

- Deterministik doğruluk
- Yanlış pozitif riskinin kontrolü

hayati önem taşır.

---

## 2. Fermat Asallık Testi

### 2.1 Temel Fikir

Fermat'ın küçük teoremi:

$$a^{n-1} \equiv 1 \pmod{n} \quad \text{(n asal ise)}$$

Ancak bu teoremin tersi her zaman doğru değildir.

**Zayıflık:** Carmichael sayıları

### 2.2 Pseudo-Code

```
FERMAT-TEST(n, k):
    if n <= 1:
        return COMPOSITE

    repeat k times:
        choose random a ∈ [2, n-2]
        if a^(n-1) mod n ≠ 1:
            return COMPOSITE

    return PROBABLY PRIME
```

### 2.3 Kriptografik Analiz

| Özellik | Değerlendirme |
|---------|--------------|
| Hız | Çok hızlı |
| Doğruluk | Zayıf |
| Carmichael sayıları | Başarısız |
| Kripto kullanımı | Uygun değil |

Modern kriptografide tek başına kullanılmaz.

---

## 3. AKS Asallık Testi (Agrawal–Kayal–Saxena)

### 3.1 Temel Fikir

İlk deterministik, polinomsal zamanlı asallık testi.

$$n \text{ asal} \Leftrightarrow (x+a)^n \equiv x^n + a \pmod{(n, x^r - 1)}$$

### 3.2 Pseudo-Code (Özet)

```
AKS-TEST(n):
    if n is a perfect power:
        return COMPOSITE

    find smallest r such that:
        ord_r(n) > (log n)^2

    for a = 2 to min(r, sqrt(phi(r)) * log n):
        if gcd(a, n) > 1:
            return COMPOSITE
        if (x + a)^n ≠ x^n + a mod (x^r - 1, n):
            return COMPOSITE

    return PRIME
```

### 3.3 Kriptografik Analiz

| Özellik | Değerlendirme |
|---------|--------------|
| Deterministik | Evet |
| Teorik önem | Çok yüksek |
| Pratik hız | Çok yavaş |
| Gerçek kullanım | Hayır |

Teori devrimi olsa da pratikte kullanılmaz.

---

## 4. Lucas Asallık Testleri

### 4.1 Temel Fikir

Lucas dizileri kullanılır:

$$U_n(P, Q)$$

Asallık, belirli modüler koşullarla test edilir.

**Önemli:** Miller–Rabin'den bağımsız matematik.

### 4.2 Pseudo-Code (Lucas Test)

```
LUCAS-TEST(n):
    choose parameters P, Q
    compute Lucas sequence U_(n+1)

    if U_(n+1) mod n == 0:
        return PROBABLY PRIME
    else:
        return COMPOSITE
```

### 4.3 Kriptografik Analiz

| Özellik | Değerlendirme |
|---------|--------------|
| Deterministik varyant | Var |
| Yanlış pozitif | Çok düşük |
| Tek başına kullanım | Nadir |
| Kombine test | Yaygın |

---

## 5. Baillie–PSW Asallık Testi

### 5.1 Temel Fikir

Hibrit test:

1. Bir adet base-2 test
2. Bir adet güçlü Lucas testi

**Önemli:** Bilinen hiç yanlış pozitif yoktur.

### 5.2 Pseudo-Code

```
BAILLIE-PSW(n):
    if n is even:
        return COMPOSITE

    if base-2 strong test fails:
        return COMPOSITE

    if strong Lucas test fails:
        return COMPOSITE

    return PROBABLY PRIME
```

### 5.3 Kriptografik Analiz

| Özellik | Değerlendirme |
|---------|--------------|
| Yanlış pozitif | Bilinmiyor (0 gözlemlendi) |
| Hız | Çok iyi |
| Deterministik | Hayır |
| Pratik kullanım | Çok yaygın |

Python ve OpenSSL iç yapılarında kullanılır.

---

## 6. Elliptic Curve Primality Proving (ECPP)

### 6.1 Temel Fikir

Eliptik eğriler kullanılır ve asallık için sertifika üretir.

**Önemli:** Sonuç kanıtlanabilir.

### 6.2 Pseudo-Code (Yüksek Seviye)

```
ECPP(n):
    choose elliptic curve E over Z/nZ
    compute #E(n)
    factor large prime q | #E(n)

    if q > (sqrt(n)+1)^2:
        recursively prove q is prime
        return PRIME with certificate
    else:
        retry with new curve
```

### 6.3 Kriptografik Analiz

| Özellik | Değerlendirme |
|---------|--------------|
| Deterministik kanıt | Evet |
| Hız | Orta |
| Sertifika | Evet |
| Büyük asal üretimi | Evet |

Yüksek güvenlikli anahtar üretimi için idealdir.

---

## 7. Karşılaştırmalı Özet Tablosu

| Algoritma | Deterministik | Hız | Kriptoda Kullanım |
|-----------|--------------|-----|------------------|
| Fermat | Hayır | Çok hızlı | Hayır |
| AKS | Evet | Çok yavaş | Hayır |
| Lucas | Kısmi | Orta | Kısmi |
| Baillie–PSW | Hayır | Çok iyi | Evet |
| ECPP | Evet | Orta | Evet |

---

## 8. Kriptografik Sonuçlar

Kriptografide "asal" demek, matematikte asal demekten daha zordur.

**Kritik gerçekler:**

- Yanlış pozitif = anahtar çöküşü
- Teorik doğruluk ≠ pratik güvenlik
- Hibrit testler fiili standarttır

**Modern yaklaşım:**

1. Hızlı probabilistik filtre
2. Ardından deterministik doğrulama

---

## 9. Pratik Tercihler Tablosu

### 9.1 Hız Kritik (Oturum Anahtarı)

- Baillie–PSW tercih edilir
- Yeterli güvenlik sağlanır

### 9.2 Güvenlik Kritik (RSA Anahtarı)

- ECPP veya Baillie–PSW + ek test
- Sertifika taşıma imkanı

### 9.3 Teori Çalışması

- AKS algoritması
- Lucas testleri

---

## 10. Akademik Kapanış

Asallık testleri kriptografinin sessiz kahramanlarıdır.

- **AKS** → Teori devrimi
- **Fermat** → Tarihsel fikir
- **Baillie–PSW** → Pratik kral
- **ECPP** → Yüksek güvenliğin zirvesi

Her test, farklı güvenlik-hız dengesi sunar. Kriptografik sistem tasarımında doğru test seçimi, anahtar üretiminin güvenliğini doğrudan etkiler.

---

## 11. Ek Kaynaklar

### 11.1 Deterministik Asallık Kanıtı

ECPP ile kanıtlanmış asallık, en güvenli yöntemdir. Proth sayıları ve Cunningham zincir gibi özel yapılar için özel algoritmalar vardır.

### 11.2 Endüstri Standartları

- OpenSSL: Baillie–PSW + ek test
- GMP (GNU Multiple Precision): ECPP seçeneği
- Python: Baillie–PSW tabanlı
