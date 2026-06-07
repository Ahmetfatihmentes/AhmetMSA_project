import numpy as np

def needleman_wunsch(x, y, match=1, mismatch=-1, gap=-2):
    matrix = np.zeros([len(x)+1, len(y)+1])

    for i in range(1, len(x)+1):
        matrix[i, 0] = matrix[i-1, 0] + gap
    for j in range(1, len(y)+1):
        matrix[0, j] = matrix[0, j-1] + gap

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == "-" or y[j-1] == "-":
                diag = matrix[i-1, j-1] + gap
            elif x[i-1] == y[j-1]:
                diag = matrix[i-1, j-1] + match
            else:
                diag = matrix[i-1, j-1] + mismatch
            up   = matrix[i-1, j] + gap
            left = matrix[i, j-1] + gap
            matrix[i, j] = max(diag, up, left)

    return matrix

def traceback(matrix, x, y, match=1, mismatch=-1, gap=-2):
    i, j = len(x), len(y)
    aligned_x, aligned_y = "", ""

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if x[i-1] == "-" or y[j-1] == "-":
                diag_score = gap
            elif x[i-1] == y[j-1]:
                diag_score = match
            else:
                diag_score = mismatch

            if matrix[i, j] == matrix[i-1, j-1] + diag_score:
                aligned_x = x[i-1] + aligned_x
                aligned_y = y[j-1] + aligned_y
                i -= 1; j -= 1
            elif matrix[i, j] == matrix[i-1, j] + gap:
                aligned_x = x[i-1] + aligned_x
                aligned_y = "-" + aligned_y
                i -= 1
            else:
                aligned_x = "-" + aligned_x
                aligned_y = y[j-1] + aligned_y
                j -= 1
        elif i > 0:
            aligned_x = x[i-1] + aligned_x
            aligned_y = "-" + aligned_y
            i -= 1
        else:
            aligned_x = "-" + aligned_x
            aligned_y = y[j-1] + aligned_y
            j -= 1

    return aligned_x, aligned_y
