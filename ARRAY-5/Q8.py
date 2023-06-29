from collections import defaultdict

def findOriginalArray(changed):
    count = defaultdict(int)

    for num in changed:
        count[num] += 1

    changed.sort()

    original = []

    for num in changed:
        if count[2 * num] > 0:
            original.append(num)
            count[2 * num] -= 1
        else:
            return []

    return original

changed = [1,3,4,2,6,8]
print(findOriginalArray(changed))