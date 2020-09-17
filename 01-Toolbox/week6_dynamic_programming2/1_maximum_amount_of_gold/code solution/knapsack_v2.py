# Uses python3
import sys
import numpy as np

# https://www.codesdope.com/course/algorithms-knapsack-problem/


# Discrete Knapsack problem without repetition
def maxGold(W, n, items):
    """ Outputs the maximum weight of gold that fits in knapsack of capacity W
    (int, int, list) -> (int, 2D-array) """

    table = np.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            # if item i is not part of optimal knapsack
            table[i][j] = table[i][j-1]
            if items[j-1] <= i:
                # if item i is part of optimal knapsack
                temp = table[i-items[j-1]][j-1] + items[j-1]
                # max(i in knapsack, i not in knapsack)
                if temp > table[i][j]:
                    table[i][j] = temp

    return (int(table[W][n]))



if __name__ == '__main__':
    W, n               = [int(i) for i in input().split()]
    item_weights       = [int(i) for i in input().split()]
    max_weight = maxGold(W, n, item_weights)
    print(f"{max_weight}")


    # TEST 1:
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    # print(optimal_weight(W, w))
