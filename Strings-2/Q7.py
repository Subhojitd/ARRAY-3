def applyBackspace(string):
    stack = []

    for char in string:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()

    return ''.join(stack)

def backspaceCompare(s, t):
    s_clean = applyBackspace(s)
    t_clean = applyBackspace(t)

    return s_clean == t_clean

s = "ab#c"
t = "adccc#c"
print(backspaceCompare(s, t))
