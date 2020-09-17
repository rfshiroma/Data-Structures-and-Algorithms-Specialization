#Uses python3

import sys
from functools import cmp_to_key

class Solution(object):
    def IsGreaterOrEqual(self, x, y):
        if x + y < y + x:
            return 1
        elif x + y == y + x:
            return 0
        else:
            return -1

    def largest_number(self, nums):
        #write your code here
        for i in range(len(nums)):
            nums [i] = str(nums[i])
        nums.sort(key=cmp_to_key(lambda x, y:self.IsGreaterOrEqual(x, y)))
        return "".join(nums).lstrip("0") or "0"


if __name__ == '__main__':
    ob1 = Solution()
    print(ob1.largest_number([3, 30, 5, 6, 8]))

    # n = int(input())
    # nums = [int(i) for i in input().split()]
    # print(''.join([str(i) for i in largest_number(nums)]))

    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]
    # print(largest_number(a))
