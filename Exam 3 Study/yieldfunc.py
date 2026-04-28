
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def give_l():
    for item in l:
        yield item**2+2
    
r = give_l()
print(next(r))

print(give_l())

for g in give_l():
    print(g)

print(list(give_l()))