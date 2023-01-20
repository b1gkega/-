for a in range(1, 500):
    flag = 0
    for x in range(1, 1000):
        if (((x % 40 == 0) or (x % 64 == 0)) <= (x % a == 0)) == 0:
            flag = 1
    if flag == 0:
        print(a)

# функция делимость
'''def f(x,a):
    return ((x % a != 0) and (x % 21 == 0)) <= (x % 14 == 0)

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''

# функция коньюнкция
'''def f(x,a):
    return ()  #выражение в ()

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)'''

#фунция график
'''def f(x, y, a):
    return

for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x in range(1, 100) for y in range(1, 100)):
        print(a)'''