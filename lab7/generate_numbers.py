import random

def generate_random(n):
    return [random.randint(1, 1000) for _ in range(n)]

def generate_sorted(n):
    return list(range(1, n+1))

def generate_reverse_sorted(n):
    return list(range(n, 0, -1))

def generate_almost_sorted(n):
    arr = list(range(1, n+1))
    # swap some
    for _ in range(n//10):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Choose type
# type = 'random'
type = 'sorted'
# type = 'reverse'
# type = 'almost'

n = 1000

if type == 'random':
    numbers = generate_random(n)
elif type == 'sorted':
    numbers = generate_sorted(n)
elif type == 'reverse':
    numbers = generate_reverse_sorted(n)
elif type == 'almost':
    numbers = generate_almost_sorted(n)

with open('numbers.txt', 'w') as f:
    f.write(' '.join(map(str, numbers)))

print(f"Generated {type} list of {n} numbers.")