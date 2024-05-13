def f(n):
    bn = f"{n:b}"
    if n % 3 == 0: bn = bn + bn[-2:]
    else:
        add = f"{(n % 3) * 3:b}"
        bn = bn + add

    return int(bn, 2)

res = []
for n in range(1, 10_000):
    r = f(n)
    if r >= 195: res.append(r)

print(min(res))
