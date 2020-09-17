#Uses python3
import sys
import math

# https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
# https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/?ref=rp
# http://people.csail.mit.edu/indyk/6.838-old/handouts/lec17.pdf

'''
Compute the closest pair of points in the array.

Algorithm approach: Divide-and-Conquer
Complexity: O(n log(n))
'''


# A class to represent a Point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A useful function to find the distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

def stripClosest(strip, size, d):
    '''
    An utility function to find the distance between the closest points of strip of given size. All points in strip[] are sorted according to y coordinate. They all have an upper bound on minimum distance as d.

    Note that this method seems to be a O(nˆ2) method, but it's a O(n) method as the inner loop runs at most 7 times.
    '''
    # Initialize the minimum distance as d
    min_val = d

    strip.sort(key = lambda point: point.y)

    # Pick all points one by one and try the next points until the difference between y coordinates is smaller than d. This is a proven fact that this loop runs at most 7 times.
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val


def closestUtil(P, n):
    '''
    A recursive function to find the smallest distance. The array P contains all points sorted according to x coordinate.
    '''
    # If there are 2 or 3 points, then use brute force
    if n <= 3:
        return bruteForce(P, n)

    # Find the middle point
    mid = n // 2
    midPoint = P[mid]

    # Consider a vertical line passing through the middle point to calculate the smallest distance dl (on left) from the middle point and dr (on right side)
    dl = closestUtil(P[:mid], mid)
    dr = closestUtil(P[mid:], n - mid)

    # Find the smallest of two distances
    d = min(dl, dr)

    # Build an array strip[] taht contains points close (closer than d) to the line passing through the middle point
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])

    # Find the closest points in strip. Return the minimum of d and closest distance is strip[]
    return min(d, stripClosest(strip, len(strip), d))


def bruteForce(P, n):
    '''
    A Brute Force method to return the smallest distance between two points in P[] of size n.
    '''
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val


def minimum_distance(P, n):
    '''
    The main function that computes the smallest distance. This method mainly uses closestUtil()
    '''
    P.sort(key = lambda point: point.x)

    # Use recursive function closestUtil() to find the smallest distance
    return closestUtil(P, n)


if __name__ == '__main__':
    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    # print("{0:.9f}".format(minimum_distance(x, y)))

    # TEST 2

    # P = [Point(4,4), Point(-2, -2), Point(-3, -4), Point(7, 7)]
    # n = len(P)
    # print("The smallest distance is", minimum_distance(P, n))
