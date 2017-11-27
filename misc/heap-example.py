import heapq

def addToHeap(arr):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)
    return heap

if __name__ == '__main__':
    arr = [6, 301, 12, 11, 5, 1, 7]

    heap = []
    heap = addToHeap(arr)
    print(heap)
    print(heapq.heappop(heap))
    print(heap)
