# python3
# Good job! (Max time used: 4.85/24.00, max memory used: 188030976/536870912.)

import sys


def PreprocessBWT(s):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position
        of this character in the sorted array of
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
    """
    freq = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        freq[char] += 1
    ele = ['$', 'A', 'C', 'G', 'T']
    first_occur = {'$': 0}
    for i in range(1, 5):
        first_occur[ele[i]] = first_occur[ele[i-1]] + freq[ele[i-1]]
    count = {}
    for e in ele:
        count[e] = [0] * (len(s) + 1)
    for i in range(len(s)):
        temp = {s[i]: 1}
        for e in ele:
            count[e][i+1] = count[e][i] + temp.get(e, 0)
    return first_occur, count


def BWMatching(s, p, first_occur, count):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.
    """
    top = 0
    bottom = len(s) - 1
    while top <= bottom:
        if p:
            symbol = p[-1]
            p = p[:-1]
            top = first_occur[symbol] + count[symbol][top]
            bottom = first_occur[symbol] + count[symbol][bottom + 1] - 1
        else:
            return bottom - top + 1
    return 0  # pattern not in string



if __name__ == '__main__':
    # TEST 1
    bwt = input()
    n_patterns = int(input())
    patterns = list(input().split())
    first_occur, count = PreprocessBWT(bwt)
    for pattern in patterns:
        result = BWMatching(bwt, pattern, first_occur, count)
        print(result, end=' ')

    # TEST 2
    # bwt = sys.stdin.readline().strip()
    # pattern_count = int(sys.stdin.readline().strip())
    # patterns = sys.stdin.readline().strip().split()
    # # Preprocess the BWT once to get starts and occ_count_before.
    # # For each pattern, we will then use these precomputed values and
    # # spend only O(|pattern|) to find all occurrences of the pattern
    # # in the text instead of O(|pattern| + |text|).
    # starts, occ_counts_before = PreprocessBWT(bwt)
    # occurrence_counts = []
    # for pattern in patterns:
        # occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    # print(' '.join(map(str, occurrence_counts)))
