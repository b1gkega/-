a = 5**36 + 5**24 - 25
a5 = ''
while a >0:
    a5 = str(a % 5) + a5
    a = a//5
print(a5, a5.count('4'))