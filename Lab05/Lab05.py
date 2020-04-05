import random


def countingSort(arr,  digit):
    arr_len = len(arr)
    temp = [0] * 10    # масив для тимчасового сховища
    arr_sorted = [0] * arr_len  # масив, в який запишемо відсортований масив
    for i in range(0, arr_len):
        index = arr[i] // digit % 10  # знаходимо значення (0..9) i-того елемента масиву на поточному розряді
        temp[index] += 1  # для знайденого значення знаходимо кількість разів, коли це значення зустрічаєтся
    for i in range(1, 10):  # записуємо в temp на i-ту позицію кількість елементів 0..9 на поточному розряді
        temp[i] += temp[i - 1]
    for i in range(arr_len - 1, -1, -1):
        index = arr[i] // digit % 10  # знаходимо значення (0..9) i-того елемента масиву на поточному розряді
        arr_sorted[temp[index] - 1] = arr[i]  # записуємо у відсортований масив на відповідну позицію i-тий елемент
        temp[index] -= 1
    arr = arr_sorted
    return arr_sorted


def radixSort(arr, digit):
    current_digit = 1  # змінна для визначення поточного розряду
    result = arr
    while current_digit != 10 ** digit:  # виконується поки не відсортуємо за кожним разрядом
        result = countingSort(result, current_digit)  # сортуємо кожний розряд елементів вхідного масиву
        current_digit *= 10  # кожну ітерацію збільшуємо степінь числа 10, таким чином переходячи на новий розряд
    return result


n = int(input("Number of elements: "))  # задаємо кількість елементів масиву
d = int(input("Number of digits: "))  # задаємо кількість розрядів чисел
array = [random.randint(10 ** (d - 1), 10 ** d - 1) for i in range(n)]   # генерація масиву, зважаючи на розряди
print("Not sorted:", array)
res = radixSort(array, d)
print("Sorted:", res)

