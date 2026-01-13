# AES-192 ve AES-256
## Çalışma Prensibi ve Kriptoanaliz Açısından Değerlendirme

## 1. Giriş

AES (Advanced Encryption Standard), Rijndael algoritmasının NIST tarafından standardize edilmiş hâlidir ve modern simetrik kriptografinin temelini oluşturur.

AES'in üç anahtar boyutu vardır:

| Versiyon | Anahtar | Round |
|----------|---------|-------|
| AES-128 | 128 bit | 10 |
| AES-192 | 192 bit | 12 |
| AES-256 | 256 bit | 14 |

Blok boyutu her zaman 128 bittir.

---

## 2. AES'in Yapısal Temeli (SPN)

AES, Substitution–Permutation Network (SPN) yapısını kullanır.

Her round şu adımlardan oluşur:

1. **SubBytes** – Nonlinearity (S-box)
2. **ShiftRows** – Permütasyon
3. **MixColumns** – Lineer difüzyon
4. **AddRoundKey** – Anahtar enjeksiyonu

Son round'da MixColumns yoktur.

---

## 3. AES-192 ve AES-256 Nasıl Çalışır?

### 3.1 Ortak Noktalar

- Aynı round fonksiyonları
- Aynı S-box
- Aynı blok yapısı
- Fark: key schedule ve round sayısı

---

## 4. AES-192

### 4.1 Temel Özellikler

- **Anahtar uzunluğu**: 192 bit
- **Round sayısı**: 12
- **Key schedule**:
  - Daha uzun
  - Daha fazla round key üretimi

### 4.2 Kriptoanaliz Perspektifi

| Saldırı Türü | Durum |
|--------------|-------|
| Brute Force | $2^{192}$ (pratik imkânsız) |
| Lineer & Diferansiyel | 8–9 round'a kadar teorik |
| Pratik saldırı | Yok |
| Related-Key Attacks | Pratik saldırı bilinmiyor |

AES-192, analitik olarak AES-128'den daha güvenlidir, ancak pratikte nadir kullanılır.

---

## 5. AES-256

### 5.1 Temel Özellikler

- **Anahtar uzunluğu**: 256 bit
- **Round sayısı**: 14
- **Key schedule**:
  - Daha karmaşık
  - İki S-box dönüşümü içerir

### 5.2 Kriptoanaliz Açısından İlginç Nokta

AES-256, AES-192'den bazı açılardan daha zor analiz edilir değildir. Bunun nedeni:

- Key schedule lineerlik içerir
- Related-key saldırılara teorik açıklık

### 5.3 Teorik Saldırılar

| Saldırı | Durum |
|--------|-------|
| Related-key | Teorik (full round değil) |
| Biclique | $2^{254.4}$ |
| Diferansiyel | 10–11 round |
| Lineer | Pratik değil |

Bu saldırılar akademiktir, gerçek dünyada uygulanamaz.

---

## 6. AES-192 vs AES-256 (Kriptoanaliz Karşılaştırması)

| Kriter | AES-192 | AES-256 |
|--------|---------|---------|
| Anahtar güvenliği | Çok yüksek | Çok yüksek |
| Round sayısı | 12 | 14 |
| Key schedule | Güçlü | Görece zayıf |
| Related-key | Dayanıklı | Teorik açık |
| Pratik saldırı | Yok | Yok |

---

## 7. Neden AES-256 "Daha Güçlü" Sanılır?

### 7.1 Algısal Yanılgı

Yaygın kanaat: Daha uzun anahtar = daha güvenli

**Gerçek durum:**

- AES-256 brute force'a karşı daha güçlü
- Yapısal analiz açısından AES-192'den daha karmaşık değil

Bu yüzden bazı sistemler AES-192'yi tercih eder (örneğin bazı askeri uygulamalar).

---

## 8. Neden AES-256 Yine de Kullanılıyor?

**Kuantum sonrası güvenlik:**
- Grover algoritması anahtar güvenliğini yarıya indirir
- AES-256 efektif 128 bit seviyesine düşer

**Uzun vadeli veri koruması:**
- 20–30 yıl boyunca koruma gerekli

**Regülasyonlar:**
- "256 bit" psikolojik eşiği

---

## 9. AES Neden Lineer ve Diferansiyel Analize Dayanıklı?

- **S-box**: Yüksek nonlinearity
- **MixColumns**: Hızlı difüzyon
- **Round sayısı**: Güvenlik marjı
- **Yapısal simetri**: Yok

AES, bu saldırılar düşünülerek tasarlanmıştır.

---

