# python3
#

import sys

def sort_characters(s):
    order = [0] * len(s)

    return order


def compute_char_classes(s, order):
    pass

    return char_class

def sort_doubled(s, L, old_order, old_class):
    pass

    return new_order

def update_classes(new_order, old_class, L):
    pass

    return new_class

def build_suffix_array(s):
    pass

    return order[1:]

def pattern_matching_with_suffix_arrayt(t, p, sa):
    pass

    return start, end

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
