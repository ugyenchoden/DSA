def binarySearch(arr, key):
    if len(arr) == 0:
        return -1
    
    if len(arr) == 1:
        return 0 if arr[0] == key else -1
    
    left = 0
    right = len(arr)+1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid -1
    
    return -1

sortedArr = [2, 3, 5, 6, 8, 10, 13, 25]
keyValue = 1

result = binarySearch(sortedArr, keyValue)
if result != -1:
    print("Value", keyValue, " was found at the index ", result)
else:
    print("Value not found")