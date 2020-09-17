# Uses python3

# Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array table in bottom up manner.

# More info: https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

import sys

def get_change(coins, m, V):
    '''
    m: size of coins array (number of different coins)
    coins: possible value of the change coins

    table = [0 for i in range(V+1)]

    table [0] = 0

    for i in range (1, V+1):
        table[i] = sys.maxsize

    for i in range(1, V+1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]

if __name__ == '__main__':
    V = int(sys.stdin.read())
    coins = [1, 5, 10]
    m = len(coins)
    print(get_change(coins, m, V))
