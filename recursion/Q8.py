def buddyStrings(s, goal):
    if len(s) != len(goal) or set(s) != set(goal):
        return False

    if s == goal:
        return len(set(s)) < len(s)

    diff_pairs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_pairs.append((s[i], goal[i]))
            if len(diff_pairs) > 2:
                return False

    return len(diff_pairs) == 2 and diff_pairs[0] == diff_pairs[1][::-1]

s = "ab"
goal = "ba"
can_swap = buddyStrings(s, goal)
print(can_swap)
