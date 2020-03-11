import random


def generate_array(n, arr_type="best"):
    arr = [i + 1 for i in range(n)]
    if arr_type == "worst":
        arr.reverse()
    elif arr_type == "random":
        random.shuffle(arr)
    return arr
