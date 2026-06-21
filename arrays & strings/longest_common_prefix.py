def longest_common_prefix(strs):
    common_prefix = ""

    shortest_string_length = float('inf')

    for str in strs:
        if len(str) < shortest_string_length:
            shortest_string_length = len(str)


    i = 0

    while i < shortest_string_length:
        for j in range(1, len(strs)):
            if strs[0][i] != strs[j][i]:
                return common_prefix
        common_prefix += strs[0][i]
        i += 1

    return common_prefix    




print(longest_common_prefix(["dog","racecar","car"]))




'''
    flow
    flower
    flight
'''