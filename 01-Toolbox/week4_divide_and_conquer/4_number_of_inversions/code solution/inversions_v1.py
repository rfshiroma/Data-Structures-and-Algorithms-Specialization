# Uses python3
import sys

# Algorithm approach: Divide-and-Conquer
# https://www.geeksforgeeks.org/counting-inversions/

# Function to Use Inversion Count
# def mergeSort(a, n):
#     # A temporary array (b) is created to store sorted array in merge function
#     b = [0] * n
#     return get_num_of_inv(a, b, 0, n - 1)

# Function will use mergeSort to count inversions
def get_num_of_inv(a, b, left, right):
    # A variable inv_count is used to store inversion counts in each recursive call
    num_of_inv = 0

    # Make a recursive call if and only if there is more than one element
    if left < right:

        # mid is calculated to divide the array into two subarrays
        # Floor division is a must in case of Python
        mid = (left + right) // 2

        # It will calculate inversion counts in the left subarray
        num_of_inv += get_num_of_inv(a, b, left, mid)

        # It will calculate inversion counts in right subarray
        num_of_inv += get_num_of_inv(a, b, mid + 1, right)

        # It will merge two subarrays in a sorted subarray
        num_of_inv += merge(a, b, left, mid, right)

    return num_of_inv


# Function will merge two subarrays in a single sorted subarray
def merge(a, b, left, mid, right):
    i = left       # Starting index of left subarray
    j = mid + 1    # Starting index of right subarray
    k = left       # Starting index to be sorted subarray
    num_of_inv = 0

    # Conditions are checked to make sure that i and j do not exceed subarray limits

    while i <= mid and j <= right:

        # there will be no inversion if arr[i] <= arr[j]
        if a[i] <= a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            # inversion will occur
            b[k] = a[j]
            num_of_inv += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining of left subarray into temporary array
    while i <= mid:
        b[k] = a[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        b[k] = a[j]
        k += 1
        j += 1

    # Copy the sorted subarray into original array
    for loop_var in range(left, right + 1):
        a[loop_var] = b[loop_var]

    return num_of_inv


if __name__ == '__main__':
    # TEST 2
    # a = [8, 4, 2, 1]
    # n = len(a)
    # b = n * [0]
    # result = get_num_of_inv(a, b, 0, len(a) - 1)
    # print("Number of inversions are: ", result)


    # TEST 1
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_num_of_inv(a, b, 0, len(a) - 1))
