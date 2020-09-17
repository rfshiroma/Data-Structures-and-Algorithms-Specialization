#Uses python3

import sys

def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

def largest_number(a):
    #write your code here
    res = []

    while a != []:
        max_digit = 0
        for digit in a:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        res.append(max_digit)
        a.remove(max_digit)

    return res

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    print(''.join([str(i) for i in largest_number(a)]))

    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]
    # print(largest_number(a))
