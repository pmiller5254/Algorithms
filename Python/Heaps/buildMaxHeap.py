import math

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def heapify(self, arr: list) -> None:
        """Build a max heap from an array in-place."""
        self.heap = arr
        n = len(arr)
        # Start from the last non-leaf node and heapify all nodes in reverse order
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
    
    def _sift_down(self, idx: int) -> None:
        """Maintain the max heap property by sifting down the element at index idx."""
        n = len(self.heap)
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        # Check if left child exists and is greater than current largest
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
            
        # Check if right child exists and is greater than current largest
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
            
        # If largest is not the current node, swap and continue sifting down
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._sift_down(largest)
    
    def _sift_up(self, idx: int) -> None:
        """Maintain the max heap property by sifting up the element at index idx."""
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._sift_up(parent)
    
    def insert(self, val: int) -> None:
        """Insert a new value into the heap."""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    
    def extract_max(self) -> int:
        """Remove and return the maximum value from the heap."""
        if not self.heap:
            raise IndexError("Heap is empty")
            
        max_val = self.heap[0]
        last_val = self.heap.pop()
        
        if self.heap:  # If heap is not empty after popping
            self.heap[0] = last_val
            self._sift_down(0)
            
        return max_val
    
    def get_max(self) -> int:
        """Return the maximum value without removing it."""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

# Test the MaxHeap implementation
if __name__ == "__main__":
    # Test case 1: Building heap from array
    heap1 = MaxHeap()
    test_array = [4, 10, 3, 5, 1]
    heap1.heapify(test_array)
    print("Heap after heapify:", heap1.heap)  # Should show a valid max heap
    
    # Test case 2: Insert operations
    heap2 = MaxHeap()
    for num in [4, 10, 3, 5, 1]:
        heap2.insert(num)
    print("Heap after insertions:", heap2.heap)  # Should show same heap as heap1
    
    # Test case 3: Extract max operations
    print("\nExtracting max values:")
    while heap1.heap:
        print(heap1.extract_max(), end=" ")  # Should print: 10 5 4 3 1


