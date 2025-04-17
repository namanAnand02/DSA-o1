
## ~~~~~~~~~~ Find peak element ~~~~~~~~~~~~~~

## duplicates are not present 

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


def findPeakWithDuplicates(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        elif arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            # arr[mid] == arr[mid + 1], reduce the search space conservatively
            # Could also check arr[mid] == arr[mid-1], and adjust accordingly
            end -= 1  # Or start += 1
    return start  # or end, both are same here


arr = [1, 2, 2, 2, 3, 2, 1]
print(findPeakWithDuplicates(arr)) ## 4 