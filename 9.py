with open("9.csv", 'r') as file:
    table = [sorted([int(j) for j in i.split(",")]) for i in file]

def odin(row):
    counts = [row.count(i) for i in row]
    return counts.count(2) == 2 and counts.count(1) == 5

def dva(row):
    nepovtor = sorted([i for i in row if row.count(i) == 1])
    povtor = [i for i in row if row.count(i) != 1][0]
    a = nepovtor[0] * nepovtor[1] * nepovtor[2]
    return a > (povtor ** 2)

k = 0
for row in table:
    if odin(row) and dva(row):
        k += 1

print(k)


