def mediana(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif a <= c <= b or b <= c <= a:
        return c
    else:
        return a

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print(mediana(a, b, c))