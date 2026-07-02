def max_number_of_balloons(text):
    target = "balloon"

    target_dict = {
        'b' : 1,
        'a' : 1,
        'l' : 2,
        'o' : 2,
        'n' : 1
    }

    balloon_dict = {}

    for char in target:
        if char not in text:
            return 0
    else:
        for char in text:
            if char in target:
                if char not in balloon_dict:
                    balloon_dict[char] = 1
                else:
                    balloon_dict[char] += 1

        min = float('inf')
        for key in balloon_dict:
            if balloon_dict[key] // target_dict[key] < min:
                min = balloon_dict[key] // target_dict[key]

        return min                    


                     



print(max_number_of_balloons("leetcode"))



'''
    balloons
    
    b -> 1
    a -> 1
    l -> 2
    o -> 2
    n -> 1


'''