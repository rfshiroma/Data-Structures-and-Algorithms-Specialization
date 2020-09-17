def calc_fib(n):
    '''
    Create a list of fibonacci numbers up to the number you want.
    '''
    if (n <= 1):
        return n

    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[n]

n = int(input())
print(calc_fib(n))


'''VERY EFFICIENT FOR LARGE NUMBERS
Good job! (Max time used: 0.01/5.00, max memory used: 9142272/536870912.)
'''
