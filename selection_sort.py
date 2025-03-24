arr = [7,12,9,11,3]

def selection_sort(input_arr):
    n = len(input_arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if input_arr[j] < input_arr[i]:
                min_index = j
        input_arr[i], input_arr[min_index] = input_arr[min_index], input_arr[i]
    print(input_arr)

selection_sort(arr)