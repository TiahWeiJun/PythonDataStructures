#Have two sections in the array, sorted and non sorted. Iterate through the elements in the unsorted section and place them into the sorted section accordingly
#Time complexity for best case scenario is O(n) while for worst case scenario is O(n^2).
#Space complexity is O(1) as it is in-place sorting
#Stable Sorting Algorithm


def insertionSort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        hole = i
        while arr[hole-1] > value and hole > 0:
            arr[hole] = arr[hole-1]
            hole-=1
        arr[hole] = value
    print(arr)
        
unsortedArr = [6,5,4,3,2,1]
insertionSort(unsortedArr)