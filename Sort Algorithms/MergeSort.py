#Divide the array into two smaller arrays recursively till there is only 1 element in the array then we merge them together in order
#TIme complexity for best case and worst case scenario is O(nlogn)
#Space complexity is O(n)
#Stable Sorting Algorithm


def mergeSort(arr):
    if len(arr) == 1:
        return
    else:
        middle = len(arr)//2
        left_array = arr[0:middle]
        right_array = arr[middle:len(arr)]

        mergeSort(left_array)
        mergeSort(right_array)
        merge(left_array, right_array, arr)
    


def merge(leftarr, rightarr, arr):
    k = 0
    while lenlefta) > 0 and len(rightarr) > 0:
        if leftarr[0] <= rightarr[0]:
            arr[k] = leftarr[0]
         leftarr.pop(0)
        elif rightarr[0] < leftarr[0]:
            arr[k] = rightarr[0]
            rightarr.pop(0)
        k += 1

    if len leftarr) == 0:
        while len(rightarr) > 0:
            arr[k] = rightarr[0]
            rightarr.pop(0)
            k += 1

    elif len(rightarr) == 0:
        while len leftarr) > 0:
            arr[k] = leftarr[0]
         leftarr.pop(0)
            k += 1
   


unsortedArr = [6,3,2,4,5,1]
mergeSort(unsortedArr)
print(unsortedArr)


