# python3
#

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

"""
Build suffix tree of the string text given its suffix array suffix_array
and LCP array lcp_array. Return the tree as a mapping from a node ID
to the list of all outgoing edges of the corresponding node. The edges in the
list must be sorted in the ascending order by the first character of the edge label.
Root must have node ID = 0, and all other node IDs must be different
nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
    * node is the node ID of the ending node of the edge
    * start is the starting position (0-based) of the substring of text corresponding to the edge label
    * end is the first position (0-based) after the end of the substring corresponding to the edge label

For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
(corresponding to the root node), and it should be the first edge in the list (because
it has the smallest first character of all edges outgoing from the root).
"""
class SuffixTree:
    class Node:
        def __init__(self, node, depth, start, end):
            self.parent = node
            self.children = {}
            self.depth = depth  # string depth
            self.start = start
            self.end = end
            self.visited = False

    def __init__(self, s, order, LCP):
        self.s = s
        self.ele = ['$', 'A', 'C', 'G', 'T']
        self.order = order
        self.LCP = LCP
        self.root = self.Node(None, 0, -1, -1)

    def create_new_leaf(self, node, suffix):
        leaf = self.Node(node, len(self.s) - suffix, suffix + node.depth, len(self.s))
        node.children[self.s[leaf.start]] = leaf
        return leaf

    def break_edge(self, node, mid_start, offset):
        mid_char = self.s[mid_start]
        left_char = self.s[mid_start + offset]
        mid = self.Node(node, node.depth + offset, mid_start, mid_start + offset)
        mid.children[left_char] = node.children[mid_char]
        node.children[mid_char].parent = mid
        node.children[mid_char].start += offset
        node.children[mid_char] = mid
        return mid

    def st_from_sa(self):
        lcp_prev = 0
        cur = self.root
        for i in range(len(self.s)):
            suffix = self.order[i]
            while cur.depth > lcp.prev:
                cur = cur.parent
            if cur.depth == lcp_prev:
                cur = self.create_new_leaf(cur, suffix)
            else:
                # break edge and as a result got 3 nodes: mid, left(exist already), right(new suffix)
                mid_start = self.order[i - 1] + cur.depth       # the start of mid-node
                offset = lcp_prev - cur.depth                   # the number of characters of mid-node
                mid = self.break_edge(cur, mid_start, offset)
                cur = self.create_new_leaf(mid, suffix)
            if i < len(self.s) - 1:
                lcp_prev = self.LCP[i]

    def print_edges(self, cur):
        cur.visited = True
        if cur != self.root:
            print(cur.start, cur.end)
        for i in range(5):
            child = cur.children.get(self.ele[i], None)
            if child is not None and not child.visited:
                self.print_edges(child)


def main():
    text = input()
    suffix_array = list(map(int, input().split()))
    lcp = list(map(int, input().split()))
    print(text)
    suffix_tree = SuffixTree(text, suffix_array, lcp)
    suffix_tree.st_from_sa()


threading.Thread(target=main).start()


"""
Output the edges of the suffix tree in the required order.
Note that we use here the contract that the root of the tree
will have node ID = 0 and that each vector of outgoing edges
will be sorted by the first character of the corresponding edge label.

The following code avoids recursion to avoid stack overflow issues.
It uses two stacks to convert recursive function to a while loop.
This code is an equivalent of

    OutputEdges(tree, 0);

for the following _recursive_ function OutputEdges:

def OutputEdges(tree, node_id):
    edges = tree[node_id]
    for edge in edges:
        print("%d %d" % (edge[1], edge[2]))
        OutputEdges(tree, edge[0]);

"""
