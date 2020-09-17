# Uses python3
import sys
from collections import namedtuple


if __name__ == '__main__':
    segments = []
    n = int(input())
    for i in range(n):
        left, right = map(int, input().split())
        segments.append((left, right))

    sortedLeft = sorted(segments, key=lambda x: x[0])
    sortedRight = sorted(segments, key=lambda x: x[1])


    thrhold = sortedLeft[0][0] - 1
    listOfPoints = []
    for i in range(len(sortedRight)-1):
        left, right = sortedRight[i]
        if left > thrhold:
            listOfPoints.append(right)
            thrhold = right


    if listOfPoints[len(listOfPoints) - 1] < sortedRight[len(sortedRight) - 1][0]:
        if sortedRight:
            listOfPoints.append(sortedRight[len(sortedRight) - 1][0])
    print(len(listOfPoints))
    result = []
    for p in listOfPoints:
        result.append(p)

    print(*result)



# sweeping algorithm (segments intersects)
# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
#
