def partition(L, i, j):
    pivot = j -1
    j = pivot -1
    #Pivot all items between left and right
    while i < j :
        while L[i] < L[pivot]:
            i = i + 1
        while i<j and L[j] >= L[pivot]:
            j = j - 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    #Swap pivot and i
    if L[i]>= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

def qshelper(arr, left, right):
    if left < right:
        part = partition(arr, left, right)
        qshelper(arr, left, part-1)
        qshelper(arr, part+1, right)



def quicksort(arr):
    part = partition(arr, 0, len(arr))
    qshelper(arr, 0, part-1)
    qshelper(arr, part+1, len(arr))

l = [7, 4, 9, 6, 2]
print(l)
quicksort(l)
print(l)