class Node:
    def __init__(self, key, next_el):
        self.key = key
        self.next_el = next_el


class LinkedList:  # класс, що відповідає за створення зв'язного списку
    def __init__(self):  # конструктор, що ініціалізує початок та кінець таблиці та її довжину
        self.head = None
        self.tail = None
        self.length = 0

    def shift(self, key):  # функція для вставки ключа у комірку 
        self.length += 1
        temp = Node(key, self.head)
        if self.tail is None:
            self.tail = temp
        self.head = temp

    def search(self, key):  # функція для перевірки чи комірка порожня
        temp = self.head
        if temp is not None:
            while (temp.key != key) and (temp.next_el is not None):
                temp = temp.next_el
            if temp.key == key:
                return True
        return False


class Hash(object):  # клас, що відпідає за хеш - таблиці
    def __init__(self, length):  # конструктор, що ініціалізує хеш - таблицю, її довжину та кількість колізій
        self.table = None
        self.length = length
        self.collisions = 0


class ChainedHash(Hash):  # клас, зо відповідає за хеш - таблиці
    def __init__(self, length):  # конструктор, що ініцілізує хеш - таблицю
        super(ChainedHash, self).__init__(length)
        self.table = [LinkedList() for i in range(length)]

    def insert(self, key):  # функція для вставки ключа в хеш - таблицю а також підрахунку колізій
        position = self.hash(key)
        if self.table[position].search(key) is False:
            self.table[position].shift(key)
            if self.table[position].length > 1:
                self.collisions += 1

    def search(self, key):  # функція для пошуку позиції елемента в хеш - таблиці
        position = self.hash(key)
        return self.table[position].search(key)


class DivisionHash(ChainedHash):  # функція для реалізації метода ділення
    def hash(self, key):
        return key % self.length


class MultiplicationHash(ChainedHash):  # функція для реалізації метода множення
    def hash(self, key):
        return int(self.length * ((key * 0.6180339887) % 1))


def write_file(array, file_name):  # функція для запису даних у вихідний файл
    output_file = open(file_name + '.txt', 'w')
    for item in array:
        if isinstance(item, list):
            output_file.write("%s %s\n" % (item[0], item[1]))
        else:
            output_file.write("%s\n" % item)


def write_result(div, mult):  # функція для створення вихідних файлів згідно методу
    file_name = 'output'
    write_file(div, file_name + '_division')
    write_file(mult, file_name + '_multiplication')


def parse_file(f):  # функція для діставання вхідних даний з файлу
    n = f.readline().split()
    d = [0] * int(n[0])
    s = [0] * int(n[1])

    for i in range(int(n[0])):
        d[i] = int(f.readline())
    for i in range(int(n[1])):
        s[i] = int(f.readline())
    return d, s


def test(d, s, hash_table):  # функція для пошуку у хеш - таблиці значень що у сумі дають небхідні числа
    res = []
    h = hash_table(3 * len(d))

    for x in d:
        h.insert(x)
    res.append(h.collisions)
    for s in s:
        for x in d:
            if h.search(s - x):
                res.append([x, s - x])
                break
        else:
            res.append([0, 0])
    return res


file = open(input('enter file name: '))
data, sums = parse_file(file)

div = test(data, sums, DivisionHash)
mult = test(data, sums, MultiplicationHash)

write_result(div, mult)
