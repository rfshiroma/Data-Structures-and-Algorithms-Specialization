# Uses python3

# More about it: https://stackoverflow.com/questions/42944323/i-am-trying-to-find-the-last-digit-of-partial-sum-of-fibonacci-series

import sys

def fibo_partial_sum(m, n):
    '''
    Compute the last digit of sum of numbers in the given range in the Fibonacci series.

    m: non-negative integer
    n: non-negative integer
    '''
    if m > n:
        return

    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i-1] + a[i-2])

    m = m % 60
    n = n % 60

    if n < m:
        n += 60

    sum_ = 0
    for j in range(m, n+1):
        sum_ += a[j % 60]

    return sum_ % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    m, n = map(int, input.split())
    print(fibo_partial_sum(m, n))
