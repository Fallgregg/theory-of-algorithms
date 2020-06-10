def open_file():  # функці зчитування з файлу
    file = open(input("File: "))
    arr = []
    w, n = tuple([int(x) for x in file.readline().split()])
    for line in file:
        i, j = tuple([int(x) for x in line.split()])
        arr.append((int(i), int(j)))
    return arr, w


def write_file():  # функція запису у файл
    file = open('ZabilskaV_output.txt', 'w')
    file.write(str(result))
    file.close()


def find_knapsack(items, w):
    memo = {}  # словник для мемоізації

    def knapsack(index, space):  # функція для пошуку максимальної суми
        if index == 0 or space == 0:  # базова умова
            return 0
        key = str([index, space])
        wt = items[index][1]
        if key in memo:  # перевірка значення функції в таблиці мемоізаціїї
            return memo[key]
        elif wt > space:  # перевірка на перевищення вмісткості
            memo[key] = knapsack(index - 1, space)  # попереднє значення
            return memo[key]
        else:
            payload = items[index][0]  # сумарна ціна на даний момент
            memo[key] = max(knapsack(index - 1, space - wt) + payload, knapsack(index - 1, space))  # пошук максимальної суми
            return memo[key]  # максимальне значення записане в таблицю мемоізації
    return knapsack(len(items) - 1, w)


array, capacity = open_file()
result = find_knapsack(array, capacity)
write_file()
