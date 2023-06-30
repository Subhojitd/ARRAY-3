def findPermutation(s):
    n = len(s)
    perm = [0] * (n + 1)
    low, high = 0, 0

    for i in range(n):
        if s[i] == 'I':
            perm[i] = low
            low += 1
        else:
            perm[i] = high
            high -= 1

    perm[n] = low  # or high, since low and high will be the same

    return perm

s1= "lDlD"
print(findPermutation(s1))