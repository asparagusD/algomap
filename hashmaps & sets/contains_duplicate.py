def contains_duplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True



print(contains_duplicate([3, 1]))