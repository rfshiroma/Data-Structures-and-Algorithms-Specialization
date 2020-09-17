# Uses python3
# More about the solution:
 #1 https://www.geeksforgeeks.org/last-digit-of-sum-of-numbers-in-the-given-range-in-the-fibonacci-series/
 # 2 https://stackoverflow.com/questions/54008328/last-digit-of-the-sum-of-fibonacci-numbers
import sys

def fibo_sum(n):
    '''
    An efficient approach which uses the concept of Pisano Period.
    runtime: O(log(n))
    '''
    pisano = 60

    if n < 2: return n

    n %= pisano

    fib_arr = [1,1]
    for i in range(n):
        fib_arr.append(fib_arr[-1] + fib_arr[-2] % 10)

    return (fib_arr[-1] -1) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibo_sum(n))
