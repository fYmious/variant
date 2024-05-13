f = open("26.txt", 'r')
s, n = map(int, f.readline().split())
a = sorted([int(x) for x in f])

i = 1
while sum(a[:i + 1]) <= s: i += 1
print(i)
res = a[:i]
ost = s - sum(res) + res[-1]
for j in range(len(a) - 1, 0, -1):
    if a[j] <= ost:
        print(a[j])
        break
