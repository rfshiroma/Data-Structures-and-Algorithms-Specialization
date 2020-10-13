# python3
# Good job! (Max time used: 4.01/10.00, max memory used: 22822912/536870912.)

import sys

from collections import deque

class Suffix_Tree(object):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """

    class Node(object):
        def __init__(self, lab):
            self.lab = lab          # label on path leading to this node
            self.out = {}           # outgoing edges; maps characters to nodes

    def __init__(self, s):
        '''Make suffix tree without suffix links, from s in quadratic time and linear space.'''
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)  # trie for just longest suf

        # add the rest of the suffixes, from longest to shortest
        for i in range(1, len(s)):
            # start at root; we will walkdown as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    lab = child.lab
                    # walk along edge until we exhaust edge label or until we mismatch
                    k = j+1
                    # print('j', j, 'k', k, 'label', child.lab)
                    while k-j < len(lab) and s[k] == lab[k-j]:
                        k += 1
                    if k-j == len(lab):
                        cur = child # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        c_exist, c_new = lab[k-j], s[k]
                        # create "mid": new node bisecting edge
                        mid = self.Node(lab[:k-j])
                        mid.out[c_new] = self.Node(s[k:])
                        # original child becomes mid's child
                        child.lab = lab[k-j:]
                        mid.out[c_exist] = child
                        # original child's label is reduced
                        # print('j-', j, 'label', child.lab)
                        # mid becomes new chiild of original parent
                        cur.out[s[j]] = mid
                else:
                    # fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def _print(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            u = queue.popleft()
            if u != self.root:
                print(u.lab)
            for label, node in u.out.items():
                queue.append(node)


if __name__ == '__main__':
    # TEST 1
    text = input()
    stree = Suffix_Tree(text)
    stree._print()

    # TEST 2
    # text = sys.stdin.readline().strip()
    # result = build_suffix_tree(text)
    # print("\n".join(result))
