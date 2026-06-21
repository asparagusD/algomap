def num_jewels_in_stones(jewels, stones):
    jewels_freq = {}

    jewels_list = list(jewels)
    stones_list = list(stones)

    for stone in stones_list:
        if stone in jewels_list:
            if stone not in jewels_freq:
                jewels_freq[stone] = 1
            else:
                jewels_freq[stone] += 1

    if jewels_freq == {}:
        return 0
    else:
        sum = 0
        for freq in jewels_freq.values():
            sum += freq                


    return sum              



print(num_jewels_in_stones("z", "ZZ"))