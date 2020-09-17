# Uses python3
import sys

def gcd(a, b):
    '''
    Euclidean Algorithm - This method will return an absolute/positive integer value after calculating the GCD of given paramenters a and b.

    a: Non-negative integer
    b: Non-negative integer
    '''
    while b != 0:
        (a, b) = (b, a % b)
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
