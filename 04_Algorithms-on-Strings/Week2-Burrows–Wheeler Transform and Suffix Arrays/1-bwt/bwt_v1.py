# python3
# Good job! (Max time used: 0.01/0.50, max memory used: 8978432/536870912.)

import sys

# Our goal is to further improve on the memory requirements of the suffix array. Construct the Burrows-Wheeler transform (BWT) of a string.
def BWT(text):
    matrix = [text]
    for i in range(1, len(text)):
        text = text[-1] + text[:-1]
        matrix.append(text)
    matrix.sort()
    bwt = ''
    for t in matrix:
        bwt += t[-1]
    return bwt

if __name__ == '__main__':
    text = input()
    print(BWT(text))
