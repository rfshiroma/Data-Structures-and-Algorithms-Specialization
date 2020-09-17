# Uses python3

# More about it: https://www.sanfoundry.com/python-program-solve-fractional-knapsack-problem-using-greedy-algorithm/
# https://stackoverflow.com/questions/47744979/fractional-knapsack-algorithm-python-input-issues

import sys

def get_optimal_value(weight, value, capacity):
    '''
    An efficient solution is to use Greedy aprroach

    Returns maximum value of items and their fractional amounts.

    (max_value, fractions) is returnd where max_value is the maximum value of items with total wight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken of items i, where 0 <= i < total number of items.

    value[i] is the value of items and weight of item i for 0 <= i < n where n is the number of items

    capacity is the maximum weight
    '''
    # index = [0,2,3,...,n-1] for n items
    index = list(range(len(value)))

    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]

    # index is sorted according to value-to-wight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data
    value = [0]*n
    weight = [0]*n
    for i in range(n):
        value[i], weight[i] = map(int, input().split())
    opt_value = get_optimal_value(weight, value, capacity)
    print("{:.10f}".format(opt_value))
