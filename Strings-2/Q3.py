def addStrings(num1, num2):
    result = ""
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry != 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        _sum = x + y + carry
        result = str(_sum % 10) + result
        carry = _sum // 10
        i -= 1
        j -= 1

    return result

num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
