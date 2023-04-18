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