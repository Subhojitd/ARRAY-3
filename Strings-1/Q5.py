def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort()
    n = len(nums1)
    min_product_sum = 0

    for i in range(n):
        product = nums1[i] * nums2[n - 1 - i]
        min_product_sum += product

    return min_product_sum

num1 = [3,4,5,6]
num2 = [1,2,6,5]
print(minProductSum(num1,num2))

