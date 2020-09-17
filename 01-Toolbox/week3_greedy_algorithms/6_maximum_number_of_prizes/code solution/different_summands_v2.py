# Uses python3
import sys


def optimal_summands(n, l = 1):
    summands = []

    while n > 2*l:
        summands.append(l)
        n -= l
        l += 1
    summands.append(n)
    return summands

if __name__ == '__main__':
    # n = 512
    # print(optimal_summands(n))

    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n, l = 1)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
