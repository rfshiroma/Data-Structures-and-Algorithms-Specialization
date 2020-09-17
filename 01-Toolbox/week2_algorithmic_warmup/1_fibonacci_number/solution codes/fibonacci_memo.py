def calc_fib(n):
    ''' Memo version of fibonacci. It keeps track of values that have already been computed by storing them in a dictionary.
    '''
    known = {0:0, 1:1}
    if n in known:
        return known[n]

    res = calc_fib(n-1) + calc_fib(n-2)
    known[n] = res
    return res

n = int(input())
print(calc_fib(n))


'''NOT EFFICIENT FOR LARGE NUMEBRS
Failed case #36/46: time limit exceeded
Input:
35

Your output:
9227465

stderr:
(Time used: 7.12/5.00, memory used: 9142272/536870912.)
'''
