def majority_element(nums):
    frequency = {}

    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    for num in frequency:
        if frequency[num] > len(nums) // 2:
            return num        


print(majority_element([2,2,1,1,1,2,2]))