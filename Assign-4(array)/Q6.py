def sortedSquares(nums):
    squared = [num * num for num in nums]
    squared.sort()
    return squared

nums = [-4,3,5,-2,32]
print(sortedSquares(nums))