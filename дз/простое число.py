def prost_numb(x):
    kega = True
    for i in range(2, x//2):
        if x % i == 0:
            kega = False
    if kega:
        return "Простое число"
    else:
        return 'НЕ простое число'

x = int(input('Введите число: '))
print(prost_numb(x))