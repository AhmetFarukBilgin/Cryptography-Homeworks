# DES ve Triple DES (3DES) Anahtar Yapılarının Kriptanalizi

## 1. Giriş

DES (Data Encryption Standard), 1970'lerde geliştirilen 64 bit blok boyutuna ve 56 bit efektif anahtar uzunluğuna sahip simetrik bir blok şifreleme algoritmasıdır. Günümüzde tek başına güvenli kabul edilmemektedir. Bu zayıflığı gidermek amacıyla Triple DES (3DES) geliştirilmiştir.

3DES, DES algoritmasının ardışık olarak birden fazla kez uygulanması prensibine dayanır ve 1-key, 2-key ve 3-key olmak üzere farklı anahtar konfigürasyonları vardır.

## 2. DES (1-Key) – Tek Anahtarlı DES

### 2.1 Yapı

- **Anahtar sayısı**: 1
- **Efektif anahtar uzunluğu**: 56 bit
- **Şifreleme**: $C = DES_K(P)$

### 2.2 Güvenlik Durumu

#### Brute Force Atağı

Anahtar uzayı: $2^{56} \approx 7.2 \times 10^{16}$

Modern donanımlar (ASIC, FPGA, GPU cluster) ile saatler–günler mertebesinde kırılabilir.

EFF tarafından 1998 yılında geliştirilen DES Cracker, 56 saatte DES'i kırabilmiştir.

### 2.3 Kriptanaliz Özeti

| Özellik | Durum |
|---------|-------|
| Brute force | Dayanıksız |
| Diferansiyel kriptanaliz | Teorik olarak mümkün |
| Lineer kriptanaliz | Uygulanabilir |
| Güncel kullanım | Yasak / deprecated |

### 2.4 Sonuç

Tek anahtarlı DES tamamen güvensizdir ve kriptografik olarak kırılmıştır.

---

## 3. 2-Key Triple DES (K₁, K₂)

### 3.1 Yapı (EDE Modu)

En yaygın kullanılan yapı:

$$C = DES_{K_1}(DES_{K_2}^{-1}(DES_{K_1}(P)))$$

- **Anahtar sayısı**: 2
- **Nominal anahtar uzunluğu**: 112 bit

### 3.2 Teorik Güvenlik

Naif beklenti: $2^{112}$

Ancak...

### 3.3 Meet-in-the-Middle (MITM) Atağı

MITM saldırısı, 2-key 3DES'i ciddi şekilde zayıflatır.

#### MITM Mantığı:

1. $DES_{K_1}(P)$ hesaplanır
2. $DES_{K_2}^{-1}(C)$ hesaplanır
3. Ortak ara değer eşleşmesi aranır

#### Karmaşıklık:

- **Zaman**: $O(2^{57})$
- **Bellek**: $O(2^{56})$

Bu, DES'ten yalnızca ~2 kat daha güvenlidir.

### 3.4 Kriptanaliz Özeti

| Özellik | Durum |
|---------|-------|
| Brute force | Teorik |
| MITM | Pratik |
| Efektif güvenlik | ~80 bit |
| Standartlarda durumu | Aşamalı kaldırılıyor |

### 3.5 Sonuç

2-key 3DES, MITM saldırıları nedeniyle modern güvenlik gereksinimlerini karşılamaz.

---

## 4. 3-Key Triple DES (K₁, K₂, K₃)

### 4.1 Yapı

$$C = DES_{K_3}(DES_{K_2}^{-1}(DES_{K_1}(P)))$$

- **Anahtar sayısı**: 3
- **Nominal anahtar uzunluğu**: 168 bit

### 4.2 Güvenlik Analizi

#### MITM'e Karşı

- MITM uygulanabilir ama çok daha maliyetlidir
- **Efektif güvenlik**: $\approx 112$ bit

### 4.3 Asıl Problem: Block Size (64 bit)

3DES'in en büyük sorunu anahtar değil, blok boyutudur.

#### Birthday Attack (Sweet32)

- 64 bit blok → $2^{32}$ blok sonrası çakışma
- Uzun süreli TLS / VPN oturumlarında plaintext sızıntısı

2016 yılında ortaya konan Sweet32 saldırısı, 3DES'in pratikte zayıf olduğunu göstermiştir.

### 4.4 Kriptanaliz Özeti

| Özellik | Durum |
|---------|-------|
| Brute force | Güvenli |
| MITM | Teorik |
| Birthday attack | Pratik |
| NIST durumu | Deprecated |

---

## 5. Karşılaştırmalı Tablo

| Özellik | DES | 2-Key 3DES | 3-Key 3DES |
|---------|-----|-----------|-----------|
| Anahtar sayısı | 1 | 2 | 3 |
| Efektif güvenlik | 56 bit | ~80 bit | ~112 bit |
| MITM direnci | Zayıf | Zayıf | Orta |
| Block size | 64 bit | 64 bit | 64 bit |
| Güncel kullanım | Hayır | Hayır | Hayır |

---

## 6. Neden Artık Kullanılmıyor?

- 64 bit blok boyutu
- Yavaşlık (DES ×3)
- Güncel saldırılar (Sweet32)
- AES'in varlığı

NIST, 3DES'i kademeli olarak kaldırırken AES'i önermiştir.

---

## 7. DES ve 3DES Üzerine Derinlemesine Kriptanaliz

### 7.1 Meet-in-the-Middle (MITM) Saldırısının Matematiksel Analizi

#### 7.1.1 Temel Fikir

Meet-in-the-Middle saldırısı, ardışık şifrelemelerde anahtar uzayını doğrudan brute force etmek yerine, ara değerler üzerinden arama yapmayı hedefler.

