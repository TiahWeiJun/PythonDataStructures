#Iterate over array to find minimum value and put it to the front of the array
#Time complexity is O(n^2) in worse case scenario as well as best case scenario due to double for loop
#Space complexity is O(1) as it is sorting in place
#Not a stable algorithm. elements with same value might end up swapping their positions in the array

def selectionSort(arr):
    for i in range(len(arr)-1):
        minindex = i
        minvalue = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] < minvalue:
                minindex = j
                minvalue = arr[j]
        arr[i],arr[minindex] = arr[minindex],arr[i]
    return arr



unsortedArr = [3,6,1,4,2,5]
selectionSort(unsortedArr)