def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # solution steps:
        # place openings in stack
        # if closing 
        #   stack not empty, 
        #   get index from openings from top of stack
        #   get index from closings from closing found
        #   if indexes are not equal return False
        # last return True is stack is empty

        # Assumption is 's' will only be parentheses

        # 0 parentheses is valid
        if len(s) == 0:
            return True

        opening = ['{', '[', '(']
        closing = ['}', ']', ')']
        # python stack:
        # list with append() for add and pop() for remove
        stack = []
        valid = False

        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if len(stack) > 0:
                    open_index = opening.index(stack.pop())
                    close_index = closing.index(char)
                    if open_index != close_index:
                        return False
                else:
                    return False

        # no openings can be left on the stack or it is not valid
        return len(stack) == 0


assert isValid('{[]{()}}') == True
assert isValid('{[]') == False
