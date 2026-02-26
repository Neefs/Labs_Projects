l = [1, 2 , 4 , 5, 7, 6, 2, 3]
s = set(l)

print (l, s)
s.add(100)
s.add(56)
print (l, s)
l2 = list(sorted(s))
print(l2)

p = l

p.append("help")

print(p != l )

d = id([1, 2])
c = id([1, 2])



x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

y = x[10:]
z = x[:2]
print(y, z)


x = "2"
y = x
y+="3"
x+="3"
print(y is x, y==x)


x = ["mutable"]
y = x
y.pop(0)
print(y is x, y==x)

y = 'buzz'
 
def hello_goodbye(x):
  if len(x) > len(y):
    print('hello', end=' ')
 
  else:
    print('goodbye')
 
hello_goodbye('fizzbuzz')