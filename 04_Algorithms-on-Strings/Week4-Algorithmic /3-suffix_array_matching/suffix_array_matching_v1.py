# python3
#

import sys

# Task: Find all occurrences of a given collection of patterns in a string. In this problem, we will let you use the suffic array to solve the Multiple Pattern Matching Problem.

def sort_characters(s):
    order = [0] * len(s)
    count = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        count[char] += 1
    ele = ['$', 'A', 'C', 'G', 'T']
    for i in range(1, 5):
        count[ele[i]] += count[ele[i-1]]
    for j in range(len(s) - 1, -1, -1):
        c = s[j]
        count[c] -= 1
        order[count[c]] = j

    return order


def compute_char_classes(s, order):
    char_class = [0] * len(s)
    for i in range(1, len(s)):
        if s[order[i]] == s[order[i-1]]:
            char_class[order[i]] = char_class[order[i-1]]
        else:
            char_class[order[i]] = char_class[order[i-1]] + 1

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
