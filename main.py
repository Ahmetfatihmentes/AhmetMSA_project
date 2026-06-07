from ahmetmsa.progressive import progressive_alignment

if __name__ == "__main__":
    # Test için girilen örnek diziler
    test_sequences = ["AATCGCC", "AATGC", "ATCGCC", "AATCG"]
    
    # Algoritmayı çalıştırıp hizalama sonucunu ve toplam skoru alıyoruz
    msa_result, total_score, _, _ = progressive_alignment(test_sequences)
    
    # Başlık kısmı
    print("----- HİZALAMA SONUCU -----")
    
    # Her dizinin soluna "Dizi 1:", "Dizi 2:" yazarak alt alta listeliyoruz
    for idx, aligned_seq in enumerate(msa_result, start=1):
        print(f"Dizi {idx}: {aligned_seq}")
        
    # En altta toplam skoru ondalıklı (x.x) formatta gösteriyoruz
    print(f"Toplam Skor: {float(total_score)}")