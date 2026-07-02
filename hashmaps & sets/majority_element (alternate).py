# alternate method for space complexity O(1)

def majority_element(nums):
    ans = -1
    count = 0

    for num in nums:
        if count == 0:
            ans = num

        if num == ans:
            count += 1
        else:
            count -= 1

    return ans                


print(majority_element([2,2,1,1,1,2,2]))