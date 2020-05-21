# Determine is a string has all unique characters. 
# (Try without an auxiliary data structure)

# STRING solution

def isunique(str):
    return len(str) == len(set(str))


print(isunique("123"))
print(isunique("1231"))
print(isunique("1"))

print()

# ARRAY solution

def arr_isunique(list):
    return len(list) == len(set(list))


print(arr_isunique(['1', '2', '3']))
print(arr_isunique(['1', '2', '3', '1']))
print(arr_isunique(['1']))
