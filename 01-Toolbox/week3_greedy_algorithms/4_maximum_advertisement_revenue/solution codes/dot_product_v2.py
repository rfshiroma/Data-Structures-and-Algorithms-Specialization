#Uses python3

import sys

def max_dot_product(a, b, n):
    sop = 0

    a.sort()
    b.sort()
    for i in range(n):
        sop += a[i] * b[i]
    return sop

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b, n))

# https://www.geeksforgeeks.org/maximum-sum-of-products-of-two-arrays/
