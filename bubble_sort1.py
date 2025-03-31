def bubble_sort(ages):
    n = len(ages)
    for i in range(n):
        for j in range(0, n-i-1):
            if ages[j] > ages[j+1]:
                # Complete the following line to swap the elements at positions j and j+1
                ages[j], ages[j+1] = ages[j+1], ages[j]

    return ages