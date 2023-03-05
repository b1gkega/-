def f(x, a1, a2):
    return ((70<=x<=140) == (90<=x<=110)) <= (not (a1<=x<=a2))

m = 0
for a1 in range(1, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(1, 600)):
             m = max(a2-a1, m)

print(m/10)