# python3

# Approach: Elimination based
  # In every iteration, the innermost bracket get eliminated (replaced with empty string). If we end up with an empty string, our initial one was balanced; otherwise, not.

# About namedtuple:
  # https://www.geeksforgeeks.org/namedtuple-in-python/

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    brackets = ['()', '{}', '[]']
    while any (x in text for x in brackets):
        for br in brackets:
            text = text.replace(br, '')

    return not text


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    # TEST 2
    string = "{[]{()}}"
    print(string, "-", "Sucess" if find_mismatch(string) else "Unbalanced")

    # TEST 1
    # main()
