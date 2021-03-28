# Write a function all_construct(target, word_bank) that accepts a target
# and an array of strings. Return a 2D array containing all the ways that target 
# can be constructed by combining elements of word_bank.  Elements from word_bank
# be reused.


# n = target, m = word_bank
# Time Complexity O(n^m)
# Space Comeplexity O(n)
def all_construct(target, word_bank, mem):

    if target in mem.keys(): return mem[target]
    
    if target == '': return [[]]

    ways = []

    for word in word_bank:
        if word == target[:len(word)]:
            way = all_construct(target[len(word):], word_bank, mem)
            for arr in way:
                arr.append(word)
            ways += way

    mem[target] = ways
    return ways


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))  # [[[purp, le], [p, ur, p, le]]]
print(all_construct('abcdef', ['ab', 'abc','cd','def','abcd'], {}))                # [['def', 'abc']]
print(all_construct('', ['ab', 'abc','cd','def','abcd'], {}))                    # [[]]
print(all_construct('skateboard', ['bo', 'rd','ate','t','ska','sk','boar'], {}))   # []
# [
#   ['ot', 'p', 'ent', 'ot', 'p', 'a', 'enter'], ['t', 'o', 'p', 'ent', 'ot', 'p', 'a', 'enter'], 
#   ['ot', 'p', 'ent', 't', 'o', 'p', 'a', 'enter'], ['t', 'o', 'p', 'ent', 't', 'o', 'p', 'a', 'enter']
# ]
print(all_construct('enterapotentpot', ['a','p','ent','enter','ot','o','t'], {}))   
print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef', \
    ['e','ee','eee','eeee','eeeee'], {}))    # 0 SLOW

