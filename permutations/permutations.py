# Permutation = set or number of things can be ordered or arranged
# Example [a,b,c] = [c,b,a], [b,c,a], [b,a,c], [c,a,b], [a,c,b], [a,b,c]
# There are n! permutations for a set of n items
# https://www.youtube.com/watch?v=us0cYQXQpxg&list=PLxQ8cCJ6LyOZHhAjIYrEFWcfYdyJl5VYf&index=7

#                        [ ]
#                        [a]                         empty so insert
#          [b,a]                     [a,b]           insert 'b' into all different locations
# [c,a,b] [b,c,a] [b,a,c]   [c,a,b] [a,c,b] [a,b,c]  insert 'c' into all different locations
# final = [ [c,b,a], [b,c,a], [b,a,c], [c,a,b], [a,c,b], [a,b,c] ]
 
 # Time Complexity O(N!) factorial
 # Space Complexity O(N^2) because the slices can be up to N
 
def permutations(arr):
    """return a list of list permutations"""
    if len(arr) == 0: return [[]]
    first_element = arr[0]
    remaining_elements = arr[1:]
    perms_without_first = permutations(remaining_elements)
    all_perms = []
    for perm in perms_without_first:
        for i in range(len(perm) + 1):
            pre = perm[0:i]
            post = perm[i:]
            all_perms.append(pre + [first_element] + post)

    return all_perms


def str_permutations(string):
    """return a list of string permutations"""
    print(_str_permutations('', string, []))

def _str_permutations(prefix, string, res):
    if not string: res.append(prefix)
    for i in range(len(string)):
        _str_permutations(prefix + string[i], string[0:i] + string[i + 1:],res)
    return res


def print_str_permutations(string):
    """print all permutations"""
    _print_str_permutations('', string, [])

def _print_str_permutations(prefix, string):
    if not string: print(prefix)
    for i in range(len(string)):
        _print_str_permutations(prefix + string[i], string[0:i] + string[i + 1:])

    

if __name__ == '__main__':
    print(permutations(['a', 'b', 'c']))
    print_str_permutations('abc')
    