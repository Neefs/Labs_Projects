import random
import time

def is_sorted(l:list):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]: 
            return False
    return True

def simple_bogo(l:list):
    attempts = 0
    while not is_sorted(l):
        random.shuffle(l)
        attempts += 1
    return l, attempts

def simple_bogo_rec(l:list):
    if is_sorted(l):
        return l, 1
    random.shuffle(l)
    sorted_list, attempts = simple_bogo_rec(l)
    return sorted_list, attempts + 1

l = list([i for i in range(6, 0, -1)])
print("Running simple_bogo with l: ", l)

start_time = time.time()
s = simple_bogo_rec(l)
end_time = time.time()
print(s)
print("Time taken: ", end_time - start_time)
