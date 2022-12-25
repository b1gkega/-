def hex2int(x):
    bukv = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    all_bukv = 'abcdefABCDEF0123456789'
    a = 0
    coun = 0
    for i in x:
        if i in all_bukv:
            if i in bukv:
                i = bukv[i]
            else:
                i = int(i)
            coun += 1
            a = a + i*16**(len(x)-coun)
        else:
            a = 'ОШИБКА, НЕТ ТАКОГО ЧИСЛА'
            break
    return a

def int2hex(y):
    bukvi = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    y = int(y)
    y16 = ''
    while y > 0:
        if y % 16 > 9:
            y16 = bukvi[y % 16] + y16
        else:
            y16 = str(y % 16) + y16
        y = y // 16
    return y16

x = input('Введите число в 16-ой СС:' )
print(hex2int(x))
y = input('Введите число в 10-ой СС:' )
print(int2hex(y))