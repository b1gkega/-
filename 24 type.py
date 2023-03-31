# # Чтение файла
# with open('24.txt', 'r') as f:
#     # работа с файлом
#
# # Запись в файл
# f = open("24.txt", "w")
# # Работа с файлом
# f.close()

# coun = 1
# maximka = 0
# s = open("zadanie24_1.txt").readline()      # Чтение файла в строку
# for i in range(len(s)):
#     if s[i] == "A" and s[i+1] == "A":
#         coun += 1
#     else:
#         maximka = max(maximka, coun)
#         coun = 1
# print(maximka)

s = open("zadanie24_1.txt").readline()
s = s.replace("B", " ").replace("C", " ")
s = s.split()
# print(s)
# print(max(s))        # Max к списку из строк - аккуратно!
# print(max("AAAAA", "BBB", "C", key=len))         ## вывод по длине