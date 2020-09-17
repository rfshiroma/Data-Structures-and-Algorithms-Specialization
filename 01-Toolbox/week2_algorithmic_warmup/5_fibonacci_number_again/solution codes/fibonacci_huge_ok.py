# Uses python3
import sys

def fibo_huge(n, m):
    '''
    Given two integers n and m, return the remainder of F(n) when divided by m. An efficient approach which uses the concept of Pisano Period.
    Output: F(n) % m
    '''
    if n <= 1:
        return n

    arr = [0,1]
    previousMod = 0
    currentMod = 1

    for i in range(n-1):
        tempMod = previousMod
        previousMod = currentMod % m
        currentMod = (tempMod + currentMod) % m
        arr.append(currentMod)
        if currentMod == 1 and previousMod == 0:
            index = (n % (i + 1))
            return arr[index]

    return currentMod

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibo_huge(n, m))
