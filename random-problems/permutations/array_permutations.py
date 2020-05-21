def permutations(arr):
    _permutations(list(arr), 0, len(arr))


def _permutations(arr, start, end):
    if start == end-1:
        print(arr)
    else:
        for i in range(start, end):
            # pythonic swap : )
            arr[start], arr[i] = arr[i], arr[start]
            _permutations(arr, start+1, end)
            arr[start], arr[i] = arr[i], arr[start]


permutations([1, 2, 3])
print()


def array_permutations(string):
    return _array_permutations(string, [], [])


def _array_permutations(arr, permutation, res):
    if len(arr) == 0:
        res.append(permutation)
    else:
        for i in range(len(arr)):
            first = arr[i:i+1]
            restOfArray = arr[0:i] + arr[i+1:]
            _array_permutations(restOfArray, permutation + first, res)
    return res

print( array_permutations([1,2,3]) )
