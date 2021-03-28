# Check if a string is a permutation of a palindrome.
# 'aba' is a palindrome and 'baa' is a permutation of a palindrome
# this is a trick question that is really hard because you need to
# know the trick:
# string chars must all be letter characters
# ODD Length string = all char counts must be even except one char count
# EVEN Length string = all char counts must be even
# use frequency pattern = dictionary in python

def ispalindromepermutation(s):
    # remove all non-letter characters
    str = ""
    for char in s:
        if char.isalpha():
            str += char
    # make frequency of character counts
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    # count how many character counts are ODD
    odd_count = 0
    for val in frequency.values():
        if val % 2 != 0:
            odd_count += 1
    # if the str is even we can have NO odd counts
    if len(str) % 2 == 0:
        return odd_count == 0
    # if the str is odd we can have only one odd count
    else:
        return odd_count == 1


assert ispalindromepermutation("tact coa") == True
assert ispalindromepermutation("tactcoapapa") == True
assert ispalindromepermutation("cat") == False
