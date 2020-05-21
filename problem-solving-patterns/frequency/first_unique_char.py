# Frequencies in Python are Dictionaries
# example: "1123" would be { '1': 2, '2': 1, '3': 1 }


# Return the index of the first non-repeating char or -1
# there isn't one.

def firstUniqChar(s):

    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

    for index in range(len(s)):
        if frequency[s[index]] == 1:
            return index

    return -1


assert firstUniqChar('a') == 0, 'index 0'
assert firstUniqChar('leetcode') == 0, 'index 0'
assert firstUniqChar('tested') == 2, 'index 2'
