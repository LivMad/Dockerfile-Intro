def fatorial(n: int) -> int:
    j = 1
    for i in range(n):
        j = j * (i + 1)
    return j
