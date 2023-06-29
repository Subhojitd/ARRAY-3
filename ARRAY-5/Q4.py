def findDisappearedNumbers(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    nums1_diff = list(nums1_set - nums2_set)
    nums2_diff = list(nums2_set - nums1_set)

    answer = [nums1_diff, nums2_diff]
    return answer

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDisappearedNumbers(nums1,nums2))
