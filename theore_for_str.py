# a[::-1] реверс строки
# replace(что, на что)
# ord(символ)
# char(число)


'''a = '8'*68
while "222" in a or "888" in a:
    a = a.replace("222", "8", 1)
    a = a.replace('888', '2', 1)
print(a)'''

a = '>' + '1' * 25 + '2' * 17 + '3' * 10
while ">1" in a or ">2" in a or ">3" in a:
    a = a.replace(">1", "22>3", 1)
    a = a.replace('>2', '2>', 1)
    a = a.replace('>3', "11>2", 1)
print(a.count('2')*2 + a.count('1') + a.count('3')*3)


# a = '2'*247
# while "222" in a or "555" in a:
#     if "222" in a:
#         a = a.replace("222", "5", 1)
#     else:
#         a = a.replace('555', '2', 1)
# print(a)

# a = '8'*70
# while "2222" in a or "8888" in a:
#     if "2222" in a:
#         a = a.replace("2222", "88", 1)
#     else:
#         a = a.replace('8888', '22', 1)
# print(a)

# a = '1'*25 + '2'*25 + '3'*25 + '1'*25 + '2'*25 + '3'*25
# while "12" in a or "32" in a or "31" in a:
#     a = a.replace("12", "21", 1)
#     a = a.replace('32', '23', 1)
#     a = a.replace('31', '13', 1)
# print(a[119])
# print(13*3 + 13*5 + 9)
# for n in range(1000):
#     coun = 0
#     a = '9' + n * "1" + n * "2"
#     while "91" in a or "92" in a:
#         a = a.replace("91", "39", 1)
#         a = a.replace('92', '59', 1)
#     sumka = a.count('5') * 5 + a.count('3') * 3 + 9
#     if len(str(sumka)) == 3:
#         for bebra in range(2, round(sumka**0.5)+1):
#             if sumka % bebra == 0:
#                 coun += 1
#         if coun == 0:
#             print(n)
#             break