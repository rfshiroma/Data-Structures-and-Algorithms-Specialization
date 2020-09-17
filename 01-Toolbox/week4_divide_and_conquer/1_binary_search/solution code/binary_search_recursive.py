# Uses python3
import sys

# https://stackoverflow.com/questions/51248973/recursive-binary-search-python

# Recursive implementation of Binary Search:
def binary_search(arr, x, low, high):

    if low > high:
        return -1

    else:
        mid = (low + high) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only be found in left subarray
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid-1)

        # If element is larger than mid, then it can only be found in right subarray
        else:
            return binary_search(arr, x, mid+1, high)




# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    arr = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(arr, x, 0, len(arr) - 1), end = ' ')
