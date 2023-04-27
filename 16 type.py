# def f(n):
#     if n == 1: return 1
#     if n > 1 and n % 2 == 0: return n * n + f(n-1)
#     if n > 1 and n % 2 != 0: return f(n-1) + 2 * f(n-2)
#
#
# print(f(23))


# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n-1) - 2 * g(n-1)
#
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n-1) + 2 * g(n-1)
#
# print(g(21))

# 5537

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n-1)
#
#
# for m in range(2, 10000):
#     f(m)
# print(f(2023)/f(2020))

# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n >= 2025: return n
#     if n < 2025: return n + f(n+2)
#
#
# for n in range(2025, 1, -1):
#     f(n)
# print(f(2022)-f(2023))


# def F(n):
#   if n > 0: return G(n - 1)
#
# def G(n):
#   if n > 1: return F(n - 3)
#
#
# print(F(11))


# def f(n):
#     if n<=3: return n
#     if 3<n<=32: return n//4 + f(n-3)
#     if n > 32: return 2*f(n-5)
#
# print(f(100))

# def f(n):
#     if n > 25: return 2*n*n*n + 1
#     if n<=25: return f(n+2) + 2*f(n+3)
#
#
# coun = 0
# for i in range(1, 1000 + 1):
#     if f(i) % 11 == 0:
#         coun +=1
# print(coun)

# def f(n):
#     if n == 1: return 2
#     if n>1: return f(n-1) + 5 * n**2
#
# print(f(39))


# 3691

# def f(n):
#     if n <= 1:
#         return 1
#     elif n > 1 and n % 2 == 0:
#         return 3 + f(n / 2 - 1)
#     elif n > 1 and n % 2 != 0:
#         return n + f(n + 2)
#
#
# n = 2
# while n < 1000:
#     try:
#         r = f(n)
#         if r == 19:
#             print(n)
#             break
#     except RecursionError:
#         pass
#     n += 1


