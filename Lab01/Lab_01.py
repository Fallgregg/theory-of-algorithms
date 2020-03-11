import random


def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if arr[j + 1] >= arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


n = int(input("Enter number of elements: "))
array = [random.randint(1, 1000) for i in range(n)]
print("Array (not sorted): ", array)
bubbleSort(array)
print("Array (sorted): ", array)
