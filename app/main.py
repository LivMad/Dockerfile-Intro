import math


def fatorial(n: int) -> int:
    j = 1
    for i in range(n):
        j = j * (i + 1)
    return j


def bhaskara(a: float, b: float, c: float) -> float:
    if b**2 >= 4 * a * c:
        delta = b**2 - 4 * a * c
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        if delta == 0:
            print("Há somente uma raíz:")
            return x1
        else:
            return x1, x2
    else:
        print("Eita, número complexo à vista!")


def serie_taylor(x: float, N: int, e: float):
    sen = 0
    for i in range(N):
        sen_pre = sen
        sen = sen + ((-1) ** i) * (x ** (2 * i + 1)) / fatorial(2 * i + 1)
        if abs(sen - sen_pre) < abs(e):
            break
    return sen


print(fatorial(20))
print(bhaskara(1, -5, 6))
print(serie_taylor(0.5, 20, 0.04))
