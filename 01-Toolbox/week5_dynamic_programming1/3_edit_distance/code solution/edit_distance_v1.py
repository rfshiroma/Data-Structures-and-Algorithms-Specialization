# Uses python3

# A dynamic Programming based python program for edit distance problem
def edit_distance(str1, str2):
    '''
    Given two strings str1 and str2 and (insert, delete and substitution of symbols), find minimum number of edits(operations) required to convert str1 into str2.

    '''
    rows = len(str2) + 1
    cols = len(str1) + 1
    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        T[0][j] = j

    for i in range(rows):
        T[i][0] = i

    for i in range(1, rows):
        for j in range(1, cols):
            if str2[i - 1] == str1[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j - 1], T[i - 1][j], T[i][j - 1])

    print(T[rows - 1][cols - 1])
    print_edits(T, str1, str2)
    # return T[rows - 1][cols - 1]


def print_edits(T, str1, str2):
    i = len(T) - 1
    j = len(T[0]) - 1
    while True:
        if i == 0 or j == 0:
            break
        if str2[i - 1] == str1[j - 1]:
            i -= 1
            j -= 1
        elif T[i][j] == T[i - 1][j] + 1:
            print("Delete %s in string2." % str2[i - 1])
            i -= 1
        elif T[i][j] == T[i][j - 1] + 1:
            print("Delete %s in string1." % str1[j - 1])
            j -= 1
        elif T[i][j] == T[i - 1][j - 1] + 1:
            print("Replace %s in string1 to %s in string2." % (str1[j - 1], str2[i - 1]))
            i -= 1
            j -= 1


if __name__ == '__main__':
    # str1 = "azced"
    # str2 = "abcdef"
    edit_distance(input(), input())
