# Write a function can_construct(target, word_bank) that accepts a target
# and an array of strings.  Return a boolean indicating whether or not the 
# target can be constructed by concatenating elements of the word_bank array.
# Elements of word_bank may be reused.


# m = target length, n = word_bank length
# Time Complexity:  O(n^m*m^2)
# Space Complexity: O(m^4)  
def can_construct(target, word_bank):
    
    if target == '':
        return True

    for word in word_bank:
        if word == target[:len(word)]:
            if can_construct(target[len(word):], word_bank):
                return True

    return False


# print(can_construct('abcdef', ['ab', 'abc','cd','def','abcd']))                # True
# print(can_construct('abcdefz', ['ab', 'abc','cd','def','abcd']))               # False
# print(can_construct('skateboard', ['bo', 'rd','ate','t','ska','sk','boar']))   # False
# print(can_construct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))  # True
# print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef', \
#     ['e','ee','eee','eeee','eeeee']))    # False SLOW


# Time Complexity:  O(n * m^2)
# Space Complexity: O(m^4)  
def can_construct_memoization(target, word_bank, mem):

    if target in mem.keys():
        return mem[target]
    
    if target == '':
        return True

    for word in word_bank:
        if word == target[:len(word)]:
            if can_construct_memoization(target[len(word):], word_bank, mem) == True:
                mem[target] = True
                return True

    mem[target] = False
    return False


print(can_construct_memoization('abcdef', ['ab', 'abc','cd','def','abcd'], {}))                # True
print(can_construct_memoization('abcdefz', ['ab', 'abc','cd','def','abcd'], {}))               # False
print(can_construct_memoization('skateboard', ['bo', 'rd','ate','t','ska','sk','boar'], {}))   # False
print(can_construct_memoization('enterapotentpot', ['a','p','ent','enter','ot','o','t'], {}))  # True
print(can_construct_memoization('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef', \
    ['e','ee','eee','eeee','eeeee'], {}))    # False FAST
