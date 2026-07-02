def two_sum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]
        else:
            num_to_index[num] = i


print(two_sum([2,7,11,15], 9))