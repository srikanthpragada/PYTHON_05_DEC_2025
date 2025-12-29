def smallest_factor(num):
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return n

    return num  # return number for prime numbers

print(smallest_factor(45))
print(smallest_factor(29))
