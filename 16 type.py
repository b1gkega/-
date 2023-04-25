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

from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 2025: return n
    if n < 2025: return n + f(n+2)


for n in range(2025, 1, -1):
    f(n)
print(f(2022)-f(2023))