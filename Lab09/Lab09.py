import math


def open_file():  # функція зчитування даних з файлу
    file = open(input("File: "))
    n = int(file.readline())
    arr = []
    for i in range(n):
        arr.append([])
    split = file.readlines()
    for i in range(n):
        current_line = split[i].split()
        arr[i].append(int(current_line[0]))
        arr[i].append(int(current_line[1]))
    file.close()
    return arr, n


def write_file():  # функція запису в файл
    file = open('Zabilska_Valeria_IS93_output.txt', 'w')
    file.write(str(result) + "\n" + str(result_way))
    file.close()


def find_way(arr, curr):  # функція пошуку найкоротшого шляху
    checked = [False] * size  # зміння для мемоезації - перевірка пройдених вершин
    checked[curr] = True  # поточний - пройдений
    res = 0
    res_way = [curr]
    for j in range (size - 1):
        min = 4294967295
        for i in range(size):
            if not checked[i]:
                len = math.hypot(arr[i][0] - arr[curr][0], arr[i][1] - arr[curr][1])
                if len < min:  # пошук мінімальної довжини між містами
                    min = len
                    closest = i
        curr = closest
        checked[closest] = True
        res += min
        res_way.append(closest)
    return round(res), res_way


array, size = open_file()

temp, temp_way = find_way(array, 0)  # беремо вершину 0 як стартову
result = temp
result_way = temp_way

for i in range(1, size):  # перевіряємо відстані беручи інші вершини стартовими
    temp, temp_way = find_way(array, i)
    # print(result)
    if temp < result:
        result = temp
        result_way = temp_way

write_file()

# print(result)
# print(result_way)
# print(len(result_way))
