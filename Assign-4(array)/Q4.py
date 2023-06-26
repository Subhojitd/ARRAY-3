def PairSum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum

nums1 = [12,4,5,7,1]
print(PairSum(nums1))
