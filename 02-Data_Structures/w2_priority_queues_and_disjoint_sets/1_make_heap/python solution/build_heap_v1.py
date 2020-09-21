# python3


class BuildHeap:
    '''Converts an array of integers into a min-heap.

    A binary heap is a complete binary tree which catifies the heap ordering property, which is the value of each node is greater than or equal to the value of its parent, with the minimum-value element at the root.'''

    def __init__(self):
        self.swaps = []
        self.array = []

    @property
    def size(self):
        return len(self.array)

    def read_data(self):
        """Reads data from standard input."""
        n = int(input())
        self.array = [int(s) for s in input().split()]
        assert n == self.size

    def write_response(self):
        """Writes the response to standard output."""
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def l_child_index(self, index):
        """Returns the index of left child.
        If there's no left child, returns -1.
        """
        l_child_index = 2 * index + 1
        if l_child_index >= self.size:
            return -1
        return l_child_index

    def r_child_index(self, index):
        """Returns the index of right child.
        If there's no right child, returns -1.
        """
        r_child_index = 2 * index + 2
        if r_child_index >= self.size:
            return -1
        return r_child_index

    def sift_down(self, i):
        """Sifts i-th node down until both of its children have bigger value.
        At each step of swapping, indices of swapped nodes are appended
        to HeapBuilder.swaps attribute.
        """
        min_index = i
        l = self.l_child_index(i)
        r = self.r_child_index(i)

        if l != -1 and self.array[l] < self.array[min_index]:
            min_index = l

        if r != - 1 and self.array[r] < self.array[min_index]:
            min_index = r

        if i != min_index:
            self.swaps.append((i, min_index))
            self.array[i], self.array[min_index] = \
                self.array[min_index], self.array[i]
            self.sift_down(min_index)

    def generate_swaps(self):
        """Heapify procedure.
        It calls sift down procedure 'size // 2' times. It's enough to make
        the heap completed.
        """
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == "__main__":
    heap_builder = BuildHeap()
    heap_builder.solve()
