import heapq
import random


class MinHeap:
    def __init__(self):
        self.minheap = list()
        heapq.heapify(self.minheap)

    def insert(self, data):  # O(logN)
        heapq.heappush(self.minheap, data)

    def pop_min(self):  # O(logN)
        max_one = heapq.heappop(self.minheap)
        return max_one

    def peek_min(self):
        return self.minheap[0] if self.minheap else None


class MaxHeap:
    def __init__(self):
        self.maxheap = list()

    def insert(self, data):  # O(logN)
        heapq.heappush(self.maxheap, data)
        heapq._heapify_max(self.maxheap)  # O(n)

    def pop_max(self):  # O(logN)
        max_one = heapq.heappop(self.maxheap)
        heapq._heapify_max(self.maxheap)  # O(n)
        return max_one

    def peek_max(self):
        return self.maxheap[0] if self.maxheap else None


if __name__ == "__main__":
    insert_order = random.sample(range(1, 20), 10)
    print("Insert Order:", insert_order)

    max_heap = MaxHeap()
    for item in insert_order:
        max_heap.insert(item)

    while max_heap.peek_max():
        print(max_heap.pop_max())
