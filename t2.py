def fewest_coins(amt, coins, solved=dict()):
    """Returns the minimum amount of coins needed to make amt"""
    # Base case: we've solved this problem already
    if amt in solved: return solved.get(amt)
 
    # Base case: we can make this amount with 1 coin
    elif amt in coins:
        solved.setdefault(amt, 1)
        return solved.get(amt)
 
    solved.setdefault(amt, float('inf'))
 
    # Explore every coin from here, find minimum
    for coin in coins:
        if coin < amt:
            n_branch = 1 + fewest_coins(amt-coin, coins, solved)
            
            if n_branch < solved.get(amt):
                solved.pop(amt)
                solved.setdefault(amt, n_branch)
 
    return solved.get(amt)
 
L1 = list((1, 5, 10, 25))
L2 = list((1, 5, 10, 20, 25))
 
n1 = fewest_coins(40, L1)
n2 = fewest_coins(40, L2)
print(n1, n2)