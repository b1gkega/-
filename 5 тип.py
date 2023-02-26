'''for i in range(1, 1000):
    a = bin(i)[2:]
    a = a + str(a.count('1') % 2)
    a = a + str(a.count('1') % 2)
    R = int(a, 2)
    if R > 43:
        print(R)'''
spisk = []
for N in range(100, 3000):
    a = bin(N)[3:]
    R = int(a, 2)
    if N-R not in spisk:
        spisk.append(N-R)
print(len(spisk))