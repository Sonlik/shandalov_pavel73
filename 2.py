a = [1, 4, 6]
b = [11, 33, 22]
nb, na = zip(*[(b, a) for b, a in sorted(zip(b, a))])
print(na)