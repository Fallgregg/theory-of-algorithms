def partition(arr, p, r):
    global counter
    x = arr[r]
    i = p - 1
    for j in range (p, r):
        counter += 1
        if arr[j] < x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)


def partition_median(arr, p, r):
    global counter2
    i = p - 1
    if arr[0] <= arr[(p + r) // 2] < arr[r]:
        pivot = arr[(p + r) // 2]
        x = (p + r) // 2
    elif arr[(p + r) // 2] < arr[0] < arr[r]:
        x = 0
        pivot = arr[0]
    else:
        x = r
        pivot = arr[r]

    for j in range(p, r):
        counter2 += 1
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[x] = arr[x], arr[i + 1]
    return i + 1


def partition_for_median(arr, p, r):
    i = p - 1
    pivot = arr[r]

    for j in range(p, r):
        global counter2
        counter2 += 1
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quickSort_for_median(arr, p, r):
    if p < r:
        pi = partition_for_median(arr, p, r)
        quickSort_for_median(arr, p, pi - 1)
        quickSort_for_median(arr, pi + 1, r)


def quickSort_median(arr, p, r):
    if p < r and r - p >= 3:
        pi = partition_median(arr, p, r)
        quickSort_median(arr, p, pi - 1)
        quickSort_median(arr, pi + 1, r)
    elif p < r:
        pi = partition_for_median(arr, p, r)
        quickSort_for_median(arr, p, pi - 1)
        quickSort_for_median(arr, pi + 1, r)


def read_from_file():
    arr = []
    for ind, line in enumerate(open("input.txt")):
        if ind != 0:
            arr.append(int(line))
    return arr


def write_to_file(count, count2):
    file = open("result.txt", 'w')
    file.write('Counter num.1:\n' + str(count) + '\nCounter num.2:\n' + str(count2))
    file.close()


arr1 = read_from_file()
n1 = len(arr1)
counter = 0
quickSort(arr1, 0, n1 - 1)

arr2 = read_from_file()
n2 = len(arr1)
counter2 = 0
quickSort_median(arr2, 0, n2 - 1)

write_to_file(counter, counter2)
