import random

def binarySearch(li, element):
    li.sort() #sorts our list, necessary step
    top = len(li)
    bottom = 0

    while top-1 > bottom:
        print(len(li[bottom:top]))
        middle = (top + bottom)//2 #find the middle of our list
        if element == li[middle]:
            return middle
        elif element < li[middle]: #looks at lower half of our list
            top = middle
        elif element > li[middle]: #looks at top half of our list
            bottom = middle

    return -1

li = [int(1000*random.random()) for i in range(10000)]
print(binarySearch(li, li[random.randrange(0, len(li))]))