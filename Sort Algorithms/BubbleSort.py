#Compare the element with the element beside and swap until the largest element is pushed to the right
#Time complexity is O(n^2) in worse case scenario and O(n) in best case scenario due to double for loop
#Space complexity is O(1) as it is sorting in place
#Stable Sorting Algorithm


def bubbleSort(arr):
    for i in range(len(arr)):
        swap = 0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap+=1
        if swap == 0:
            break
    print(arr)

unsortedArr = [6,5,4,3,2,1]
bubbleSort(unsortedArr)