# alternate method for O(n) time complexity

def sorted_sqaures(nums):
    left = 0
    right = len(nums) - 1
    output = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            output.append(nums[left] ** 2)
            left += 1
        else:  
            output.append(nums[right] ** 2)
            right -= 1

    output.reverse()
    return output            


print(sorted_sqaures([-7,-3,2,3,11]))