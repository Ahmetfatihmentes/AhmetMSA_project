import numpy as np
from .dp_aligner import needleman_wunsch, traceback

def calculate_msa_total_score(msa_result, match=1, mismatch=-1, gap=-2):
    """Hocanın mantığıyla hizalanmış tüm dizilerin toplam skorunu hesaplar."""
    total_score = 0
    num_seqs = len(msa_result)
    seq_len = len(msa_result[0])
    
    for col in range(seq_len):
        for i in range(num_seqs):
            for j in range(i + 1, num_seqs):
                char1 = msa_result[i][col]
                char2 = msa_result[j][col]
                if char1 == "-" and char2 == "-":
                    continue
                elif char1 == "-" or char2 == "-":
                    total_score += gap
                elif char1 == char2:
                    total_score += match
                else:
                    total_score += mismatch
    return total_score

def progressive_alignment(sequences):
    """Sadece gerekli olan aşamalı hizalamayı yürüten temiz ana fonksiyon."""
    if not sequences:
        return [], 0, None, []
        
    # İlk iki diziyi doğrudan hizalayarak profili başlatıyoruz
    s = needleman_wunsch(sequences[0], sequences[1])
    al1, al2 = traceback(s, sequences[0], sequences[1])
    msa_result = [al1, al2]
    
    # Kalan dizileri mevcut profile sırayla ekliyoruz
    for i in range(2, len(sequences)):
        next_seq = sequences[i]
        s = needleman_wunsch(msa_result[0], next_seq)
        ref_aligned, new_aligned = traceback(s, msa_result[0], next_seq)
        
        for j in range(len(msa_result)):
            updated_seq = ""
            ref_idx = 0
            for char in ref_aligned:
                if char == "-":
                    updated_seq += "-"
                else:
                    updated_seq += msa_result[j][ref_idx]
                    ref_idx += 1
            msa_result[j] = updated_seq
        msa_result.append(new_aligned)
        
    total_score = calculate_msa_total_score(msa_result)
    return msa_result, total_score, None, None