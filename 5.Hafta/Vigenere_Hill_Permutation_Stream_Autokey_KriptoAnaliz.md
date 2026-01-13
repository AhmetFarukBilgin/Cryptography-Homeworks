# Klasik Şifreleme Algoritmalarının Kriptoanalizi

**(Vigenère – Hill – Permutation – Stream – Autokey)**

---

## 1. Vigenère Şifreleme Algoritması

### 1.1 Çalışma Prensibi

Vigenère şifreleme, **çok alfabeli (polyalphabetic)** bir yerine koyma (substitution) şifreleme yöntemidir. Düz metindeki her harf, anahtar kelimenin ilgili harfiyle birlikte modüler toplama işlemine tabi tutulur.

**Anahtar:**

$$K = k_1, k_2, \ldots, k_m$$

**Düz metin:**

$$P = p_1, p_2, \ldots$$

**Şifreleme işlemi:**

$$C_i = (P_i + K_{i \bmod m}) \bmod 26$$

Anahtar, metin boyunca periyodik olarak tekrar eder.

### 1.2 Kriptoanaliz

Vigenère şifresinin temel zayıflığı **anahtarın tekrar etmesidir**. Bu tekrar, şifreli metinde istatistiksel izler bırakır.

- **Kasiski testi**, tekrarlayan harf dizilerinin mesafelerini inceleyerek anahtar uzunluğunu tahmin eder.
- **Friedman testi (Index of Coincidence)**, metnin doğal dil istatistiklerine yakınlığını ölçerek anahtar uzunluğu hakkında bilgi verir.

Anahtar uzunluğu belirlendikten sonra her alt dizi klasik frekans analizi ile çözülebilir.

### 1.3 Güvensizlik Nedeni

Anahtarın kısa ve periyodik olması, frekans analizinin parçalı olarak uygulanmasına imkân tanır. Bu nedenle Vigenère şifresi modern kriptografi açısından **güvenli değildir**.

---

## 2. Hill Şifreleme Algoritması

### 2.1 Çalışma Prensibi

Hill şifrelemesi **lineer cebir** temellidir. Düz metin, belirli boyutta vektörlere ayrılır ve terslenebilir bir anahtar matrisi ile çarpılır.

$$C = K \cdot P \bmod 26$$

Burada $K$, mod 26 altında terslenebilir bir matristir.

### 2.2 Kriptoanaliz

Hill şifresi tamamen **lineer bir yapıya** sahiptir. Yeterli sayıda bilinen düz metin–şifreli metin çifti elde edildiğinde anahtar matris şu şekilde hesaplanabilir:

$$K = C \cdot P^{-1} \bmod 26$$

Bu durum, **known-plaintext attack** ile sistemin doğrudan kırılabilmesine yol açar.

### 2.3 Güvensizlik Nedeni

Lineerlik, kriptografide ciddi bir zayıflıktır. Hill şifresi **diffusion** sağlar ancak **confusion** içermez. Bu durum, modern blok şifrelerde neden non-lineer bileşenlerin kullanıldığını açıkça göstermektedir.

---

## 3. Permutation (Yer Değiştirme) Şifreleri

### 3.1 Çalışma Prensibi

Permutation şifrelerinde harfler değiştirilmez, yalnızca metin içerisindeki konumları yer değiştirir.

### 3.2 Kriptoanaliz

Bu tür şifrelerde **harf frekansları korunur** ve dilin istatistiksel yapısı büyük ölçüde bozulmaz. Bu nedenle frekans analizi, kelime kalıpları ve dil istatistikleri kullanılarak kolayca çözülebilir.

### 3.3 Güvensizlik Nedeni

Permutation şifreleri yalnızca **diffusion** sağlar, **confusion** sağlamaz. Tek başına kullanıldıklarında güvenli değildirler. Modern şifrelerde yalnızca yardımcı bir bileşen olarak yer alırlar (örneğin AES ShiftRows).

---

## 4. Stream Cipher (Akış Şifreleri)

### 4.1 Çalışma Prensibi

Akış şifrelerinde mesaj bit veya byte seviyesinde, keystream ile XOR işlemine tabi tutulur:

$$C = P \oplus K$$

### 4.2 Kriptoanaliz

En kritik zayıflık **keystream'in tekrar kullanılmasıdır**. Aynı keystream ile şifrelenmiş iki mesaj için:

$$C_1 \oplus C_2 = P_1 \oplus P_2$$

ifadesi elde edilir ve düz metinler arasındaki ilişki açığa çıkar.

### 4.3 Güvensizlik Nedeni

Zayıf rastgele sayı üreteçleri veya anahtar tekrarları sistemin tamamen çökmesine yol açar. **RC4**, bu duruma klasik bir örnektir.

---

## 5. Autokey Cipher

### 5.1 Çalışma Prensibi

Autokey şifrelemede anahtar, düz metnin kendisiyle genişletilir:

$$K = \text{KEY} + \text{PLAINTEXT}$$

Amaç, Vigenère şifresindeki anahtar tekrar problemini azaltmaktır.

### 5.2 Kriptoanaliz

Düz metnin bir kısmı bilindiğinde, anahtarın geri kalanı kolaylıkla elde edilebilir. Bu durum **known-plaintext attack** ile sistemin tamamen kırılmasına neden olur.

### 5.3 Güvensizlik Nedeni

Anahtarın plaintext'e bağımlı olması **zincirleme bir zayıflık** oluşturur. İlk birkaç karakterin açığa çıkması tüm sistemi çökertebilir.

---

## 6. Karşılaştırmalı Özet

| Algoritma     | Temel Zayıflık          | Kırılma Nedeni       |
|---------------|-------------------------|----------------------|
| Vigenère      | Anahtar tekrarı         | İstatistiksel analiz |
| Hill          | Lineer yapı             | Lineer cebir         |
| Permutation   | Frekans korunumu        | Dil analizi          |
| Stream        | Keystream reuse         | XOR ilişkisi         |
| Autokey       | Plaintext bağımlılığı   | Known-plaintext      |

---

## 7. Modern Kriptolojiye Katkıları

Bu algoritmalar günümüzde kullanılmamaktadır; ancak modern kriptografinin temel prensipleri bu sistemlerin zayıflıkları üzerinden şekillenmiştir. **Anahtar tekrarının önlenmesi**, **non-lineer yapıların kullanımı**, **güçlü rastgelelik** ve **confusion–diffusion dengesi** bu kırılmaların doğrudan sonucudur.

---

## Sonuç

Klasik şifreleme algoritmaları, günümüz güvenlik gereksinimlerini karşılamasa da kriptolojinin evriminde kritik bir rol oynamıştır. Bu sistemlerin kriptoanalizi, modern şifreleme algoritmalarının neden belirli tasarım ilkelerine sahip olduğunu anlamak açısından **temel öneme sahiptir**.