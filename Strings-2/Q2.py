def is_strobogrammatic(num):
    digit_map = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in digit_map or num[right] not in digit_map:
            return False

        if digit_map[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True

num = "69"
print(is_strobogrammatic(num))  
