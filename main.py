from ahmetmsa import progressive_alignment

if __name__ == "__main__":
    # Test için örnek diziler
    test_sequences = ["ACGTACGT", "ACGGTTCGT", "CGTCCGT","ATGCGGTA"]

    # Algoritmayı çalıştır
    msa_result, total_score, merge_order, dist_matrix = progressive_alignment(test_sequences)

    # Guide tree birleştirme sırasını göster
    print("----- GUIDE TREE (UPGMA) -----")
    for step, (group_a, group_b) in enumerate(merge_order, start=1):
        seqs_a = [f"Dizi{i+1}({test_sequences[i]})" for i in group_a]
        seqs_b = [f"Dizi{i+1}({test_sequences[i]})" for i in group_b]
        print(f"Adım {step}: {seqs_a} + {seqs_b}")

    # Hizalama sonucu
    print("\n----- HİZALAMA SONUCU -----")
    for idx, aligned_seq in enumerate(msa_result, start=1):
        print(f"Dizi {idx}: {aligned_seq}")

    # Toplam Sum-of-Pairs skoru
    print(f"\nToplam Skor: {float(total_score)}")
