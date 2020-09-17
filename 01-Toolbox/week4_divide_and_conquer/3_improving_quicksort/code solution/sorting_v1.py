import sys
import random

def partition3 (a, l, r):
    lt = l
    i = l
    gt = r
    pivot = a[l]

    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1

        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1

        else:
            i += 1

    return lt, gt


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    lt, gt = partition3(a, l, r)
    randomized_quick_sort(a, l, lt - 1)
    randomized_quick_sort(a, gt + 1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
