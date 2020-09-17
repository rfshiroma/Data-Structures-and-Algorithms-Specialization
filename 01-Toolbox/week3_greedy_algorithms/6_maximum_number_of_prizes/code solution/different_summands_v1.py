# Uses python3
import sys

# Math concept: partitions
# https://en.wikipedia.org/wiki/Partition_%28number_theory%29
# Solution approach: Greedy algorithm

def optimal_summands(n):
    summands = []
    for i in range(1, n + 1):
        n -= i
        if n <= i:
            summands.append(n + i)
            break
        elif n == 0:
            summands.append(i)
            break
        else:
            summands.append(i)

    return summands

if __name__ == '__main__':
    n = 512
    print(optimal_summands(n))

    # input = sys.stdin.read()
    # n = int(input)
    # summands = optimal_summands(n)
    # print(len(summands))
    # for x in summands:
    #     print(x, end=' ')
