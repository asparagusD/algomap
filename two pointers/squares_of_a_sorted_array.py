def sorted_sqaures(nums):
    output = []
    for num in nums:
        output.append(num*num)

    return sorted(output)    


print(sorted_sqaures([-4,-1,0,3,10]))