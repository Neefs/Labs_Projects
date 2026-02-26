import time


def time_function(func, args, n_trails=10):
    """This function tells how long it takes to run the function func accepts 1 arg.
        :param: func - parent function
        :param: args - function argument
        :param: n_trails - number of times ran

        :returns: min_time of function 
    """
    min_time = float('inf')
    for i in range(n_trails):
        start_time = time.time()
        func(args)
        end_time = time.time()
        min_time = (end_time - start_time) if (end_time - start_time) < min_time else min_time

        
    return min_time

    
def time_function_flexible(func, args, n_trails=10):
    """This function tells how long it takes to run the function func accepts multiple args packed in a tuple.
        :param: func - parent function
        :param: args - function argument
        :param: n_trails - number of times ran

        :returns: min_time of function 
    """
    min_time = float('inf')
    for i in range(n_trails):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        min_time = (end_time - start_time) if (end_time - start_time) < min_time else min_time
    return min_time


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))