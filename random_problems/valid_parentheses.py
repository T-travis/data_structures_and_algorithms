def isValid(s):
    # push open brackets on stack
    # pop off open when reach a close and see it they match, return false if not
    
    open_brackets = ['(', '[', '{']
    complete_brackets = ['()', '[]', '{}']
    stack = []
    
    for char in s:
        if char in open_brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            bracket = stack.pop() + char
            if bracket not in complete_brackets:
                return False
        
    return len(stack) == 0


assert isValid('{[]{()}}') == True
assert isValid('{[]') == False
