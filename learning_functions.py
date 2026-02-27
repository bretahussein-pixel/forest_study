def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


seq1 = 'SPAM'
seq2 = 'SCAM'
print(intersect(seq1, seq2))
