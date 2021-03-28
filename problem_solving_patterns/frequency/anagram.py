# Frequency ['a': '1', 'b': '2', ...] holds values as keys and their counts as values
# this is like a Java Map or Python dictionary
# Example of using Frequency Pattern to solve a problem:
# is str1 an anagram of st2
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# using all the original letters exactly once


# check if both strings have the same number of characters
def is_anagram(str1, str2):
    length = len(str1)
    if length <= 0 and length != len(str2):
        return False

    frequency1 = {}
    frequency2 = {}
    # make frequencies
    for i in range(length):
        if str1[i] in frequency1:
            frequency1[str1[i]] = frequency1[str1[i]] + 1
        else:
            frequency1[str1[i]] = 1
        if str2[i] in frequency2:
            frequency2[str2[i]] = frequency2[str2[i]] + 1
        else:
            frequency2[str2[i]] = 1

    # check frequencies
    for char in frequency1:
        if char not in frequency2:
            return False
        elif frequency1[char] != frequency2[char]:
            return False

    return True


assert is_anagram("abc", "cab")
assert is_anagram("abc", "cba")
assert is_anagram("abc", "bca")
assert is_anagram("abc", "caa")

