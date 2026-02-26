with open("smth.txt", "r") as f:
    entries = [l.split("\t") for l in f.readlines()]
    
print(entries)
d = [float(i[1]) for i in entries]
x = [float(i[2]) for i in entries]

print("D:\n" + str(d))
print("a:\n" + str(x))


l = [3, 10, 4, 6, 9]
