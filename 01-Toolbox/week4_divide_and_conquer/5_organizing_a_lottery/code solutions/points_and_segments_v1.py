# Uses python3
import sys
from itertools import chain
# from collections import namedtuple

# https://www.geeksforgeeks.org/python-itertools-chain/

# Segment = namedtuple('Segment', 'start end')

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    left_start = zip(starts, ["l"] * len(starts), range(len(starts)))
    right_end = zip(ends, ["r"] * len(ends), range(len(ends)))
    point_tuple = zip(points, ["p"] * len(points), range(len(points)))
    listpoints = sorted(chain(left_start, right_end, point_tuple), key = lambda a: (a[0], a[1]))

    segments_num = 0
    for num, letter, index in listpoints:
        if letter == 'l': segments_num += 1
        elif letter == 'r': segments_num -= 1
        else: cnt[index] = segments_num

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    # TEST 1:
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    # TEST 2
    # starts = [0, 7]
    # ends = [5, 10]
    # points = [1, 6, 11]

    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
