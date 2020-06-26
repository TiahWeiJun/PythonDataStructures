#HeapSort involves iterating through an array to place the elements in a min heap, then we iterate over the length of the array and replace the smallest elements from left to right
#Time complexity is O(nlogn) for best and worst case scenario
#Unstable sorting algorithm

import sys

sys.path.insert(2, '/Users/Admin/Documents/Projects/DSA/Heaps')

from MinHeap import MinHeap

def heapSort(arr):
    heap = MinHeap()
    length = len(arr)
    for x in arr:
        heap.push(x)
    for i in range(length):
        value = heap.retrieve_min()
        arr[i] = value
    print(arr)

unsortedArr = [3,6,4,1,5,2]
heapSort(unsortedArr)


