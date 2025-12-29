def count_pos_neg(nums):
    pcount = ncount = 0

    for n in nums:
        if n >= 0:
            pcount += 1
        else:
            ncount += 1

    return (pcount, ncount)  # Return a tuple


print( count_pos_neg( [10, -1, -5, 20, 0]))

