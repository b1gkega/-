# # Чтение файла
# with open('24.txt', 'r') as f:
#     # работа с файлом
#
# # Запись в файл
# f = open("24.txt", "w")
# # Работа с файлом
# f.close()

# nechet = "13579"
# cocojumbo = []
# bebra = ""
# s = open("24-1.txt").readline()      # Чтение файла в строку
# for i in range(len(s)):
#     if s[i] in nechet:
#         bebra = bebra + s[i]
#     else:
#         cocojumbo.append(bebra)
#         bebra = ""
# print(max(cocojumbo, key=len), cocojumbo)

# s = open("zadanie24_1.txt").readline()
# s = s.replace("B", " ").replace("C", " ")
# s = s.split()
# print(s)
# print(max(s))        # Max к списку из строк - аккуратно!
# print(max("AAAAA", "BBB", "C", key=len))         ## вывод по длине

# coun = 1
# last_coun = 0
# s = open("24_3.txt").readline()
# s = s.replace("C", " ").replace("D", " ")
# s = s.split()
# print(max(s, key=len),len((max(s, key=len))))


# cocojumbo = []
# bebra = ""
# s = open("24-1.txt").readline()
# for i in range(1, len(s)):
#     if ord(s[i-1]) < ord(s[i]) :
#         bebra += s[i-1]
#     else:
#         bebra += s[i-1]
#         if bebra not in cocojumbo:
#             cocojumbo.append(bebra)
#         bebra = ""
# print(max(cocojumbo, key=len))

from itertools import product
coun = 1
maximka = 0
cocojumbo = []

'''cab = product('QRS', repeat=2)
for m in cab:
    k = ''.join(m)
    cocojumbo.append(k)
s = open("24_7600.txt").readline()
for i in range(len(s)-1):
    if (s[i] + s[i+1]) not in cocojumbo:
        coun += 1
    else:
        maximka = max(maximka, coun)
        coun = 1
print(coun)
'''

# s = open("24_7600.txt").readline()
# cab = product('QRS', repeat=2)
# for m in cab:
#     k = ''.join(m)
#     s = s.replace(k, " ")
# s = s.split()
# print(len(max(s, key=len))+2)