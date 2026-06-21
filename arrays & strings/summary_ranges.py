def summary_ranges(nums):
    range_list = []


    i = 0

    while i < len(nums):
        lower = nums[i]

        while i < len(nums) - 1 and nums[i+1] - nums[i] == 1:
            i += 1

        if nums[i] != lower:
            range_list.append(f"{lower}->{nums[i]}")
        else:
            range_list.append(f"{nums[i]}")

        i += 1

    return range_list                

print(summary_ranges([0,2,3,4,6,8,9]
))


'''
    0 -> 2
    4 -> 5
    7


    0    1    2   4   5    7
                      i     j
            
    '''