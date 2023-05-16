# a = sorted([int(x) for x in open("26_5228.txt")][1:])[::-1]
# b = [a[0]]
# for i in range(len(a)):
#     if b[-1] - a[i] >= 8:
#         b.append(a[i])
#
#
# print(len(b))





f = open("26_2686.txt")
k = int(f.readline())
spisk = sorted([list(map(int, x.split())) for x in f])
coun = 0
for i in range(k-1):
    if spisk[i][0] == spisk[i+1][0]:
        if spisk[i+1][1] - spisk[i][1] == 1:
            coun += 1
            if coun >= 5:
                print(spisk[i+1])
    else:
        coun = 0
