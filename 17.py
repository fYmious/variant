nums = [int(x) for x in open("17.txt", 'r')]
max21 = max( i for i in nums if str(i).endswith("21") and len(str(abs(i))) == 5 )

def odin(a, b):
    aa = str(a).endswith("21") and len(str(abs(a))) == 5
    bb = str(b).endswith("21") and len(str(abs(b))) == 5
    return aa + bb == 1

def dva(a, b):
    return ((a ** 2) + (b ** 2)) >= (max21 ** 2)

res = []
for i in range(len(nums) - 1):
    if odin(nums[i], nums[i + 1]) and dva(nums[i], nums[i + 1]):
        res.append(nums[i] + nums[i + 1])

print(len(res), max(res))

