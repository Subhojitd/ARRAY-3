def findMaxLength(nums):
    max_length = 0
    count = 0
    count_dict = {0: -1}

    for i in range(len(nums)):
        num = nums[i]
        if num == 1:
            count += 1
        else:
            count -= 1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length

nums = [0,0,1,1]
print(findMaxLength(nums))