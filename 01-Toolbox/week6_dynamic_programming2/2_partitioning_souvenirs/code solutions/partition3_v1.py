# Uses python3
import sys
import itertools
import numpy as np

def partition3(W, n, items):
    ''' Finds if number of partitions having capacity W is >= 3
    (int, int, list) --> (int)
    '''
    count = 0

    # initializes the table
    table = np.zeros((W+1, n+1))

    # fill the partition table in bottom-up manner
    for i in range(1, W+1):
        for j in range(1, n+1):
            table[i][j] = table[i][j-1]
            if i >= items[j-1]:
                temp = table[i - items[j-1]][j-1] + items[j-1]
                if temp > table[i][j]:
                    table[i][j] = temp
            if table[i][j] == W: count += 1

    if count < 3: print("0")
    else: print("1")



if __name__ == '__main__':
    # TEST 2
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n < 3:
        print("0")
    elif total_weight % 3 != 0:
        print("0")
    else:
        partition3(total_weight // 3, n, item_weights)

    # TEST 1
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    # print(partition3(A))
