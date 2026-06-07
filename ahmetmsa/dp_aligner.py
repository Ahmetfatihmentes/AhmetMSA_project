import numpy as np

def needleman_wunsch(x, y, match=1, mismatch=-1, gap=-2):
    """
    Match:1, Mismatch:-1, Gap:-2 puanlamasına göre 
    len+1 boyutunda matris doldurur.
    """
    s = np.zeros([len(x) + 1, len(y) + 1])
    
    # İlk satır ve sütunların gap cezası (-2) ile doldurulması
    for i in range(1, len(x) + 1):
        s[i, 0] = s[i - 1, 0] + gap
    for j in range(1, len(y) + 1):
        s[0, j] = s[0, j - 1] + gap

    # Hücrelerin max(a, b, c) ile hesaplanması
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                a = s[i - 1, j - 1] + match
            else:
                a = s[i - 1, j - 1] + mismatch
            
            b = s[i - 1, j] + gap
            c = s[i, j - 1] + gap
            
            s[i, j] = max(a, b, c)
            
    return s

def traceback(s, x, y, match=1, mismatch=-1, gap=-2):
    """
    Matrisin sağ altından başlayarak geriye doğru iz sürer.
    """
    i, j = len(x), len(y)
    se1, se2 = "", ""

    while i > 0 or j > 0:
        if i > 0 and j > 0 and (x[i - 1] == y[j - 1] or s[i, j] == s[i - 1, j - 1] + match or s[i, j] == s[i - 1, j - 1] + mismatch):
            se1 = x[i - 1] + se1
            se2 = y[j - 1] + se2
            i, j = i - 1, j - 1
        elif i > 0 and (j == 0 or s[i, j] == s[i - 1, j] + gap):
            se1 = x[i - 1] + se1
            se2 = "-" + se2
            i = i - 1
        else:
            se1 = "-" + se1
            se2 = y[j - 1] + se2
            j = j - 1
            
    return se1, se2