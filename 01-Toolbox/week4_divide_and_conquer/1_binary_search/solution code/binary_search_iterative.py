# Uses python3
import sys

# Iterative implementation of Binary Search:
def binary_search(arr, x):
    low, high = 0, len(arr) -1

    while low <= high:
        mid = (low + high) // 2
        
        # Check if x is present at mid
        if a[mid] == x:
            return mid

        # If x is greater, ignore left healf
        elif a[mid] < x:
            low = mid + 1

        # If x is smaller, ignore
        else:
            high = mid -1

    # Then the element was not found
    return -1

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
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
