from itertools import product

k = 0
for x in product([0,1,2,3,4,5,6], repeat=7):
    if x[0] != 0:
        if sum(1 for i in x if i % 2 == 0) == 2:
            k += 1

print(k)

