# Uses python3

# More about it: https://www.geeksforgeeks.org/fractional-knapsack-problem/

import sys

class ItemValue:

    # Item Value Dataclass
    def __init__(self, weight, value, ind):
        self.weight = weight
        self.value = value
        self.ind = ind
        self.cost = value // weight

    def __lt__(self, other):
        return self.cost < other.cost


class FractionKnapSack:

    def get_optimal_value(weight, value, capacity):
        '''
        An efficient solution is to use Greedy aprroach
        Time complexity O(n log n)
        '''
        # function to get maximum value
        iVal = []
        for i in range(len(weight)):
            iVal.append(ItemValue(weight[i]), value[i], i)

        # sorting items by value
        iVal.sort(reverse=True)

        totalValue = 0
        for i in iVal:
            curr_Wt = int(i.weight)
            curr_Val = int(i.value)
            if capacity - curr_Wt >= 0:
                capacity -= curr_Wt
                totalValue += curr_Val
            else:
                fraction = capacity / curr_Wt
                totalValue += curr_Val * fraction
                capacity = int(capacity - (curr_Wt * fraction))
                break

        return totalValue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    value = data[2:(2 * n + 2):2]
    weight = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(weight, value, capacity)
    print("{:.10f}".format(opt_value))
