# Uses python3
import sys

# https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/


# Dynamic Programming implemaentaion
def get_change(coin, change, memo):
    if change == 0:
        return 0

    if change in memo:
        return memo[change]

    min_value = float("inf")
    for i in range(len(coins)):
        coin = coins[i]
        if coin > change:
            continue
        val = get_change(coins, change - coin, memo)
        min_value = min(min_value, val)

    min_value += 1

    memo[change] = min_value
    return min_value

if __name__ == '__main__':
    # TEST 1:
    change = int(sys.stdin.read())
    coins = [1, 3, 4]
    print(get_change(coins, change, dict()))
