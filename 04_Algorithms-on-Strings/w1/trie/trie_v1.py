#Uses python3
# Good job! (Max time used: 0.04/2.00, max memory used: 67592192/536870912.)


import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

# tree = { node1: { label1: c1, label2: c2, ...}, node2, ...}
def build_trie(patterns):
    tree = {}
    new_node = 0
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if tree.__contains__(current_node) and tree[current_node].__contains__(current_symbol):
                current_node = tree[current_node].get(current_symbol)
            else:
                new_node = new_node + 1
                if not tree.__contains__(current_node):
                    tree[current_node] = {}
                    tree[current_node][current_symbol] = new_node
                else:
                    tree[current_node][current_symbol] = new_node
                current_node = new_node
    return tree


if __name__ == '__main__':
    n_patterns = int(input())
    patterns = list(input() for _ in range(n_patterns))
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

    # TEST 2
    # patterns = sys.stdin.read().split()[1:]
    # tree = build_trie(patterns)
    # for node in tree:
    #     for c in tree[node]:
    #         print("{}->{}:{}".format(node, tree[node][c], c))
