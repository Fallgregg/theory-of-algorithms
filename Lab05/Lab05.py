import random


def countingSort(arr, diapason, digit):
    arr_len = len(arr)
    temp = [0] * diapason
    arr_sorted = [0] * arr_len
    for i in range(0, arr_len):
        index = arr[i] // digit % 10
        temp[index] += 1
    for i in range(1, diapason):
        temp[i] += temp[i - 1]
    for i in range(arr_len - 1, -1, -1):
        index = arr[i] // digit % 10
        arr_sorted[temp[index] - 1] = arr[i]
        temp[index] -= 1
    arr = arr_sorted
    return arr_sorted


def radixSort(arr, digit):
    current_digit = 1
    result = arr
    while current_digit != 10 ** digit:
        result = countingSort(result, 10, current_digit)
        current_digit *= 10
    return result


n = int(input("Number of elements: "))
d = int(input("Number of digits: "))
array = [random.randint(10 ** (d - 1), 10 ** d - 1) for i in range(n)]
print("Not sorted:", array)
res = radixSort(array, d)
print("Sorted:", res)


