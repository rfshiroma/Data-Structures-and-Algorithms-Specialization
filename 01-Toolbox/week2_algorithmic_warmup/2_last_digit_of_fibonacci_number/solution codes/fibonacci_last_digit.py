# Uses python3
import sys

'''
Optimized version to find last digit of nth Fibonacci number. It computes the units digit of first 60 Fibonacci numbers and store it in an array (list) and use that array values for further calculations. The series of final digits repeats with a cycle length of 60.
https://www.geeksforgeeks.org/program-find-last-digit-nth-fibonnaci-number/
'''

def fibo(f, n):
    '''Finds nth Fibonacci number'''
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2]) % 10

    return f

def fibo_LastDigit(n):
    f = [0] * 61
    f = fibo(f, 60)
    return f[n % 60]

if __name__ == '__main__':
    n = int(input())
    print(fibo_LastDigit(n))
