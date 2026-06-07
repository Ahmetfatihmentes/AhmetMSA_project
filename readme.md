# AhmetMSA — Çoklu Dizi Hizalama Kütüphanesi

Biyoinformatik dersi final projesi kapsamında geliştirilmiş, **Dinamik Programlama (Needleman-Wunsch)** ve **UPGMA Guide Tree** tabanlı Çoklu Dizi Hizalama (MSA) kütüphanesi.

---

## Kurulum

```bash
pip install ahmetmsa
```

---

## Kullanım

```python
from ahmetmsa.progressive import progressive_alignment

sequences = ["AATCGCC", "AATGC", "ATCGCC", "AATCG"]
msa, score, merge_order, _ = progressive_alignment(sequences)

print("----- GUIDE TREE -----")
for step, (ga, gb) in enumerate(merge_order, 1):
    print(f"Adım {step}: {[sequences[i] for i in ga]} + {[sequences[i] for i in gb]}")

print("\n----- HİZALAMA SONUCU -----")
for i, seq in enumerate(msa, 1):
    print(f"Dizi {i}: {seq}")

print(f"\nToplam Skor: {score}")
```

**Çıktı:**
```
----- GUIDE TREE -----
Adım 1: ['AATCGCC'] + ['ATCGCC']
Adım 2: ['AATGC'] + ['AATCG']
Adım 3: ['AATCGCC', 'ATCGCC'] + ['AATGC', 'AATCG']

----- HİZALAMA SONUCU -----
Dizi 1: AATCGCC
Dizi 2: -ATCGCC
Dizi 3: AAT-G-C
Dizi 4: AATCG--

Toplam Skor: 2
```

---

## Algoritma

### 1. Needleman-Wunsch (Dinamik Programlama)
İki dizi arasında global hizalama yapar. `(len(x)+1) x (len(y)+1)` boyutunda bir matris doldurulur, ardından sağ-alt köşeden başlayarak geriye doğru iz sürülür.

| Durum | Puan |
|-------|------|
| Eşleşme (Match) | +1 |
| Uyuşmazlık (Mismatch) | -1 |
| Boşluk (Gap) | -2 |

### 2. UPGMA Guide Tree
Tüm dizi çiftleri arasındaki NW skoru hesaplanır ve bir mesafe matrisi oluşturulur. UPGMA algoritması bu matrise göre en benzer dizileri önce birleştirecek bir kılavuz ağaç üretir.

### 3. Aşamalı Hizalama (Progressive Alignment)
Guide tree sırasına göre diziler birer birer mevcut profile eklenir. Her adımda profile ait bir consensus dizi üretilir ve yeni dizi buna hizalanır.

### 4. Sum-of-Pairs Skoru
Hizalama kalitesi her sütundaki tüm dizi çiftleri karşılaştırılarak hesaplanır.

---

## Proje Yapısı

```
AhmetMSA_project/
├── ahmetmsa/
│   ├── __init__.py
│   ├── dp_aligner.py      # Needleman-Wunsch ve Traceback
│   └── progressive.py     # Guide Tree, Progressive Alignment, SP Skoru
├── main.py
├── pyproject.toml
└── readme.md
```

---

## Geliştirici

**Ahmet Fatih Menteş** — Biyoinformatik Final Projesi  
Öğrenci No: 221201007
