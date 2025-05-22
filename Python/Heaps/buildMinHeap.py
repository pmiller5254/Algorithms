class MinHeap:
    def __init__(self):
        # Initialize an empty min heap.
        # The heap will be implemented using a list where:
        # - For any node at index i:
        #   - Left child is at index 2i + 1
        #   - Right child is at index 2i + 2
        #   - Parent is at index (i-1) // 2
        self.heap = []
    
    def parent(self, i):
        # Returns the index of the parent of the node at index i.
        return (i - 1) // 2

    def left_child(self, i):
        # Returns the index of the left child of the node at index i.
        return 2 * i + 1
    
    def right_child(self, i):
        # Returns the index of the right child of the node at index i.
        return 2 * i + 2
    
    def swap(self, i, j):
        # Swaps the elements at indices i and j in the heap.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        # Maintains the min heap property by bubbling up the element at index i
        # if it's smaller than its parent.
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        # Maintains the min heap property by bubbling down the element at index i
        # if it's larger than its children.
        while 2 * i + 1 < len(self.heap):  # Check if left child exists
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[i] <= self.heap[smallest]:
                break
            self.swap(i, smallest)
            i = smallest
    
    def insert(self, key):
        # Inserts a new key into the min heap.
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        # Removes and returns the minimum element from the heap.
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_val
    
    def get_min(self):
        # Returns the minimum element without removing it.
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def size(self):
        # Returns the number of elements in the heap.
        return len(self.heap)
    
    def is_empty(self):
        # Returns True if the heap is empty, False otherwise.
        return len(self.heap) == 0
    
    def build_heap(self, arr):
        # Builds a min heap from an array.
        self.heap = arr
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heap_sort(self, arr):
        # Sorts an array using heap sort.
        self.build_heap(arr)
        sorted_arr = []
        for _ in range(len(arr)):
            sorted_arr.append(self.extract_min())