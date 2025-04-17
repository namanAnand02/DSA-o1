
## ~~~~~~~~~~ Find peak element ~~~~~~~~~~~~~~

## duplicates are not present and any peak can be returned as the answer

## Leetcode medium - https://leetcode.com/problems/find-peak-element/description/





def findPeakElement(arr):

    ## 17 apr 25 
    ## its given that duplicates are not present 
    start = 0 
    end = len(arr) -1 
    if len(arr) == 1:
        return 0
    while start <=end: 
        mid = start + (end - start) // 2 

        if mid > 0 and mid < len(arr) -1 :
            if arr[mid] > arr[mid -1 ] and arr[mid] > arr[mid +1]:
                return mid 

            elif arr[mid] < arr[mid- 1]:
                end = mid-1 

            else:
                start = mid + 1 

        if mid == 0:
            if arr[mid] > arr[mid+ 1]:
                return mid
            else:
                return mid +1 
        if mid == len(arr) -1:
            if arr[mid] > arr[mid -1 ]:
                return mid 
            else:
                return mid -1 
            

## time - o(logn)
## space - o(1)

# nums = [1,2,1,3,5,6,4]
# output = 5 






## ~~~~~~~~~ 

## what if duplicates are present in the array? 
## and we have to return the maximum peak 

## in case, duplicates are present, we'll have to use linear scan - BS can't find max peak in array with duplicates


def findMaximumPeak(arr):
    peak = arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            peak = max(peak, arr[i])
    peak = max(peak, arr[0], arr[-1])
    return peak



## time - o(n)
## space = o(1)







### NOTE : 
## If we want any peak → Binary Search → O(log n)
## But if we want the maximum peak → we must scan all elements → O(n) is the best possible.