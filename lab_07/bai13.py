from collections import Counter

def count_substrings(s):
    return Counter(
        s[i:j]
        for i in range(len(s))
        for j in range(i +1, len(s) + 1)
    )
input_string ="abababab"
result = count_substrings(input_string)
print(result)