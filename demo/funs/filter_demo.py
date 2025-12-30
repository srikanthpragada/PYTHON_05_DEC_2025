def ispositive(num):
    return num > 0


nums = [-10, 5, 0, 9, -4]

for n in filter(ispositive, nums):
    print(n)
