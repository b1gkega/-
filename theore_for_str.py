# a[::-1] реверс строки
# replace(что, на что)
# ord(символ)
# char(число)


'''a = '8'*68
while "222" in a or "888" in a:
    a.replace("222", "8", 1)
    a.replace('888', '2', 1)
print(a)'''

a = '>' + '1' * 11  + '2' * 12 + '3' * 30
while ">1" in a or ">2" in a or ">3" in a:
    a = a.replace(">1", "22>", 1)
    a = a.replace('>2', '2>', 1)
    a = a.replace('>3', "1>", 1)
print(a.count('2')*2 + a.count('1') + a.count('3'))