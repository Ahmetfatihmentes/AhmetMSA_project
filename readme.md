# ahmetmsa - Dinamik Programlama Tabanlı Çoklu Dizi Hizalama Kütüphanesi

[cite_start]Bu kütüphane, Biyoinformatik dersi final projesi kapsamında, birden fazla biyolojik diziyi (DNA/RNA/Protein) hizalamak amacıyla geliştirilmiştir[cite: 2]. [cite_start]Projede çekirdek hizalama motoru olarak **Dinamik Programlama (Needleman-Wunsch)** algoritması kullanılmış, çoklu hizalama süreci ise **Aşamalı Hizalama (Progressive Alignment)** stratejisiyle yönetilmiştir[cite: 8].

## 🧬 Algoritma Mantığı ve Tasarım Adımları

Kütüphane, karmaşık çok boyutlu matris hesaplamalarından kaçınarak verimli bir Çoklu Dizi Hizalaması (MSA) gerçekleştirmek için şu adımları uygular:

1. **Global İkili Hizalama (Needleman-Wunsch):** Girilen diziler, dinamik programlama matrisi ($len(x)+1 \times len(y)+1$) oluşturularak ikişerli şekilde hizalanır.
2. **Skorlama Parametreleri:** Hizalama esnasında ders senaryosuna uygun olarak şu ceza ve ödül puanları uygulanır:
   - **Match (Eşleşme):** `+1`
   - **Mismatch (Uyuşmazlık):** `-1`
   - **Gap (Boşluk):** `-2`
3. **Aşamalı Birleştirme (Progressive Alignment):** İlk iki dizi dinamik programlama ile hizalanarak temel bir "profil" oluşturulur. Kalan diğer diziler, bu profile sırayla ve geriye doğru iz sürme (traceback) mantığıyla aşama aşama dahil edilerek nihai çoklu hizalama sonucuna ulaşılır.

## 📂 Proje Klasör Yapısı

```text
ahmetMSA_project/
│
├── pyproject.toml         # Kütüphane paketleme ve bağımlılık ayarları
├── main.py                # Test ve çalıştırma scripti
│
└── ahmetmsa/              # Ana kütüphane modülü
    ├── __init__.py        # Dışa aktarım (export) tanımlamaları
    ├── dp_aligner.py      # İkili Dinamik Programlama (NW) ve Traceback kodları
    └── progressive.py     # Aşamalı çoklu hizalama ve MSA skorlama motoru


    🛠️ Kurulum
Kütüphaneyi yerel bilgisayarınızda bir Python paketi olarak kurmak için projenin ana dizininde (ahmetMSA_project/) terminali açıp aşağıdaki komutu çalıştırmanız yeterlidir:

Bash
pip install .
🚀 Kullanım ve Örnek Çıktı
Kütüphaneyi kurduktan sonra main.py dosyasını çalıştırarak veya kendi Python kodunuza dahil ederek kullanabilirsiniz:

Python
from ahmetmsa.progressive import progressive_alignment

# Test dizileri
test_sequences = ["AATCGCC", "AATGC", "ATCGCC", "AATCG"]

# Algoritmayı çalıştırma
msa_result, total_score, _, _ = progressive_alignment(test_sequences)

# Sonuçları yazdırma
print("----- HİZALAMA SONUCU -----")
for idx, aligned_seq in enumerate(msa_result, start=1):
    print(f"Dizi {idx}: {aligned_seq}")
print(f"Toplam Skor: {float(total_score)}")
Örnek Terminal Çıktısı:
Plaintext
----- HİZALAMA SONUCU -----
Dizi 1: AATCGCC
Dizi 2: AATG-C-
Dizi 3: -ATCGCC
Dizi 4: AATCG--
Toplam Skor: 5.0
👨‍💻 Geliştirici
İsim: Ahmet Fatih Menteş

Öğrenci Numarası: 221201007

Ders: Biyoinformatik Final Projesi