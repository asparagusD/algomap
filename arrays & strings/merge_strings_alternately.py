def merge_alternately(word1, word2):
    merged_string_list = []

    word1_list = list(word1)
    word2_list = list(word2)

    while word1_list != [] and word2_list != []:
        merged_string_list.append(word1_list.pop(0))
        merged_string_list.append(word2_list.pop(0))

    if word1_list != []:
        merged_string_list.extend(word1_list)
    elif word2_list != []:
        merged_string_list.extend(word2_list)   

    return "".join(merged_string_list)     



print(merge_alternately("abc", "pqr"))