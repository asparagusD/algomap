def roman_to_int(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    s_list = list(s[::-1])
    sum = 0
    sum += roman_dict[s_list[0]]

    for i in range(len(s_list)-1):
        if roman_dict[s_list[i]] <= roman_dict[s_list[i+1]]:
            sum += roman_dict[s_list[i+1]]
        elif roman_dict[s_list[i]] > roman_dict[s_list[i+1]]:
            sum -= roman_dict[s_list[i+1]]    


        

    return sum            



print(roman_to_int("MCMXCIV"))