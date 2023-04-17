# 1 БЛОК : ПЕРЕБОР

# accept = []
# a = [int(x) for x in open("17.txt")]
# for bebra in range(len(a)):
#     if (a[bebra] % 5 == a[bebra] % 3) and (a[bebra] % 31 == 0 or a[bebra] % 47 == 0 or a[bebra] % 53 == 0):
#         accept.append(a[bebra])
# print(len(accept), min(accept))

accept = []
a = [int(x) for x in open("17.txt")]
for bebra in range(len(a)):
    if sum(list(map(int, str(a[bebra])))) % 5 == 0 and a[bebra] % (3**2) != 0:
        accept.append(a[bebra])
print(len(accept), max(accept))