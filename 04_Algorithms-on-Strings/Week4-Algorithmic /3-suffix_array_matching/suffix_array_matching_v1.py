# python3
#

import sys

def sort_characters(s):
    order = [0] * len(s)

    return order

if __name__ == '__main__':
    # TEST 1
    text = input()
    n_patterns = int(input())
    suffix_array = build_suffix_array(text+'$')
    result = [0] * len(text)
    for pattern in patterns:
        s, e = pattern_matching_with_suffix_array(text, pattern, suffix_array)
        if s <= e:
            for i in range(s, e + 1):
                pos = suffix_array[i]
                if result[pos] == 0:
                    print(pos, end=' ')
                result[pos] += 1

    # TEST 2
    # text = sys.stdin.readline().strip()
    # pattern_count = int(sys.stdin.readline().strip())
    # patterns = sys.stdin.readline().strip().split()
    # occs = find_occurrences(text, patterns)
    # print(" ".join(map(str, occs)))
