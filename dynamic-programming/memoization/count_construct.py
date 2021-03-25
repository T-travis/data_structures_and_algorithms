# Write a function count_construct(target, word_bank) that accepts a target
# and an array of strings.  Return the number of ways the target can be constructed
# by combining the elements including reusing element for word_bank.


# n = target length, m = word_bank length
# Time Complexity  O(n*m^4)
# Space Complexity O(m^4) 
#   m^4 because python list slice is O(n) done twice each call for m calls
def count_construct(target, word_bank):

    if target == '': return 1

    count = 0

    for word in word_bank:
        if word == target[:len(word)]:
            way = count_construct(target[len(word):], word_bank)
            count += way

    return count


# print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))             # 2
# print(count_construct('abcdef', ['ab', 'abc','cd','def','abcd']))                # 1
# print(count_construct('abcdefz', ['ab', 'abc','cd','def','abcd']))               # 0
# print(count_construct('skateboard', ['bo', 'rd','ate','t','ska','sk','boar']))   # 0
# print(count_construct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))  # 3
# print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef', \
#     ['e','ee','eee','eeee','eeeee']))    # 0 SLOW



# n = target length, m = word_bank length
# Time Complexity  O(n^m*m^4)
# Space Complexity O(m^4)
def count_construct_mem(target, word_bank, mem):

    if target in mem.keys():
        return mem[target]

    if target == '': return 1

    count = 0

    for word in word_bank:
        if word == target[:len(word)]:
            way = count_construct_mem(target[len(word):], word_bank, mem)
            count += way
            #mem[target] = count not needed as we aren't returning 

    mem[target] = count
    return count


print(count_construct_mem('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))             # 2
print(count_construct_mem('abcdef', ['ab', 'abc','cd','def','abcd'], {}))                # 1
print(count_construct_mem('abcdefz', ['ab', 'abc','cd','def','abcd'], {}))               # 0
print(count_construct_mem('skateboard', ['bo', 'rd','ate','t','ska','sk','boar'], {}))   # 0
print(count_construct_mem('enterapotentpot', ['a','p','ent','enter','ot','o','t'], {}))  # 4
print(count_construct_mem('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef', \
    ['e','ee','eee','eeee','eeeee'], {}))    # 0 SLOW