for a in range(1, 500):
    flag = 0
    for x in range(1, 1000):
        if (((x % 40 == 0) or (x % 64 == 0)) <= (x % a == 0)) == 0:
            flag = 1
    if flag == 0:
        print(a)

