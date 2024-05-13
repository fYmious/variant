f = open("27A.txt", 'r')
n, k = int(f.readline()), 263
a = [int(x) for x in f]

res = 0
for i in range(n):
    for j in range(i, n):
        p = a[i:j + 1]
        if sum(p) % k == 0:
            res = max(res, len(p))

print(res)
