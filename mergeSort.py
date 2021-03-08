# Code By Saideep Shetty
def merge(array, left, middle, right):

    a = middle - left + 1
    b = right - middle

    Left_temp = [0] * a
    Right_temp = [0] * b

    for i in range(0, a):
        Left_temp[i] = array[left + i]

    for j in range(0, b):
        Right_temp[j] = array[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < a and j < b:
        if Left_temp[i] <= Right_temp[j]:
            array[k] = Left_temp[i]
            i += 1
        else:
            array[k] = Right_temp[k]
            j += 1
        k += 1

    while i < a:
        array[k] = Left_temp[i]
        i += 1
        k += 1

    while j < b:
        array[k] = Right_temp[j]
        j += 1
        k += 1


def mergeSort(array, left, right):
    if left < right:
        middle = (left + right - 1) // 2
        mergeSort(array, left, middle)
        mergeSort(array, middle + 1, right)
        merge(array, left, middle, right)


array = [12, 11, 13, 5, 6, 7]
n = len(array)
print("Given array is")
for i in range(n):
    print(array[i])

mergeSort(array, 0, n - 1)

print("Sorted array is")
for i in range(n):
    print(array[i])
