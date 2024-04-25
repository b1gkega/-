f = open("27.txt")
n,v = map(int,f.readline().split())
s = [int(x)//v if int(x)%v == 0 else int(x)//v+1 for x in f.readlines()]
flg = 1
for i in range(n):
    for j1 in range(n):
        if j1 != i and j1+1 != i:
            sumk1 = sumk2 = 0
            j2 = j1+1
            l1 = n-i+j1 if i-j1 >= 0 else j1-i
            l2 = i-j2 if i-j1 >= 0 else n-l1-1
            for perv in range(l1):
                sumk1 += s[j1-perv]*(l1-perv)
            for vtor in range(l2):
                sumk2 += s[(j2+vtor)%n]*(l2-vtor)
            if sumk1 == sumk2:
                print(i)
                break


