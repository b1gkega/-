# 1 БЛОК : "ПЕРЕБОР"

# accept = []
# a = [int(x) for x in open("17.txt")]
# for bebra in range(len(a)):
#     if (a[bebra] % 5 == a[bebra] % 3) and (a[bebra] % 31 == 0 or a[bebra] % 47 == 0 or a[bebra] % 53 == 0):
#         accept.append(a[bebra])
# print(len(accept), min(accept))

# accept = []
# a = [int(x) for x in open("17.txt")]
# for bebra in range(len(a)):
#     if sum(list(map(int, str(a[bebra])))) % 5 == 0 and a[bebra] % (3**2) != 0:
#         accept.append(a[bebra])
# print(len(accept), max(accept))

# 2 БЛОК : "ПАРЫ"
# accept = []
# a = [int(x) for x in open("17 (3).txt")]
# for i in range(len(a) - 1):
#     for j in range(i+1, len(a)):
#         if (a[i] * a[j]) % 34 != 0:
#             accept.append(a[i]+a[j])
# print(len(accept), max(accept))

# accept = []
# a = [int(x) for x in open("17 (4).txt")]
# for i in range(len(a) - 1):
#     for j in range(i+1, len(a)):
#         if (a[i] - a[j]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0):
#             accept.append(a[i]+a[j])
# print(len(accept), max(accept))

# accept = []
# a = [int(x) for x in open("17 (5).txt")]
# for i in range(len(a) - 1):
#     for j in range(i+1, len(a)):
#         if (a[i] % 160 != a[j] % 160) and (a[i] % 7 == 0 or a[j] % 7 == 0):
#             accept.append(a[i]+a[j])
# print(len(accept), max(accept))

#37357

# accept = []
# a = [int(x) for x in open("17 (6).txt")]
# for i in range(len(a) - 1):
#     for j in range(i+1, len(a)):
#         if (a[i] + a[j]) % 8 == 0:
#             accept.append(a[i]+a[j])
# print(len(accept), max(accept))

#37336

# accept = []
# a = [int(x) for x in open("17 (7).txt")]
# for i in range(len(a) - 1):
#     if a[i+1] % 3 == 0 or a[i] % 3 == 0:
#         accept.append(a[i]+a[i+1])
# print(len(accept), max(accept))

#48465
# accept = []
# a = [int(x) for x in open("17 (8).txt")]
# c_6_na_konce = []
# for bebra in a:
#     if str(bebra)[-1] == "6":
#         c_6_na_konce.append(int(bebra))
# minimalk = min(c_6_na_konce)
# for bebe in range(len(a)-1):
#     if (str(a[bebe])[-1] == "6" and str(a[bebe + 1])[-1] != "6") or (str(a[bebe])[-1] != "6" and str(a[bebe + 1])[-1] == "6"):
#         if (a[bebe]**2 + a[bebe+1]**2) < minimalk**2:
#             accept.append(a[bebe]**2 + a[bebe+1]**2)
#
# print(len(accept), max(accept))

# accept = []
# a = [int(x) for x in open("17 (9).txt")]
# c_3_na_konce = []
# for bebra in a:
#     if str(bebra)[-1] == "3":
#         c_3_na_konce.append(int(bebra))
# minimalk = max(c_3_na_konce)
# for bebe in range(len(a)-1):
#     if (str(a[bebe])[-1] == "3" and str(a[bebe + 1])[-1] != "3") or (str(a[bebe])[-1] != "3" and str(a[bebe + 1])[-1] == "3"):
#         if (a[bebe]**2 + a[bebe+1]**2) >= minimalk**2:
#             accept.append(a[bebe]**2 + a[bebe+1]**2)
#
# print(len(accept), max(accept))

# accept = []
# a = [int(x) for x in open("17-205.txt")]
# for bebra in range(len(a)-1):
#     if (a[bebra] - a[bebra + 1]) % 74 == 0:
#         accept.append(a[bebra]+a[bebra + 1])
# print(len(accept), max(accept))

#5066
# accept = []
# a = [int(x) for x in open("17-288.txt")]
# for bebra in range(len(a)-2):
#     if (abs(a[bebra]) % 7 != abs(a[bebra+1]) % 7 and abs(a[bebra]) % 7 != abs(a[bebra+2]) % 7 and abs(a[bebra + 2]) % 7 != abs(a[bebra+1]) % 7) and ((a[bebra] != abs(a[bebra])) or (a[bebra + 1] != abs(a[bebra + 1])) or (a[bebra + 2] != abs(a[bebra + 2]))):
#         accept.append(max(a[bebra],a[bebra + 1],a[bebra + 2]) - min(a[bebra],a[bebra + 1],a[bebra + 2]))
# print(len(accept),min(accept))


#4693
# accept = []
# a = [int(x) for x in open("17-243.txt")]
# del_na_119 = []
# for chiselko in range(len(a)):
#     if a[chiselko] % 119 == 0:
#         del_na_119.append(a[chiselko])
# maximka = max(del_na_119)
# for bebra in range(len(a)-1):
#     if (a[bebra] % 100 == 21 or a[bebra + 1] % 100 == 21) and (a[bebra]>maximka or a[bebra + 1]> maximka):
#         accept.append(a[bebra] + a[bebra + 1])
# print(len(accept), min(accept))

# 4688
# accept = []
# a = [int(x) for x in open("17-243.txt")]
# del_na_19 = []
# for chiselko in range(len(a)):
#     if a[chiselko] % 19 == 0:
#         del_na_19.append(a[chiselko])
# maximka = max(del_na_19)
# for bebra in range(len(a)-1):
#     if a[bebra]>maximka or a[bebra + 1]> maximka:
#         accept.append(a[bebra] + a[bebra + 1])
# print(len(accept), min(accept))
