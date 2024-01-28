#순차탐색
def sequntial_serch(A, key, low, high) :
    for i in range(low, high) :
        if A[i] == key :
            return i
        return -1
    
#교환 전략을 더한 순차탐색
def sequntial_serch_transpose(A, key, low, high) :
    for i in range(low, high) :
        if A[i] == key :
            if i > low :
                A[i], A[i-1] = A[i-1], A[i]
            return i
        return -1
    
#이후 탐색은 오름차순 정렬이 되어 있다고 가정
#이진탐색
def binary_serch(A, key, low, high) :
    if (low <= high) :
        middle = (low + high)//2
        if key == A[middle] :
            return A[middle]
        
        elif key > A[middle] :
            return binary_serch(A, key, low, middle -1)
        elif key < A[middle] :
            return binary_serch(A, key, middle + 1, high)
        
    return -1

def binary_serch_iter(A, key, low, high) :
    while(low <= high) :
        middle = (low + high)//2
        if key == A[middle] :
            return A[middle]
        
        elif key > A[middle] :
            high = middle -1
        elif key < A[middle] :
            low = middle + 1

        return -1

def interpolation_serch(A, key, low, high) :
    while(low <= high):
        middle = int(low + (high - low) * ((key - A[low])/A[high] - A[low]))
        if key == A[middle] :
            return A[middle]
        
        elif key > A[middle] :
            high = middle -1
        elif key < A[middle] :
            low = middle + 1

        return -1