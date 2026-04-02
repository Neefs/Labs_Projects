"""mplement the insertionsort algorithm. Your algorithm should start on the left-hand side of the list, 
so that at the end of k loops, the first k items in the list are sorted relative to each other.
Your implementation should also be adaptive with respect to the number of swaps 
(Do not swap if the element is already in its correct position).  
Experimental: If you'd like, you can run your code in clientide.com
"""

def insertionsort(L):
    """"""
    n = len(L)
    for i in range(n):
        j = n-i-1
        while j < n-1 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j+=1
    return L

def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j+1], L[j] = L[j], L[j+1]
    return L



print(bubble_sort([2, 8, 5, 3, 9, 4]))
assert insertionsort([2, 8, 5, 3, 9, 4]) == [2, 3, 4, 5, 8, 9]