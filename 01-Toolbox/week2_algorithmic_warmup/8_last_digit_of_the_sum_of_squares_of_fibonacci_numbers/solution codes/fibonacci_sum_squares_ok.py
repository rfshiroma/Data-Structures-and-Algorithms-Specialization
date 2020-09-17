# Uses python3

# More about it: https://www.geeksforgeeks.org/sum-of-squares-of-fibonacci-numbers/


from sys import stdin

def fibo_last_digit(n):
    '''
    An efficient approach which uses the concept of Pisano Period.
    runtime: O(log(n)).
    '''
    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(n - 1):
        prev, curr= curr, (prev + curr) % 10

    return curr % 10

def fibosum_squares(n):
    '''
    An efficient approach which uses the concept of Pisano Period.
    runtime: O(log(n)).
    '''
    vertical = fibo_last_digit(n % 60)
    horizontal = fibo_last_digit((n + 1) % 60)
    return (vertical*horizontal) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibosum_squares(n))
