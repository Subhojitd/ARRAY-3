def reverseStr(s, k):
    s = list(s)
    n = len(s)

    for i in range(0, n, 2 * k):
        start = i
        end = min(i + k - 1, n - 1)

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    return ''.join(s)

s = "abcdefg"
k = 2
print(reverseStr(s, k))
