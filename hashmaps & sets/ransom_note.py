def can_construct(ransomNote, magazine):
    char_freq_magazine = {}

    for char in magazine:
        if char not in char_freq_magazine:
            char_freq_magazine[char] = 1
        else:
            char_freq_magazine[char] += 1

    for char in ransomNote:
        if char not in char_freq_magazine:
            return False
        elif char_freq_magazine[char] == 1:
            del char_freq_magazine[char]
        else:
            char_freq_magazine[char] -= 1

    return True            
                




print(can_construct("aa", "aab"))