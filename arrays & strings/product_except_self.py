def product_except_self(nums):
    l_mult = 1
    r_mult = 1

    n = len(nums)

    l_array = [0] * n
    r_array = [0] * n

    for i in range(n):
        j = -i - 1
        l_array[i] = l_mult
        r_array[j] = r_mult

        l_mult *= nums[i]
        r_mult *= nums[j]


    return [l*r for l, r in zip(l_array, r_array)]    

          

     



print(product_except_self([1, 2, 3, 4]))





'''
    [1,2,3,4]

    123
    023
    013
    012
'''