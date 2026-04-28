
def _merge(a, b, L):
    print(a,b)
    i = 0 
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]: #compare
            L[i+j] = a[i] # we put a[i] into where it is supposed to be in the list
            i+=1 # move to next element and repeat
        else: # we know b[j] < a[i] so b[j] is next in list
            L[i+j] = b[j] # put it at current list element
            j +=1
    L[i+j:] = a[i:] + b[j:] # adds the remaining sorted values
    # list splicing LIST[start:stop:step]
    #starts at i+j:stops at end
    #starts at i: go to end ...

def mergeSort(L:list):
    n = len(L)
    if n<2:
        return L
    mid = n // 2
    a = L[mid:] # left of list
    b = L[:mid] # right
    mergeSort(a) # breaks lists down over and over again
    mergeSort(b)

    _merge(a,b,L) # merges the broken down lists up to the final sorted value

if __name__ == "__main__":
    L = [7, 6, 9, 3, 4, 5, 1]
    print(L)
    mergeSort(L)
    print(L)