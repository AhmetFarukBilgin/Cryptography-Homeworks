# Çin Kalanlar Teoremi (Chinese Remainder Theorem)

## 1. Çalışma Mantığı

Çin Kalanlar Teoremi (ÇKT), çok büyük bir modül altında yapılması gereken hesaplamayı, daha küçük ve hesaplanması kolay modüller altında yapılan birden fazla hesaba ayırmayı mümkün kılar.

Bu yaklaşım sayesinde:
- Tek ve uzun sürecek bir büyük modüler işlem yerine,
- Aynı anda yürütülebilen birden fazla küçük modüler işlem gerçekleştirilir,
- Sonuçlar matematiksel olarak **tek ve doğru bir çözüme** birleştirilir.

CRT’nin temel fikri, çözümün **küçük modüler uzaylarda inşa edilip daha büyük modüler uzaya taşınmasıdır**.  
Doğrudan “büyük modülden küçüğe” bir indirgeme yapılmaz; büyük modül çözümü, küçük modül çözümlerinden **yeniden yapılandırılır**.

Böylece, **güvenlikten ödün vermeden** hesaplama süresi ciddi ölçüde azaltılır. Bu özellik, özellikle büyük tamsayı aritmetiğinin yoğun olarak kullanıldığı kriptografik algoritmalarda (örneğin RSA) kritik öneme sahiptir.

---

## 2. Çin Kalanlar Teoremi İçin Gerekli Şartlar

Klasik Çin Kalanlar Teoremi’nin uygulanabilmesi için kullanılan alt modüllerin **çiftler halinde aralarında asal olması** gerekir.

\[
\gcd(m_i, m_j) = 1 \quad (i \neq j)
\]

Bu şart sağlanmazsa:
- Farklı modüler uzaylardan gelen kalıntılar birbiriyle çelişebilir,
- Tekil bir çözüm garanti edilemez,
- Bazı durumlarda sistemin **hiç çözümü olmayabilir**.

> Not: Genelleştirilmiş CRT’de modüllerin aralarında asal olması zorunlu değildir; ancak bu durumda çözümün varlığı ek tutarlılık koşullarına bağlıdır.

---

## 3. Neden Güvenlik Azalmıyor?

Çin Kalanlar Teoremi kullanıldığında teorik anlamda güvenlik azalmaz, çünkü:

- CRT **yeni bir bilgi üretmez**, yalnızca mevcut hesaplamayı yeniden düzenler.
- Büyük modül altında yapılan işlem ile küçük modüller altında yapılan işlemler **matematiksel olarak birebir eşdeğerdir**.
- Anahtar uzayı ve problem zorluğu değişmez.

Başka bir ifadeyle:

> Çin Kalanlar Teoremi kriptografik bir dönüşüm değil, saf bir performans optimizasyonudur.

⚠️ Ancak pratikte önemli bir istisna vardır:  
CRT kullanan sistemler **fault attack (hata enjeksiyonu)** gibi yan kanal saldırılarına karşı korunmazsa ciddi açıklar ortaya çıkabilir. Bu durum teorik güvenliği değil, **uygulama güvenliğini** ilgilendirir.

---

## 4. Günlük Hayat Örneği 1

Bir sınıfta **X** tane öğrenci olsun:

\[
\begin{aligned}
X &\equiv 1 \pmod{3} \\
X &\equiv 3 \pmod{4} \\
X &\equiv 2 \pmod{5}
\end{aligned}
\]

Bu üç bilginin her biri tek başına eksiktir; ancak Çin Kalanlar Teoremi bu bilgilerin **tek bir X değeri** işaret ettiğini garanti eder.

---

## 5. Günlük Hayat Örneği 2 (Kilit Analojisi)

143 basamaklı (temsili olarak) çok karmaşık bir kilit düşünelim.

\[
143 = 11 \times 13
\]

Bu kilit:
- Tek parça hâlinde çözülmeye çalışılırsa çok zor,
- 11 ve 13’e göre iki ayrı küçük kilide bölündüğünde çok daha kolay çözülür.

Çözüm daha sonra CRT ile tekrar tek bir anahtara dönüştürülür.  
Bu işlem **kilidin güvenliğini azaltmaz**, sadece açma süresini kısaltır.

---

## 6. Sayısal Örnek

Hesaplanmak istenen ifade:

\[
7^{103} \bmod 143
\]

\[
143 = 11 \times 13
\]

Önce küçük modüller altında hesaplanır:

\[
\begin{aligned}
7^{103} \bmod 11 \\
7^{103} \bmod 13
\end{aligned}
\]

Elde edilen sonuçlar Çin Kalanlar Teoremi ile birleştirilir ve:

\[
7^{103} \bmod 143 = 123
\]

sonucu elde edilir.

---

## 7. RSA-CRT ve Fault Attack (Bellcore Saldırısı)

RSA implementasyonlarında CRT şu şekilde kullanılır:

\[
\begin{aligned}
m_p &= c^{d_p} \bmod p \\
m_q &= c^{d_q} \bmod q \\
m &= CRT(m_p, m_q)
\end{aligned}
\]

Eğer bu hesaplamalardan **yalnızca biri hatalı** yapılırsa, saldırgan şu değeri hesaplayabilir:

\[
\gcd(m - m', n)
\]

Bu işlem sonucunda:
- \(p\) veya \(q\) doğrudan elde edilir,
- RSA anahtarı tamamen açığa çıkar.

Bu saldırı literatürde **Bellcore Attack** olarak bilinir.

---

## 8. Garner Algoritması ve Klasik CRT Karşılaştırması

| Özellik | Klasik CRT | Garner Algoritması |
|------|-----------|------------------|
| Ara sayı büyüklüğü | Büyük | Kontrollü |
| Overflow riski | Yüksek | Düşük |
| Donanım uyumu | Zayıf | Güçlü |
| Kriptografik kullanım | Orta | Yaygın |

Garner algoritması, CRT’nin özellikle **donanım ve büyük anahtarlar** için optimize edilmiş hâlidir.

---

## 9. Zaman Karmaşıklığı Analizi

RSA için:

- Doğrudan hesaplama:  
  \[
  O(n^3)
  \]

- CRT ile:
  \[
  2 \times O\left(\left(\frac{n}{2}\right)^3\right)
  \]

Bu, pratikte **4–8 kat hızlanma** anlamına gelir.

---

## 10. Lattice-Based Cryptography’de CRT

Post-quantum kriptografide CRT:
- Ring-LWE
- NTRU
- BFV / CKKS

gibi şemalarda **polinom halkalarını küçük bileşenlere ayırmak** için kullanılır.

Amaç:
- Paralel polinom işlemleri
- FFT-benzeri hızlandırmalar
- Bellek ve zaman optimizasyonu

---

## 11. Sonuç

Çin Kalanlar Teoremi, kriptografide yalnızca bir matematiksel araç değil; doğru uygulandığında yüksek performans sağlayan, yanlış uygulandığında ise ciddi güvenlik açıklarına yol açabilen kritik bir yapı taşıdır.

Bu nedenle CRT:
- Matematiksel doğruluk,
- Güvenli implementasyon,
- Fault-resistance

ilkeleri birlikte ele alınarak kullanılmalıdır.
