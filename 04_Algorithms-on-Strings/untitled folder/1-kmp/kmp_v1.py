# python3
# Good job! (Max time used: 1.04/4.00, max memory used: 92798976/536870912.)

# import sys

def PrefixFunction(p):
    s = [0] * len(p)
    border = 0
    for i in range(1, len(p)):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

# knuth-Morris-Pratt (KMP) Algorithm
def find_pattern(p, t):
    s = p + '$' + t
    pre_func = PrefixFunction(s)
    result = []
    for i in range(len(p) + 1, len(s)):
        if pre_func[i] == len(p):
            result.append(i - 2 * len(p))
    return result


if __name__ == '__main__':
    # TEST 1
    pattern = input()
    text = input()
    positions = find_pattern(pattern, text)
    for pos in positions:
        print(pos, end=' ')

    # TEST 2
    # pattern = sys.stdin.readline().strip()
    # text = sys.stdin.readline().strip()
    # result = find_pattern(pattern, text)
    # print(" ".join(map(str, result)))
