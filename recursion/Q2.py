def isValid(s):
    stack = []
    
    for char in s:
        if char == '(' or char == '*':
            stack.append(char)
        elif char == ')' and stack:
            stack.pop()
        elif char == ')' and not stack:
            if '*' in stack:
                stack.remove('*')
            else:
                return False
    
    return len(stack) == 0

# Test the function
s = "()"
print(isValid(s)) 
