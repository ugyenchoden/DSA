arr = [7, 12, 9, 11, 3]

def insertion_sort(input_arr):
    n = len(input_arr)
    for i in range(1, n):
        insert_index = i
        current_value = input_arr[i]
        for j in range(i-1, -1, -1):
            if input_arr[j] > current_value:
                # shift
                input_arr[j+1] = input_arr[j]
                insert_index = j 
            else:
                break
        input_arr[insert_index] = current_value
    print(input_arr)

insertion_sort(arr)