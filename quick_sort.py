def partition(arr, low, high):
    pivot= arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low=0, high= None):
    if high is None:
        high = len(arr)-1
    
    if low < high:
        pivotIndex= partition(arr,low, high)
        quicksort(arr, low, pivotIndex-1)
        quicksort(arr, pivotIndex+1, high)

arr = [7,12,9,11,3]
quicksort(arr)
print(arr)