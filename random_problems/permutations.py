# Determine if two strings/arrays are permutations of each other.
# example: 'hello' and 'leloh' is True

# STRING implementaion:

def ispermutation(str1, str2):
    # assuming a None type can't be a permutation
    # and empty strings are not permutations
    if str1 is None or str2 is None:
        return False
    elif len(str1) == 0 or len(str2) == 0:
        return False
    elif len(str1) != len(str2):
        return False

    for char in str1:
        if not (char in str2):
            return False
        
    return True


assert ispermutation(None, "a") == False
assert ispermutation("a", None) == False
assert ispermutation("", "afasdf") == False
assert ispermutation("afasdf", "") == False
assert ispermutation("aa", "aaa") == False
assert ispermutation("abc", "cab") == True
assert ispermutation("abc", "caz") == False


# ARRAY/LIST implementation

def arr_ispermutation(list1, list2):

    if list1 is None or list2 is None:
        return False
    elif len(list1) == 0 or len(list2) == 0:
        return False
    elif len(list1) != len(list2):
        return False

    for char in list1:
        if not (char in list2):
            return False

    return True


assert arr_ispermutation(None, ["a"]) == False
assert arr_ispermutation(["a"], None) == False
assert arr_ispermutation([""], ["a", "f", "a", "s", "d", "f"]) == False
assert arr_ispermutation(["a", "f", "a", "s", "d", "f"], [""]) == False
assert arr_ispermutation(["a", "a"], ["a", "a", "a"]) == False
assert arr_ispermutation(["a", "b", "c"], ["c", "a", "b"]) == True
assert arr_ispermutation(["a", "b", "c"], ["c", "a", "z"]) == False
