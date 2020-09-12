def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


array = [10, 13, 5, 1, 3, 2]
n = len(array)

print("Given array is:")
for i in range(n):
    print(array[i])

quickSort(array, 0, n - 1)

print("Sorted array is:")
for i in range(n):
    print(array[i])
