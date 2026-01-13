# Lineer ve Diferansiyel Kriptanaliz
## Modern Blok Şifrelerin Güvenlik Analizi

## 1. Giriş

Modern kriptografinin temel hedefi, şifreli metin ile anahtar arasında istatistiksel olarak anlamlı hiçbir ilişki bırakmamaktır. Ancak birçok blok şifre, özellikle tarihsel olarak geliştirilenler (DES gibi), tam rastgele fonksiyonlardan küçük sapmalar içerir.

Lineer ve diferansiyel kriptanaliz, bu sapmaları kullanarak:

- Anahtar bitleri hakkında olasılıksal bilgi çıkarmayı
- Brute force'tan daha verimli saldırılar üretmeyi amaçlar

Bu iki yöntem:

- Blok şifrelerin tasarımını kökten değiştirmiş
- AES gibi algoritmaların neden bugünkü yapıda tasarlandığını açıklayan temel araçlar olmuştur

---

## 2. Diferansiyel Kriptanaliz

### 2.1 Temel Fikir

Diferansiyel kriptanaliz:

- Girişteki belirli farkların, çıkışta beklenenden daha yüksek olasılıkla belirli farklara dönüşmesini inceler

**Tanım:**

$$\Delta X = X \oplus X'$$
$$\Delta Y = E_K(X) \oplus E_K(X')$$

**Amaç:**

$\Delta X \to \Delta Y$ dönüşümlerinde yüksek olasılıklı yolları bulmak.

### 2.2 S-Box Merkezli Analiz

Diferansiyel kriptanalizin kalbi S-box analizidir.

Bir S-box için:

- Girdi farkı → çıktı farkı
- Differential Distribution Table (DDT) oluşturulur

**Örnek tablo yorumu:**

- Rastgele fonksiyon için her fark eşit olasılıklı
- Gerçek S-box'ta bazı farklar daha sık

DES S-box'ları bu saldırıya karşı bilinçli olarak güçlendirilmiştir.

### 2.3 Çoklu Round Üzerinden Saldırı

Tek round yeterli değildir. Saldırı:

1. Yüksek olasılıklı fark seçilir
2. Round'dan round'a diferansiyel yol izlenir
3. Son round anahtar bitleri tahmin edilir
4. İstatistiksel filtreleme yapılır

### 2.4 Karmaşıklık

| Algoritma | Gerekli Plaintext |
|-----------|------------------|
| DES | $\approx 2^{47}$ |
| AES | Pratik değil |

### 2.5 Kriptografik Önemi

Diferansiyel kriptanaliz, S-box tasarımının kriptografinin kalbi olduğunu kanıtlamıştır.

---

## 3. Lineer Kriptanaliz

### 3.1 Temel Fikir

Lineer kriptanaliz:

- Giriş bitleri, çıkış bitleri ve anahtar bitleri arasında yaklaşık lineer ilişkiler arar

**Form:**

$$P[i_1] \oplus P[i_2] \oplus C[j_1] \oplus K[k_1] = 0$$

Bu eşitlik:

- %50'den sapıyorsa, bilgi sızar

### 3.2 Bias (Sapma) Kavramı

**Tanım:**

$$\varepsilon = P(\text{eşitlik doğru}) - \frac{1}{2}$$

- Rastgele fonksiyon: $\varepsilon = 0$
- Gerçek şifre: $\varepsilon \neq 0$

Ama sapma çok küçüktür, bu nedenle çok veri gerekir.

### 3.3 Piling-Up Lemması

Birden fazla lineer yaklaşım birleştiğinde:

$$\varepsilon_{\text{total}} = 2^{n-1} \prod_{i=1}^{n} \varepsilon_i$$

Bu formül:

- Round sayısı arttıkça neden güvenliğin hızla arttığını açıklar

### 3.4 DES'e Uygulama

DES için:

- $\approx 2^{43}$ bilinen plaintext ile anahtar çıkarımı mümkündür
- Teorik olarak brute force'tan hızlıdır

---

## 4. Neden Modern Şifreler Dayanıklı?

| Özellik | DES | AES |
|---------|-----|-----|
| S-box tasarımı | Küçük, sabit | Algebraic, yüksek nonlinearity |
| Round sayısı | 16 | 10–14 |
| Lineer bias | Var | Yok |
| Diferansiyel yol | Var | Yok |

---

## 5. Lineer vs Diferansiyel Kriptanaliz

| Kriter | Diferansiyel | Lineer |
|--------|-------------|--------|
| İncelenen şey | XOR farkları | Lineer ilişkiler |
| Gerekli veri | Chosen plaintext | Known plaintext |
| Hedef | Round anahtarları | Anahtar bitleri |
| DES üzerindeki etkisi | Yüksek | Yüksek |
| AES üzerindeki etkisi | Yok | Yok |

---

## 6. Ufuk Açıcı Perspektif

### 6.1 Neden Bu Saldırılar Önemli?

Bu saldırılar:

- Şifreyi kırmak için değil
- Şifreyi tasarlamak için geliştirilmiştir

AES:

- Bu saldırılara dayanıklı olacak şekilde tasarlanmıştır

### 6.2 Modern Kriptografide Ders

"Bir şifre kırılabiliyorsa değil, kırılabileceği matematiksel bir yol varsa başarısızdır."

---

## 7. Akademik Sonuç

Lineer ve diferansiyel kriptanaliz:

- Blok şifre tasarımını bilimsel hale getirmiştir
- "Gizli tasarım" dönemini bitirmiştir
- Modern şifrelerin neden karmaşık göründüğünü açıklar
