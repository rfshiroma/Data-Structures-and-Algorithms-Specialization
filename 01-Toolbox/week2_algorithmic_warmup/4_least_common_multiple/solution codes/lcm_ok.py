# Uses python3
import sys

'''We can make it more efficient by using the fact that the product of two numbers is equal to the product of the least common multiple and greatest common divisor of those two numbers.'''
  # Number1 * Number2 = GCD * LCM

def gcd(a, b):
    '''
    Euclidean Algorithm - This method will return an absolute/positive integer value after calculating the GCD of given paramenters a and b.

    a: Non-negative integer
    b: Non-negative integer
    '''
    while b != 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    '''The least common multiple (L.C.M.) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.'''
    lcm = (a*b)//gcd(a, b)
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
