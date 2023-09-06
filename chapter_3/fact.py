def fac(n: int):
    if n and n > 0:
        return n * fac(n-1)
    else:
        return 1

print(fac(3))