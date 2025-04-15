## ~~~~~~~~~~ Count of an element in sorted array ~~~~~~~~~~~ 


## https://www.naukri.com/code360/problems/occurrence-of-x-in-a-sorted-array_630456?leftPanelTabValue=PROBLEM

## total count of an elem = second - first +1


def count(arr, x):

    start = 0 
    end = len(arr) -1 
    first = second = -1
    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == x:
            first = mid 
            end = mid -1  

        elif arr[mid] < x:
            start = mid +1 

        else:
            end = mid -1 

    start = 0 
    end = len(arr) -1 
    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == x:
            second = mid 
            start = mid +1 

        elif arr[mid] < x:
            start = mid +1 

        else:
            end = mid -1 


    ## IMP: edge case handled if there was no such elem in the array 
    if first != -1:
        return second - first +1 

    else:
        return 0
    


## time - o(logn)
## space - o(1)


