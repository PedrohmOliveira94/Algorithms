import random

def selectionSort(li):
    indexing_len = range(0, len(li)-1)

    for i in indexing_len:
        min_value = i

        for j in range(i+1, len(li)):
            if li[j] < li[min_value]:
                min_value = j

        if min_value != i:
            li[min_value], li[i] = li[i], li[min_value]

    return li


li = [int(1000*random.random()) for i in range(100)]
print(selectionSort(li))