## 10. AES Neden Lineer ve Diferansiyel Kriptoanalize Dayanıklıdır?
## Yapısal ve Matematiksel Derin Analiz

### 10.1 Tehdit Modelini Netleştirelim

Lineer ve diferansiyel kriptoanaliz şunu hedefler:

| Saldırı | Aranan şey |
|--------|-----------|
| Diferansiyel | Yüksek olasılıklı fark yolları |
| Lineer | %50'den sapan lineer ilişkiler |

AES'in hedefi: Her round'da bu olasılıkları ve sapmaları üstel olarak bastırmak.

### 10.2 AES S-Box: Savunmanın Kalbi

#### DES'ten Farkı

**DES S-box:**
- Lookup table
- Deneysel olarak optimize

**AES S-box:**
- Algebraic olarak tanımlı
- GF(2⁸) üzerinde: $S(x) = A(x^{-1}) \oplus b$

Bu kritik bir farktır.

#### Diferansiyel Dayanıklılık (DDT)

Bir S-box için önemli metrik:

$$\max_{\Delta x \neq 0} P(\Delta x \to \Delta y)$$

AES S-box:

$$\max = \frac{4}{256} = 2^{-6}$$

Bu ne demek?

- En iyi fark bile çok düşük olasılıklı
- Rastgele fonksiyona çok yakın
- Diferansiyel yollar ilk round'da ölür

#### Lineer Dayanıklılık (LAT)

Lineer bias:

$$\varepsilon = \frac{1}{16}$$

Bu değer:

- Bilinen en düşük bias değerlerinden biridir
- Birden fazla S-box birleşince: $\varepsilon_{\text{total}} \approx \varepsilon^n$

Sonuç: Üstel düşüş

### 10.3 ShiftRows + MixColumns: Difüzyon Silahı

#### Avalanche Etkisi

AES'te:

- 1 bit değişiklik
- 2 round sonra: Tüm state etkilenir

DES'te:

- 4–5 round gerekir

#### MixColumns Matematiği

MixColumns:

- MDS matrix kullanır
- Maksimum difüzyon garantisi

Özellik:

- 1 aktif byte → 4 aktif byte

Diferansiyel yollar kontrol edilemez hâle gelir.

### 10.4 Round Bağımsızlığı (Independence)

Lineer ve diferansiyel saldırılar:

- Round'lar arasında bağımlılık ister

AES'te:

- SubBytes → nonlinear
- ShiftRows → konum karıştırma
- MixColumns → lineer ama güçlü

Bu kombinasyon: Her round'u bir öncekinden istatistiksel olarak koparır.

### 10.5 Piling-Up Lemması AES'te Neden Çalışmaz?

Piling-up formülü:

$$\varepsilon_{\text{total}} = \prod \varepsilon_i$$

AES'te:

- Çok fazla aktif S-box
- Her biri küçük bias

Örnek - 10 round AES-128:

- Minimum aktif S-box ≈ 25+
- $(2^{-6})^{25} = 2^{-150}$

Veri gereksinimi astronomik.

### 10.6 Neden "Yüksek Round" Gerekmedi?

AES:

- 10–14 round
- Ama her round çok güçlü

DES:

- 16 round
- Ama yarım blok nonlinear

Farkı: AES'te "Az ama öldürücü round" felsefesi.

### 10.7 Key Schedule Neden Saldırıya Engel?

Round key'ler:

- Anahtar ile nonlinearly bağlı
- Round key bağımsızlığı yüksek
- Lineer/diferansiyel izler anahtara ulaşamaz

AES-256'da related-key teorisinin ortaya çıkması buradan kaynaklanır, ancak:

- Pratik değildir
- Full-round analizi değildir

### 10.8 Kritik Karşılaştırma (DES vs AES)

| Özellik | DES | AES |
|---------|-----|-----|
| S-box | Küçük, lookup | Algebraic |
| Nonlinearity | Yarım blok | Tüm blok |
| Difüzyon | Yavaş | Hızlı |
| Bias bastırma | Zayıf | Üstel |
| Analiz direnci | Düşük | Yüksek |

### 10.9 Kriptografik Perspektif

AES:

- Lineer ve diferansiyel analizi imkânsız kılmaz
- Ama istatistiksel olarak anlamsız kılar

Bu, modern kriptografinin altın standardıdır.

---

## 11. Akademik Sonuç

AES-192 ve AES-256, kriptoanalitik olarak kırılmamış, yalnızca sınırları test edilmiş algoritmalardır.

- **AES-192** → Yapısal olarak en dengeli seçenek
- **AES-256** → Uzun vadeli ve kuantum dirençli seçenek