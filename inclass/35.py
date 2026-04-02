import random

def selection_sort(L:list):
    for i in range(len(L)):
        _min = i
        
        for j in range(i, len(L)): # checks from current index (i) to end of the list for a value less than _min
            if L[j] < L[_min]:
                _min = j
                print(i, j)
        L[i], L[_min] = L[_min], L[i] #swaps the min with the current index
    return L

L = [4, 5, 1, 2, 3]

def insertion_sort(L:list):
    for i in range(len(L)):
        for j in range(len(L)-i, len(L)):
            if L[j-1] > L[j]: # checks if the items are out of order
                L[j], L[j-1] = L[j-1], L[j] #switch
    return L

    #Run in debug mode with breakpoints to see how it sorts




#print(selection_sort([int(random.random()*1000) for i in range(50)]))
print(insertion_sort(L.copy()))
print(selection_sort(L.copy()))