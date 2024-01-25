import random
from collections import deque
BUCKETS = 10 #10진법
DIGITS = 4 # 4자릿수 숫자 정렬 가능

def checkSortFunc(func) :
    data = [6, 3, 2, 7, 9, 1, 8]
    print("Origin : ", data)
    func(data)
    print("Sort : ", data)

def selection_sort(lst) :
    n = len(lst)
    for i in range(n-1):
        least = i
        for j in range(i+1, n) :
            if (lst[j]<lst[least]) :
                least = j
        lst[i], lst[least] = lst[least], lst[i]
        print("Step : %2d " % (i+1), lst)
            
def insert_sort(lst) :
    n = len(lst)
    for i in range(1, n) :
        key = lst[i]
        j = i-1
        while j>=0 and lst[j] > key :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
        print("Step : %2d " % (i+1), lst)
        
def quick_sort(lst, left, right) :
    if left < right :
        q = partition(lst, left, right)
        quick_sort(lst, left, q -1)
        quick_sort(lst, q + 1, right)
        
def partition(lst, left, right) :
    pivot = lst[left]
    low = left + 1
    high = right
    
    while (low < high) :
        while low <= right and lst[low] <= pivot :
            low += 1
        
        while high >= left and lst[high] > pivot:
            high -= 1
            
        if low < high :
            lst[low], lst[high] = lst[high],  lst[low]
        
    lst[left], lst[high] = lst[high],  lst[left]       
    return high

def radix_sort(lst) :
    queues = []
    for i in range(BUCKETS) :
        queues.append(deque())
        
    n = len(lst)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) :
            queues[(lst[i]//factor) % BUCKETS].append(lst[i])
            
        i = 0
        for b in range(BUCKETS):
            while queues[b] :
                lst[i] = queues[b].popleft()
                i += 1
        factor *= BUCKETS
        print("Step", d+1, lst)

#Selection Sort            
checkSortFunc(selection_sort)
print()
#Insert Sort Test
checkSortFunc(insert_sort)
print()

#Quick Sort Test
data = random.sample(range(1, 1000), 10)
print("Origin : ", data)
quick_sort(data, 0, len(data)-1)
print("Sort : ", data)

#Radix Sort Test
data = [random.randint(1,9999) for _ in range(10)]
radix_sort(data)
print("Radix : ", data)

