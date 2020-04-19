from pip._vendor.distlib.compat import raw_input


class Heap:

    def __init__(self, arr, is_max):
        """конструктор класу Heap,
        що ініціалізує масив як піраміду,
        та встановлює фложок для перевірки
        максимального розміру піраміди"""
        self.heap = arr
        self.is_max = is_max

    size = -1
    is_max = False
    heap = []

    def buildHeap(self):
        """функція що проходить по кожному з вузлів
        та винокує для них процедуру max_heapify"""
        self.size = len(self.heap) - 1
        for i in range(len(self.heap) // 2, -1, -1):
            self.max_heapify(self.heap, i)

    def max_heapify(self, arr, counter):
        """функція опускає значення arr[i] вниз до тих пір,
        доки піддерево з корнем, щ о відповідає i, не буде
        незростаючаою пірамідою"""

        l_ch = left_child(counter)
        r_ch = right_child(counter)
        h_peak = counter

        if self.is_max:
            if l_ch <= self.size and arr[l_ch] > arr[counter]:
                h_peak = l_ch

            if r_ch <= self.size and arr[r_ch] > arr[h_peak]:
                h_peak = r_ch
        else:
            if l_ch <= self.size and arr[l_ch] < arr[counter]:
                h_peak = l_ch

            if r_ch <= self.size and arr[r_ch] < arr[h_peak]:
                h_peak = r_ch

        if h_peak is not counter:
            arr[counter], arr[h_peak] = arr[h_peak], arr[counter]
            self.max_heapify(arr, h_peak)

    def insert_max(self, key):
        """ функція, що всталяє вузол до піраміди"""

        self.size += 1
        counter = self.size
        self.heap.append(key)
        while counter > 0 and (
                (self.heap[parent(counter)] < key and self.is_max) or
                (self.heap[parent(counter)] > key and not self.is_max)
        ):
            self.heap[counter] = self.heap[parent(counter)]
            counter = parent(counter)
        self.heap[counter] = key


def parent(counter):
    """функція для знаходження індекса батьківського вузла"""

    return (counter - 1) // 2


def right_child(counter):
    """" функція для знаходження індекса правого дочірнього вузла"""

    return 2 * counter + 2


def left_child(counter):
    """функція для знаходження індекса лівого дочірнього вузла"""

    return 2 * counter + 1


def check_heaps(h_low, h_high):
    """функція для визначення, в яку піраміду (heapHigh, heapLow) додавати новий елемент"""

    if h_high.size - h_low.size > 1:
        h_low.insert_max(h_high.heap.pop(0))
        h_high.buildHeap()

    if h_low.size - h_high.size > 1:
        h_high.insert_max(h_low.heap.pop(0))
        h_low.buildHeap()


def median(h_low, h_high, length):
    """функція пошуку медіани відсортвоаного масиву, використовуючи heapHigh та  heapLow"""

    if(length + 1) % 2:
        if h_low.size > h_high.size:
            res = h_low.heap[0]
        else:
            res = h_high.heap[0]
    else:
        res = [h_low.heap[0], h_high.heap[0]]

    return res


def sequence(arr):
    """функція для знаходження пірамід heapHigh та  heapLow"""

    h_low = Heap([], True)
    h_high = Heap([], False)
    res = []

    h_low.insert_max(arr[0])
    res.append(arr[0])

    for counter in range(1, len(arr)):
        temp = arr[counter]
        if temp < h_low.heap[0]:
            h_low.insert_max(temp)
        else:
            h_high.insert_max(temp)

        check_heaps(h_low, h_high)

        res.append(median(h_low, h_high, counter))
    return res


"""достємо вхідні дані із введеного з консолі файлу"""

array = [int(s) for s in [line.strip() for line in open(raw_input('Enter file name:\n'), 'r')]]
array.pop(0)

result = sequence(array)

"""записуємо вихідні дані у файл"""
outputFile = open('output.txt', 'w')
for item in result:
    if isinstance(item, list):
        outputFile.write("%s %s\n" % (item[0], item[1]))
    else:
        outputFile.write("%s\n" % item)

