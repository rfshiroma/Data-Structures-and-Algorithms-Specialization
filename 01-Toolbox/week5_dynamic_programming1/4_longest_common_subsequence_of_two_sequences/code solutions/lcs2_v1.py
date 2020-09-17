#Uses python3

import sys

# Dynamic Programming (dp) implementation of Longest Common Sequence (LCS) problem
def lcs2(s1, s2):
    #Find the length of the strings
    m = len(s1)
    n = len(s2)

    # Declaring the array for storing the dp values
    L = [[None] * (n+1) for i in range(m+1)]

    # Following steps build T[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of s1[0...i-1] and s2[0....j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # T[m][n] contains the length of LCS of s1[0...i-1] and s2[0...j-1]
    return L[m][n]

if __name__ == '__main__':
    # TEST 2
    n1, s1, n2, s2 = int(input()), input(), int(input()), input()
    s1, s2 = [int(i) for i in s1.split()], [int(i) for i in s2.split()]
    print(lcs2(s1, s2))


    # TEST 1
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    #
    # n = data[0]
    # data = data[1:]
    # a = data[:n]
    #
    # data = data[n:]
    # m = data[0]
    # data = data[1:]
    # b = data[:m]
    #
    # print(lcs2(a, b))
