def findMissingRanges(nums, lower, upper):
    result = []

    if lower < nums[0]:
        result.append([lower, nums[0] - 1])

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] + 1:
            result.append([nums[i - 1] + 1, nums[i] - 1])

    if upper > nums[-1]:
        result.append([nums[-1] + 1, upper])

    return result

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))
