import numpy as np
from .dp_aligner import needleman_wunsch, traceback

def pairwise_score(seq1, seq2):
    matrix = needleman_wunsch(seq1, seq2)
    return matrix[len(seq1), len(seq2)]

def build_distance_matrix(sequences):
    # Tüm dizi çiftleri arasındaki mesafe matrisini hesapla
    n = len(sequences)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            dist[i][j] = dist[j][i] = -pairwise_score(sequences[i], sequences[j])
    return dist

def build_guide_tree(sequences):
    dist = build_distance_matrix(sequences)
    clusters = [[i] for i in range(len(sequences))]
    merge_order = []

    # En yakın iki kümeyi bul ve birleştir (UPGMA)
    while len(clusters) > 1:
        min_dist, ci, cj = np.inf, -1, -1
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                avg = np.mean([dist[a][b] for a in clusters[i] for b in clusters[j]])
                if avg < min_dist:
                    min_dist, ci, cj = avg, i, j
        merge_order.append((clusters[ci], clusters[cj]))
        merged = clusters[ci] + clusters[cj]
        clusters = [c for k, c in enumerate(clusters) if k not in (ci, cj)] + [merged]

    return merge_order

def get_consensus(msa):
    # Her kolon için en sık görülen karakteri seç
    consensus = ""
    for col in range(len(msa[0])):
        chars = [seq[col] for seq in msa if seq[col] != "-"]
        consensus += max(set(chars), key=chars.count) if chars else "-"
    return consensus

def add_sequence_to_msa(msa, new_seq):
    # Mevcut MSA'nın konsensüsüne yeni diziyi hizala
    consensus = get_consensus(msa)
    matrix = needleman_wunsch(consensus, new_seq)
    ref_aligned, new_aligned = traceback(matrix, consensus, new_seq)

    # Konsensüs hizalamasındaki gap'leri mevcut MSA dizilerine yansıt
    updated_msa = []
    for seq in msa:
        updated_seq = ""
        ref_idx = 0
        for char in ref_aligned:
            if char == "-":
                updated_seq += "-"
            else:
                updated_seq += seq[ref_idx]
                ref_idx += 1
        updated_msa.append(updated_seq)

    updated_msa.append(new_aligned)
    return updated_msa

def sp_score(msa, match=1, mismatch=-1, gap=-2):
    # Sum-of-Pairs: tüm dizi çiftlerinin kolon bazlı skorlarını topla
    total = 0
    for col in range(len(msa[0])):
        for i in range(len(msa)):
            for j in range(i+1, len(msa)):
                a, b = msa[i][col], msa[j][col]
                if a == "-" and b == "-": continue
                elif a == "-" or b == "-": total += gap
                elif a == b:              total += match
                else:                     total += mismatch
    return total

def progressive_alignment(sequences):
    if not sequences:        return [], 0, None, []
    if len(sequences) == 1: return list(sequences), 0, [], []

    merge_order = build_guide_tree(sequences)

    # Guide tree'nin ilk adımındaki iki diziyi ikili hizalamayla başlat
    first_group, second_group = merge_order[0]
    matrix = needleman_wunsch(sequences[first_group[0]], sequences[second_group[0]])
    al1, al2 = traceback(matrix, sequences[first_group[0]], sequences[second_group[0]])
    msa = [al1, al2]
    aligned_indices = set(first_group + second_group)

    # Kalan dizileri guide tree sırasına göre MSA'ya ekle
    for group_a, group_b in merge_order[1:]:
        for idx in group_a + group_b:
            if idx not in aligned_indices:
                msa = add_sequence_to_msa(msa, sequences[idx])
                aligned_indices.add(idx)

    # Tamamen boş kolonları temizle
    keep_cols = [c for c in range(len(msa[0])) if any(seq[c] != "-" for seq in msa)]
    msa = ["".join(seq[c] for c in keep_cols) for seq in msa]

    return msa, sp_score(msa), merge_order, None
