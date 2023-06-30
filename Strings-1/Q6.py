def findOriginalArray(changed):
    count_dict = {}

    for num in changed:
        count_dict[num] = count_dict.get(num, 0) + 1

    original = []

    for num in changed:
        if count_dict.get(2 * num, 0) == 0:
            return []
        else:
            count_dict[2 * num] -= 1
            original.append(num)

    return original

changed = [1,2,3,2,4,6]
print(findOriginalArray(changed))