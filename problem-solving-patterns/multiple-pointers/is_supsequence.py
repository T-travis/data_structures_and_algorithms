# Multiple Pointers - isSubsequence
# Write a function called isSubsequence which takes in two strings and
# checks whether the characters in the first string form a subsequence of
# the characters in the second string.  A subsequence is a sequence that
# can be derived from another sequence by deleting some elements without
# changing the order of the remaining elements

# Time Complexity O(n)
# Space Complexity O(1)


def is_subsequence(str1, str2):
    str1_len, str2_len = len(str1), len(str2)
    if str1_len <= str2_len:
        str1_index, str2_index = 0, 0
        while str1_index < str1_len and str2_index < str2_len:
            if str1[str1_index] == str2[str2_index]:
                str1_index += 1
            str2_index += 1
        if str1_index == str1_len:
            return True
    return False


assert is_subsequence("hello", "hello world")
assert is_subsequence("sing", "sting")
assert is_subsequence("abc", "abracba")
assert is_subsequence("abc", "acb") is False
