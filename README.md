# Kriptoloji Ödevleri - Kriptografi Algoritmaları ve Analizi

Bu repository, **CENG 4.1 7. Dönem Kriptoloji** dersi kapsamında tamamlanan temel kriptografi algoritmalarını, analitik incelemelerini ve implementasyonlarını içerir.

## 📚 İçerik Özeti

### **Haftalık Konular**

#### **2. Hafta: Temel Matematik**
- **Euclid Alg/** - Öklid Algoritması (EBOB hesaplamı)
- **Extended GCD** - Genişletilmiş Öklid Algoritması

#### **3. Hafta: Moduler Aritmetik**
- **extended_euclid.py** - Extended GCD uygulaması

#### **4. Hafta: Çin Kalan Teoremi**
- **ChineeseRemainder.py** - Çin Kalan Teoremi implementasyonu
- **HizliModulUsAlma.py** - Hızlı Modüler Üs Alma (Binary Exponentiation)

#### **7. Hafta: DES ve 3DES Analizi**
- **3-Des_2key-3key.md** - DES ve Triple DES kriptanalizi
  - MITM saldırıları, block size problemleri, AES ile karşılaştırma

#### **8. Hafta: AES Derinlemesine Analiz**
- **AES192ve256bitteNasılÇalışır.md** - AES-192 ve AES-256 işleyişi
- **AESsonDöngüdeNedenMCyok.md** - Son round'da MixColumns neden yoktur?
- **RastgeleSayıÜreteci.md** - RNG'nin kriptografik önemi

#### **9. Hafta: Ayrık Logaritma Problemi**
- **DiscreteLogoritmaProblemiKriptoAnalizi.md** - DLP algoritmaları ve güvenlik analizi

#### **10. Hafta: Anahtar Değişim ve Analiz**
- **DiffieHelmenKeyExchange.md** - Diffie-Hellman protokolü
- **PollandRho,Pohlig-helmen.md** - DLP çözmek için gelişmiş algoritmalar

#### **11. Hafta: Asallık Testleri**
- **OtherAlgs.md** - Primality Testing Algoritmaları

#### **12. Hafta: Açık Anahtarlı Kriptografi**
- **RSA.py** - RSA şifreleme sistemi (eğitim implementasyonu)
- **El_Gamal.py** - ElGamal şifreleme sistemi

## 🚀 Kullanım

```bash
# RSA Örneği
python 12.Hafta/RSA.py

# ElGamal Örneği
python 12.Hafta/El_Gamal.py

# Öklid Algoritması
cd "2.Hafta/Euclid Alg"
python main.py
```

## 📋 Dosya Yapısı

```
Kriptoloji/
├── 2.Hafta/Euclid Alg/
├── 3.Hafta/extended_euclid.py
├── 4.Hafta/
│   ├── ChineeseRemainder.py
│   └── HizliModulUsAlma.py
├── 7.Hafta/
│   ├── 3-Des_2key-3key.md
│   └── LinearVeDiferansayalKriptoAnalizAtaklar.md
├── 8.Hafta/ (AES analiz dosyaları)
├── 9.Hafta/ (DLP dosyaları)
├── 10.Hafta/ (DH ve Pollard Rho/Pohlig-Hellman)
├── 11.Hafta/ (Asallık testleri)
├── 12.Hafta/ (RSA ve ElGamal)
└── README.md
```

## 📝 Metodoloji Notu

### AI Yardımı ve Pseudo Algoritma Odağı

Bu ödev seti hazırlanırken:

- **AI Kullanımı:** Konsept açıklamaları, markdown formatı önerileri ve kod dokümantasyon şablonları oluşturulmuştur. Fakat tüm matematiksel doğruluk ve kriptanalitik analiz **manuel olarak doğrulanmıştır**.

- **Pseudo Algoritma Odağı:** 
  - Merkezi çalışma alanı **algoritmaların yapısı** ve **neden çalıştığı**'dır
  - Ürün kodu yerine **eğitim odaklı pseudo-kod** tercih edilmiştir
  - Her algoritma için "Bu neden kırılmaz?" sorusuna cevap bulunmaya çalışılmıştır

---

## 🛠️ Future Work - Gelecek Geliştirmeler

### Planlanan İlaveler
- **ECC Implementation** - Elliptic Curve Cryptography uygulaması
- **Lattice-based Cryptography** - Kuantum-dirençli yöntemler (Post-Quantum Crypto)
- **Side-Channel Analysis** - Yan kanal saldırıları (Timing, Power Analysis)
- **Performance Benchmarking** - Algoritmaların hız karşılaştırması
- **Interactive Notebooks** - Adım adım görselleştirme (Jupyter)

### Derinlemesine Analiz Konuları
- Fault Attack uygulamaları (CRT'ye dayalı)
- Meet-in-the-Middle saldırıları
- Modüler aritmetik yapılarının görsel gösterimi
- Kriptanalitik başarısızlık case study'leri

---

## 🎓 Kriptolojiyi Gerçekten Anlamak İçin Çalışma Stratejisi

### 0️⃣ Önce Zihniyet (En Kritik Kısım)

Şunu kabul ederek başla:

- **Kriptoloji ≠ algoritma ezberi**
- **Kriptoloji = neden çalışıyor / nerede kırılır sorularıdır**
- **Modüler aritmetik = araç, amaç değil**

**Hedefin:**
- "Bu algoritma neden güvenli?"
- "Hangi varsayım kırılırsa çöker?"
- "Bu optimizasyon neyi değiştirir?"

### 1️⃣ Modüler Aritmetiği "Hesap" Değil "Yapı" Olarak Öğren

**❌ Yanlış yaklaşım**
- Formülleri ezberleme
- `pow(a, b, n)` çalışıyor → tamam

**✅ Doğru yaklaşım**

Her modüler kavram için şu 3 soruyu sor:
1. Bu hangi kümede çalışıyor? ($\mathbb{Z}_n$, $\mathbb{Z}_n^*$, grup mu?)
2. Neden ters var / yok? (neden `gcd(a, n) = 1` önemli?)
3. Bu yapı kriptoda neden işe yarıyor?

**Kritik mikro-hedefler:**

Aşağıdaki cümleleri açıklayabilir hale gel:
- "Neden RSA'da φ(n) var?"
- "Neden ElGamal'de mesaj direkt şifrelenmez?"
- "Neden modüler üs alma hızlı yapılır?"
- "Neden CRT güvenliği düşürmez ama uygulamada risklidir?"

### 2️⃣ Algoritmaları 3 Katmanlı Öğren

| Seviye | Hedef | Odak |
|--------|-------|------|
| **1 – Mekanik** | Kodu yazabilmek | "Çalışıyor mu?" |
| **2 – Yapısal** | Matematiksel temeli anlamak | Grup yapısı, Determinizm |
| **3 – Kriptanalitik** | Zafiyetleri görmek | Hangi varsayım kırılırsa çöker? |

**⚠️ Gerçek öğrenme Seviye 3'te başlar**

### 3️⃣ Karşılaştırmalı Öğrenme (Çok Etkili)

Hiçbir algoritmayı tek başına çalışma:

| Özellik | RSA | ElGamal | ECDH |
|---------|-----|---------|------|
| **Problem** | Faktörleme | DLP | ECDLP |
| **Deterministik** | Evet | Hayır | Hayır |
| **CRT** | Var | Yok | Yok |
| **Yan Kanal Riski** | Yüksek | Orta | Orta |
| **Kuantum Etkisi** | Shor | Shor | Shor |

### 4️⃣ Kriptanaliz Odaklı Çalış

Algoritmayı değil, **saldırıyı merkeze al**:

1. Algoritma (RSA)
2. Optimizasyon (CRT)
3. Saldırı (Bellcore Fault Attack)
4. Karşı önlem (recompute / verify)

### 5️⃣ Günlük Mini Egzersizler (20–30 dk)

- 🔢 1 küçük modüler örnek elle çöz
- ❓ 1 "neden" sorusu yaz
- 🔐 1 saldırı oku

**Örnek sorular:**
- "Eğer ElGamal'de k tekrar kullanılırsa ne olur?"
- "CRT fault attack'ı nasıl çalışır?"

### 6️⃣ Okuma Stratejisi

**📘 Temel kaynaklar:**
- Katz & Lindell – sadece ilgili bölümler
- Understanding Cryptography (Paar & Pelzl)

**📄 Makale okurken:**
- İspatları geç
- Problem → çözüm → kırılma noktası üçlüsünü ara

### 7️⃣ Kendini Test Etmenin En İyi Yolu

**Bu cümleleri desteksiz açıklayabiliyor musun?**

- "CRT neden hız kazandırır ama fault attack riskini artırır?"
- "Neden AES lineer/diferansiyel analize dayanıklıdır?"
- "Neden rastgele sayı üreteci kriptografinin kalbidir?"

Eğer cevaplar sezgisel geliyorsa → doğru yoldasın.

### 8️⃣ Gerçekçi Yol Haritası

**Önerim:**
- Algoritma sayısını azalt, analiz derinliğini artır
- 2 ay boyunca **RSA**, **Diffie–Hellman**, **AES** çalış ama derinlemesine

---

## 🎯 En Önemli Cümle

> **Kriptolojiyi anlayan insanlar, algoritmayı ezberleyenler değil, algoritmanın neden kırılmadığını ve nasıl kırılabileceğini düşünenlerdir.**

---

**Güncelleme Tarihi:** Ocak 2026  
**Dersin Bölümü:** CENG 4.1 Kriptoloji  
**Dönem:** 7. Dönem (Güz)  
**Notlar:** AI yardımı ve pseudo-algoritma araştırması ile hazırlanmıştır.