Örnek olarak 2-Key Triple DES (EDE):

$$C = E_{K_1}(D_{K_2}(E_{K_1}(P)))$$

- **Naif brute force**: $2^{112}$
- **MITM ile**:
  - Anahtar uzayı ikiye bölünür
  - Ara değerler üzerinden eşleştirme yapılır

#### 7.1.2 Matematiksel İşleyiş

Tanımlayalım:

$$X = E_{K_1}(P)$$
$$Y = D_{K_2}(C)$$

Doğru anahtarlar için: $X = Y$

**Algoritma**:

1. Tüm $K_1$ için $E_{K_1}(P)$ hesaplanır → tabloya yazılır
2. Tüm $K_2$ için $D_{K_2}(C)$ hesaplanır
3. Ortak ara değer aranır

#### 7.1.3 Karmaşıklık Analizi

| Tür | Karmaşıklık |
|-----|-------------|
| Zaman | $O(2^{57})$ |
| Bellek | $O(2^{56})$ |

112 bit güvenlik beklentisine karşın, MITM saldırısı efektif güvenliği ~80 bite indirmiştir.

#### 7.1.4 Kriptografik Anlamı

- Çoklu şifreleme doğrusal biçimde güvenliği artırmaz
- Ara değerlerin varlığı saldırı yüzeyini genişletir
- Yeni algoritmalarda (AES, ChaCha20) bu tür zincirleme yapıdan kaçınılır

---

### 7.2 DES Round Yapısının Kriptanalizi

#### 7.2.1 Feistel Yapısı

DES, 16 round'luk Feistel ağı kullanır:

$$L_{i+1} = R_i$$
$$R_{i+1} = L_i \oplus F(R_i, K_i)$$

Bu yapı sayesinde:

- Şifreleme ve deşifreleme aynı algoritmayla yapılır
- Ancak bu simetri bazı analizleri kolaylaştırır

#### 7.2.2 S-Box Tasarımı

DES'in güvenliği büyük ölçüde S-box'lara dayanır.

**Güçlü Yanlar:**
- Diferansiyel kriptanalize karşı bilinçli olarak optimize edilmiştir
- NSA katkısı bu noktada kritiktir

**Zayıf Yanlar:**
- S-box'lar gizli tasarlanmıştır
- Modern standartlara göre küçük ve sabittir

#### 7.2.3 Lineer Kriptanaliz

- DES: Lineer yaklaşımlara karşı tam bağışık değildir
- $\approx 2^{43}$ bilinen plaintext ile istatistiksel anahtar çıkarımı mümkündür

#### 7.2.4 Round Sayısı Problemi

- 16 round yetersiz kalmıştır
- Yeni blok şifreler 10–14 round kullanırlar, ancak çok daha güçlü nonlinearity ile

DES'in round yapısı kendi zamanında ilerici olsa da, artık yetersiz kabul edilmektedir.

---

### 7.3 Legacy Sistemlerde DES / 3DES Neden Hâlâ Görülüyor?

#### 7.3.1 Teknik Borç (Technical Debt)

- Bankacılık sistemleri
- Ana bilgisayarlar (mainframe)
- Gömülü sistemler (HSM, POS)

Bu sistemlerde:
- Algoritma değiştirmek çok maliyetli
- Sertifikasyon süreçleri uzun

#### 7.3.2 Geriye Dönük Uyumluluk

- ISO 8583 (kart sistemleri)
- Eski TLS konfigürasyonları
- Smart card altyapıları

Bu, "çalışıyorsa değiştirme" yaklaşımının tipik sonucudur.

#### 7.3.3 Regülasyon ve Sertifikasyon

- Bazı sistemler eski FIPS sertifikalarıyla çalışır
- Yeniden sertifikasyon milyon dolarlar gerektirebilir

#### 7.3.4 Pratik Tehdit Modeli Yanılgısı

Bazı kurumlar:
- "Biz hedef değiliz"
- "Kısa mesajlaşma yapıyoruz"

yanılgısıyla zayıf kriptoyu kullanmaya devam eder.

---

### 7.4 AES ile Yapısal Karşılaştırma

#### 7.4.1 Temel Mimari Fark

| Özellik | DES / 3DES | AES |
|---------|-----------|-----|
| Yapı | Feistel | Substitution-Permutation |
| Block size | 64 bit | 128 bit |
| Anahtar | 56–168 bit | 128–256 bit |
| S-box | Küçük, sabit | Büyük, algebraic |
| Paralellik | Düşük | Yüksek |

#### 7.4.2 Güvenlik Perspektifi

**DES / 3DES**:
- Küçük blok → birthday attack
- MITM saldırıları
- Yavaş

**AES**:
- Bilinen pratik saldırı yok
- Geniş analiz geçmişi
- Donanım hızlandırma (AES-NI)

#### 7.4.3 Kriptanaliz Dayanımı

| Saldırı Türü | DES | AES |
|--------------|-----|-----|
| Brute force | Dayanıksız | Güvenli |
| Lineer | Zayıf | Güvenli |
| Diferansiyel | Zayıf | Güvenli |
| Birthday | Dayanıksız | Güvenli |

---

## 8. Genel Akademik Değerlendirme

DES ve 3DES, kriptografi tarihinde öğretici ve dönüm noktası algoritmalardır; ancak modern tehdit modeli altında kullanılamaz durumdadır.

AES ise:
- Yapısal olarak daha güçlü
- Analitik olarak daha şeffaf
- Donanım/yazılım açısından optimize edilebilir

Bu nedenlerle, günümüzün kriptografik uygulamalarında AES veya daha yeni algoritmalar tercih edilir.
