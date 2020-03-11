from generate import generate_array
from graphics import plot_data


def bubble_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            counter += 1
            if arr[j + 1] >= arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            # counter += 1
    print(arr)
    print(counter)
    return counter


def improve_bubble_sort(arr):
    flag = True
    n = len(arr) - 1
    counter = 0
    while n > 0 and flag:
        flag = False
        for i in range(0, n):
            if arr[i] > arr[i + 1]:
                flag = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            counter += 1
        n -= 1
    print(arr)
    print(counter)
    return counter


def insertion_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            counter += 1
            arr[j + 1] = arr[j]
            j -= 1
        counter += 1
        arr[j + 1] = val
    print(arr)
    print(counter)
    return counter


algorithms = [bubble_sort, improve_bubble_sort, insertion_sort]
sizes = range(0,10,1)
arr_types = ["random", "best", "worst"]
result = {}

for algorithm in algorithms:
    alg_name = algorithm.__name__
    # print(alg_name)
    result[alg_name] = {}
    for size in sizes:
        # print(alg_name + " " + str(size))
        result[alg_name][size] = {}
        for arr_type in arr_types:
            print(alg_name + " " + str(size) + " " + arr_type)
            array = generate_array(size, arr_type)
            compares = algorithm(array)
            result[alg_name][size][arr_type] = compares

for alg_name in result:
    temp = {}
    for size in result[alg_name]:
        for arr_type in result[alg_name][size]:
            if temp.get(arr_type) is None:
                temp[arr_type] = {}
            temp[arr_type][size] = result[alg_name][size][arr_type]
    result[alg_name] = temp

plot_data(result)
