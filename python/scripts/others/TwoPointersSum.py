array = [1,3,5,7,8,25,45,59]
target = 13

left = 0
right = len(array)-1

while (left < right):
    if array[left] + array[right] == target:
        print(array[left], array[right])
    if array[left] + array[right] > target:
        right-=1
    else:
        left+=1
