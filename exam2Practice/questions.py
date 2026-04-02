

s = "appleppppjpjpjpjpj"

def fun(s:str, letter:str) -> int:
    if not s:
        return 0
    if letter == s[0]:
        return 1 + fun(s[1:], letter)
    else:
        return fun(s[1:], letter)
    
print(fun(s, "p"))

l = [1, 1, 1, 1, 1, 1, 1]

#are all elements in list equal recursion
def in_list_rec(l:list):
    if len(l) <= 1:
        return True
    if l[0] != l[1]:
        return False
    return in_list_rec(l[1:]) #make sure to RETURN this not just run it


print(in_list_rec(l))

def get_binary(n:int):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return get_binary(n//2) + str(n%2)


print(get_binary(12))