# 4988
# from fnmatch import *
#
# for i in range(0, 10**9, 169):
#     if fnmatch(str(i), "123*567?"):
#         print(i, i//169)

# # МАСКА
# from fnmatch import *
#
# for i in range(0, 10 ** 8, 273):
#     if fnmatch(str(i), "12??36*1"):
#         print(i, i // 273)


# # Делители
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x // i)
#     return sorted(d)
#
#
# for k in range(174457,174505 + 1):
#     cocojumbo = div(k)
#     if len(cocojumbo) == 2:
#         print(cocojumbo, k)


# #2572
#
# def div(x):
#     d = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x // i)
#     return sorted(d)
#
#
# for k in range(190201, 190260 + 1):
#     delilki = []
#     cocojumbo = div(k)
#     for myav in cocojumbo:
#         if myav % 2 == 0:
#             delilki.append(myav)
#     if len(delilki) == 4:
#         print(delilki[-1], delilki[-2])



#2575

# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x // i)
#     return sorted(d)
#
#
# for cocojumbo in range(244143, 1367821 + 1):
#     if cocojumbo**0.25 == int(cocojumbo**0.25):
#         if len(div(cocojumbo**0.25)) == 0:
#             print((cocojumbo**0.25)**2, (cocojumbo**0.25)**3)


