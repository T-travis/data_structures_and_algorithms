# String Permutation Problem

def permutations(string):
    _permutations(list(string), 0, len(string))


def _permutations(string, start, end):
    if start == end-1:
        print(''.join(string))
    else:
        for i in range(start, end):
            # pythonic swap : )
            string[start], string[i] = string[i], string[start]
            _permutations(string, start+1, end)
            string[start], string[i] = string[i], string[start]


permutations('123')
print()


# no aux data structures like above
def string_permutations(string):
    _string_permutations(string, "")


def _string_permutations(s, permutation):
    if len(s) == 0:
        print(permutation)
    else:
        for i in range(len(s)):
            firstChar = s[i:i+1]
            restOfString = s[0:i] + s[i+1:]
            _string_permutations(restOfString, permutation + firstChar)

    
string_permutations('123')


