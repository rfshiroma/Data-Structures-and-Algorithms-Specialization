# Uses python3
import sys
import itertools

# More about it:
  # https://www.geeksforgeeks.org/partition-problem-dp-18/
  # https://en.wikipedia.org/wiki/Partition_problem

# Problem Statement:
# Partitioning problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

# Approach:
  # Two main steps to solve this problem:
   # 1. Calculate sum of the array. If sum is odd, there can not be two subsets with equals sum, so return false (which is 0) or true (which is 1).
   # 2. If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2.

# Returns true if arr[] can be partitioned in two subsets of equal sum, otherwise false
def findPartition(arr, n):
    '''
    Time complexity: O(sum * n)
    Auxiliary Space: O(sum * n)
    Note: This solution will not be feasible for arrays with big sum.
    '''
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return false

    table = [[ True for i in range(n+1)] for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(1, n+1):
        table[i][0] = True

    # initialize leftmost column except table[0][0], as 0
    for i in range(1, sum // 2 + 1):
        table[i][0] = False

    # fill the partition table in bottom-up manner
    for i in range(1, sum // 2 + 1):
        for j in range(1, n+1):
            table[i][j] = table[i][j-1]

            if i >= arr[j-1]:
                table[i][j] = (table[i][j] or table[i - arr[j-1]][j-1])

    return table[sum // 2][n]


if __name__ == '__main__':
    # TEST 2
    arr = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    # arr = [3, 1, 1, 2, 2, 1]
    # arr = [40]
    n = len(arr)
    if findPartition(arr, n) == True:
        print("Can be divided into two subsets of equal sum.")
    else:
        print("Can not be divided into two subsets of equal sum.")

    # TEST 1
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    # print(partition3(A))
