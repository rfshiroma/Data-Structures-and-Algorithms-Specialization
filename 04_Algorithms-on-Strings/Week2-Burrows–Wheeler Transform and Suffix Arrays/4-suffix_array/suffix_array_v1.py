# python3
# Good job! (Max time used: 0.05/1.00, max memory used: 57425920/536870912.)

import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    suffix = []
    for i in range(len(text)):
        suffix.append((text[i:], i)) # (suffix, starting position)
    suffix.sort()
    result = []
    for e in suffix:
        result.append(e[1])
    return result


if __name__ == '__main__':
    # TEST 1
    text = input()
    suffix_array = build_suffix_array(text)
    for e in suffix_array:
        print(e, end= ' ')

    # TEST 2
    # text = sys.stdin.readline().strip()
    # print(" ".join(map(str, build_suffix_array(text))))
