#Recursively choose a pivot and place smaller elements to the left and larger elements to the right
#Time complexity for best case scenario is O(nlogn) and worst case scenario is O(n^2), but worst case scenario can be avoided by randomizing pivot
#Space Complexity is O(1) as sorting is in place
#UnStable Sorting Algorithm
import random

def quickSort(arr, start, end):
    if start < end:
        pIndex = partition(arr,start,end)
        quickSort(arr, start, pIndex - 1)
        quickSort(arr, pIndex+1, end)
    else:
        return


def partition(arr, start, end):
    randomIndex = random.randint(start, end+1)
    arr[randomIndex], arr[end] = arr[end], arr[randomIndex]
    pivotValue = arr[end]
    pIndex = start
    for i in range(start,end):
        if arr[i] < pivotValue:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return pIndex


#unsortedArr = [1,4,4,2,6,5,3]
#quickSort(unsortedArr, 0 ,len(unsortedArr) - 1)
#print(unsortedArr)

                
def getTotalX(a, b):
    # Write your code here
   print(a, b)

print(getTotalX([2,4], [16,32,96]))