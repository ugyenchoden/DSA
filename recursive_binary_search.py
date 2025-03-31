def binarySearch(arr, key, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # Key not found

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearch(arr, key, mid + 1, right)
    else:
        return binarySearch(arr, key, left, mid - 1)

# Test case
myArr = [2, 3, 4, 10, 40]
keyValue = 5

result = binarySearch(myArr, keyValue)
if result != -1:
    print("Element is present at index", result)
else:
    print("Not found")
