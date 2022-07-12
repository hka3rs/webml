
def check_anagram(str1, str2):
    dict_str1 = {}
    dict_str2 = {}
    ans = True
    for letter in str1:
        if letter in dict_str1.keys():
            dict_str1[letter] += 1
        else:
            dict_str1[letter] = 1
    
    for letter in str2:
        if letter in dict_str2.keys():
            dict_str2[letter] += 1
        else:
            dict_str2[letter] = 1

    for key in dict_str1.keys():
        if key not in dict_str2.keys():
            ans = False
            return ans
        else:
            if dict_str1[key] != dict_str2[key]:
                ans = False
                return ans

    return ans

str1 = "srinivas"
str2 = "savinirs"

ans = check_anagram(str1, str2)

print(ans)

