

def find_closest_num(nums):
    closest_num = nums[0]

    for num in nums:
        if abs(num) < abs(closest_num):
            closest_num = num
        elif abs(num) == abs(closest_num):
            if num > closest_num:
              closest_num = num

    return closest_num            
                



print(find_closest_num([2,-1,1]))