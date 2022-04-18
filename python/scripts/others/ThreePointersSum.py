array = [1,3,5,7,8,25,45,59]
target = 18

array.sort()
result = []
for i in range(len(array) - 2):
    left = i + 1
    right = len(array) - 1
    while left < right:
        currSum = array[i] + array[left] + array[right]
        if currSum == target:
             print([array[i], array[left], array[right]])
             break
             left += 1
             right -= 1
        elif currSum < target:
             left += 1
        elif currSum > target:
             right -= 1
