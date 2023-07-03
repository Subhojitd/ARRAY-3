from collections import Counter

def findAnagrams(s, p):
    result = []
    window_size = len(p)
    p_count = Counter(p)
    window_count = Counter(s[:window_size])

    if window_count == p_count:
        result.append(0)

    for i in range(1, len(s) - window_size + 1):
        # Remove the leftmost character from the window count
        if window_count[s[i - 1]] == 1:
            del window_count[s[i - 1]]
        else:
            window_count[s[i - 1]] -= 1

        # Add the rightmost character to the window count
        if s[i + window_size - 1] in window_count:
            window_count[s[i + window_size - 1]] += 1
        else:
            window_count[s[i + window_size - 1]] = 1

        # Check if the window is an anagram of p
        if window_count == p_count:
            result.append(i)

    return result

s = "cbaebabacd"
p = "abc"
indices = findAnagrams(s, p)
print(indices)
