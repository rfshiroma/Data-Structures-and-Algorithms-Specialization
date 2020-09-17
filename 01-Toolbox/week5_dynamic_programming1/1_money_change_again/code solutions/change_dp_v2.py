# Uses python3
import sys

# https://github.com/mission-peace/interview/blob/master/python/dynamic/coinchangingmincoins.py


def min_coins(coins, change):
    cols = change + 1
    rows = len(coins)
    T = [[0 if col == 0 else float("inf") for col in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(1, cols):
            if j < coins[i]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(T[i - 1][j], 1 + T[i][j - coins[i]])

    return T[rows - 1][cols - 1]


def print_coins(R, coins):
    start = len(R) - 1

    if R[start] == -1:
        print("No Solution Possible.")
        return

    print("Coins:",)
    while start != 0:
        coin = coins[R[start]]
        print("%d " % coin)
        start = start - coin


def min_coins2(coins, change):
    cols = change + 1
    T =[0 if idx == 0 else float("inf") for idx in range(cols)]
    R = [-1 for _ in range(change + 1)]

    for j in range(len(coins)):
        for i in range(1, cols):
            coin = coins[j]
            if i >= coins[j]:
                if T[i] > 1 + T[i - coin]:
                    T[i] = 1 + T[i - coin]
                    R[i] = j

    print_coins(R, coins)
    return T[cols - 1]


def min_coins_top_down(coins, change, memo):
    if change == 0:
        return 0

    if change in memo:
        return memo[change]

    min_value = float("inf")
    for i in range(len(coins)):
        coin = coins[i]
        if coin > change:
            continue
        val = min_coins_top_down(coins, change - coin, memo)
        min_value = min(min_value, val)

    min_value += 1

    memo[change] = min_value
    return min_value

if __name__ == '__main__':
    # TEST 1:
    # m = int(sys.stdin.read())
    # print(get_change(m))

    # TEST 2:
    coins = [1, 3, 4]
    change = 34

    print("Approach 1. 2D array: ", min_coins(coins, change))
    print("Approach 1. 1D array:  ", min_coins2(coins, change))
    print("Topdown DP: ", min_coins_top_down(coins, change, dict()))
