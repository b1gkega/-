# a[::-1] реверс строки
# replace(что, на что)
# ord(символ)
# char(число)


'''a = '8'*68
while "222" in a or "888" in a:
    a.replace("222", "8", 1)
    a.replace('888', '2', 1)
print(a)'''

a = '1' + '8' * 80
while "18" in a or "288" in a or "3888" in a:
    a = a.replace("18", "2", 1)
    a = a.replace('288', '3', 1)
    a = a.replace('3888', "1", 1)
print(a)