#Uses python3
# https://www.tutorialspoint.com/largest-number-in-python

import sys
from functools import cmp_to_key


def IsGreaterOrEqual(x, y):
    if x + y < y + x:
        return 1
    elif x + y == y + x:
        return 0
    else:
        return -1

def largest_number(nums):
    #write your code here
    for i in range(len(nums)):
        nums [i] = str(nums[i])
    nums.sort(key=cmp_to_key(lambda x, y:IsGreaterOrEqual(x, y)))
    return "".join(nums).lstrip("0") or "0"


if __name__ == '__main__':
    # TEST 1
    # print(largest_number([3, 30, 5, 6, 8]))

    # TEST 2
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(''.join([str(i) for i in largest_number(nums)]))

    # TEST 3
    # input = sys.stdin.read()
    # data = input.split()
    # nums = data[1:]
    # print(largest_number(nums))
