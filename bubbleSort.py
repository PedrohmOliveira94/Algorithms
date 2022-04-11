import random

def bubble(li):
    indexing_len = len(li) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_len):
            if li[i] > li[i+1]:
                sorted = False
                li[i], li[i+1] = li[i+1], li[i]  #flip the items

    return li

li = [int(1000*random.random()) for i in range(100)]
print(bubble(li))