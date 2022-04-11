import random

def quickSort(li):
    length = len(li)
    if length <= 1:
        return li
    else:
        pivot = li.pop()

    items_greater = []
    items_lower = []

    for item in li:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

li = [int(1000*random.random()) for i in range(100)]
print(quickSort(li))