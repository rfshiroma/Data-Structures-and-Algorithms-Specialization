# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refill, curr_refill, limit = 0, 0, tank
    while limit < distance:
        if curr_refill >= n or stops[curr_refill] > limit:
            return -1
        while curr_refill < n-1 and stops[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1
        limit = stops[curr_refill] + tank
        curr_refill += 1
    return num_refill

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))

    # test 2:
    # print(compute_min_refills(950, 400, 4, [200, 375, 550, 750]))
    # print(compute_min_refills(10, 3, 4, [1, 2, 5, 9]))


# map() -> https://www.geeksforgeeks.org/python-map-function/
# https://stackoverflow.com/questions/61570575/car-fueling-problem-by-greedy-alogorithm-getting-list-index-out-of-range
# https://www.geeksforgeeks.org/number-of-refills-to-complete-the-journey-of-n-km/
