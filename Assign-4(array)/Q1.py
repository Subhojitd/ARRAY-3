def arraysIntersection(arr1,arr2,arr3):
    
    ptr1,ptr2,ptr3 = 0,0,0
    result = []

    while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
        num1, num2, num3 = arr1[ptr1], arr2[ptr2], arr3[ptr3]

        if num1 == num2 == num3:
            result.append(num1)
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        elif num1 <= num2 and num1 <= num3:
            ptr1 += 1
        elif num2 <= num1 and num2 <= num3:
            ptr2 += 1
        else:
            ptr3 += 1

    return result 

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(arraysIntersection(arr1, arr2, arr3))