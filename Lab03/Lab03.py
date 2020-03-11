from generate import generate_array
from graphics import plot_data
from graphics import plot_ratio
import time


def merge_sort(arr, l, r):
    if l < r:
        m = ((l + (r - 1)) // 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    left, right = arr[:m], arr[m:]

    i, j = 0, 0
    for k in range(l, r + 1):
        if j >= len(right) or (i < len(left) and left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def insertion_sort(arr, l, r):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val


algorithms = [merge_sort, insertion_sort]
sizes = range(3, 100, 1)
repeats = 500
result = {}

for _ in range(repeats):
    # print('Repeat: {}'.format(_ + 1))
    for size in sizes:
        array = generate_array(size, 'random')
        if result.get(size) is None:
            result[size] = {}
        for algorithm in algorithms:
            alg_name = algorithm.__name__
            if result[size].get(alg_name) is None:
                result[size][alg_name] = []
            start = time.perf_counter()
            algorithm(array.copy(), 0, size - 1)
            end = time.perf_counter()
            result[size][alg_name].append(end - start)

temp_res = {}
for size in result:
    for alg_name in result[size]:
        if temp_res.get(alg_name) is None:
            temp_res[alg_name] = {}
        temp_res[alg_name][size] = sum(result[size][alg_name]) / len(result[size][alg_name])
result = temp_res

ratios = {size: result['insertion_sort'][size] / result['merge_sort'][size] for size in result['insertion_sort']}
print(ratios)
prev = None
for size in ratios:
    if prev is None:
        prev = size
    if ratios[prev] <= 1 and ratios[size] > 1:
        print("Intersection n is: ", prev if abs(1 - ratios[prev]) >= abs(1 - ratios[size]) else size)
        break
    prev = size

# plot_ratio(ratios)

plot_data(result)
