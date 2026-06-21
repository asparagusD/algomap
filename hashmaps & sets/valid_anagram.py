def is_anagram(s, t):
    s_list = list(s)
    t_list = list(t)

    anagram_dict_s = {}
    anagram_dict_t = {}

    if len(s) != len(t):
        return False
    else:
        for char in s_list:
            if char not in anagram_dict_s:
                anagram_dict_s[char] = 1
            else:
                anagram_dict_s[char] += 1

        for char in t_list:
            if char not in anagram_dict_t:
                anagram_dict_t[char] = 1
            else:
                anagram_dict_t[char] += 1

        if anagram_dict_s == anagram_dict_t:
            return True
        else:
            return False                        

    



print(is_anagram("rat", "car"))