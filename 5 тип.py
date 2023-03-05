'''for i in range(1, 1000):
    a = bin(i)[2:]
    a = a + str(a.count('1') % 2)
    a = a + str(a.count('1') % 2)
    R = int(a, 2)
    if R > 43:
        print(R)'''
'''spisk = []
for N in range(10000, 100000):
    a = bin(N)[3:]
    R = int(a, 2)
    if N-R not in spisk:
        spisk.append(N-R)
print(len(spisk))'''


for N in range(10000, 100000):
    a = str(N)
    a135 = int(a[0]) + int(a[2]) + int(a[4])
    a24 = int(a[1]) + int(a[3])
    if a135 > a24:
        R = str(a24) + str(a135)
    else:
        R = str(a135) + str(a24)
    if R == '621':
        print(N)
        break