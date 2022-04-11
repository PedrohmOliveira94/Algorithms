import random

def insertionSort(li):
    indexing_len = range(1, len(li))
    for i in indexing_len:
        value_to_sort = li[i]

        while li[i-1] > value_to_sort and i>0:
            li[i], li[i-1] = li[i-1], li[i]
            i = i-1

    return li

li = [int(1000*random.random()) for i in range(100)]
print(insertionSort(li))