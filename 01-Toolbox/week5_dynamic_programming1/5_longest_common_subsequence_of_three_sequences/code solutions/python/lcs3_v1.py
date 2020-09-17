# Uses python3
# https://www.geeksforgeeks.org/lcs-longest-common-subsequence-three-strings/

import sys

# Python program to find LCS of three strings
# Returns length of LCS for s1[0... n1-1], s2[0... n2-1], s3[0... n3-1]

def lcs3(a, b, c):
    ''' Finds the length of the longest common subsequence of three strings
    (str, str, str, int, int, int) --> (int, 3D-array) '''

    m = len(a)
    n = len(b)
    o = len(c)

    # Initializing the table
    L = [[[0 for i in range(o + 1)] for j in range(n + 1)] for k in range(m + 1)]

    # Following steps build L[m+1][n+1][o+1] in bottom-up approach
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0

                elif a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1

                elif a[i-1] != b[j-1] and a[i-1] != c[k-1]:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1])

    # L[m][n][o] contains length of LCS for a[0... m-1] and b[0... n-1] and c[0... o-1]
    return L[m][n][o]

if __name__ == '__main__':
    # TEST 3:
    m, a, n, b, o, c = int(input()), input(), int(input()), input(), int(input()), input()

    # If inputs for s1, s2, s3 are numbers uncomment below line.
    a, b, c = [int(i) for i in a.split()], [int(i) for i in b.split()], [int(i) for i in c.split()]

    print(LCS3(a, b, c))

    # TEST 2:
    # a = 'AGGT12'
    # b = '12TXAYB'
    # c = '12XBA'
    #
    #
    # print(lcs3(a, b, c))

    # TEST 1:
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # an = data[0]
    # data = data[1:]
    # a = data[:an]
    # data = data[an:]
    # bn = data[0]
    # data = data[1:]
    # b = data[:bn]
    # data = data[bn:]
    # cn = data[0]
    # data = data[1:]
    # c = data[:cn]
    # print(lcs3(a, b, c))
