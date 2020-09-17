# Uses python3
import sys

def optimal_summands(n):
    if n == 1:
        return "1"

    summands = []
    for i in range(1, n):
        if n > 2 * i:
            summands.append(i)
            n -= i
        else:
            summands.append(n)
            break

    return summands

if __name__ == '__main__':
    # n = 1
    # print(optimal_summands(n))

    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
