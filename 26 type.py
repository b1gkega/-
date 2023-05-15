a = sorted([int(x) for x in open("26_5228.txt")][1:])[::-1]
b = [a[0]]
for i in range(len(a)):
    if b[-1] - a[i] >= 8:
        b.append(a[i])


print(len(b))