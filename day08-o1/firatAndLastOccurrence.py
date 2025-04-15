## ~~~~~~~~ first and last occurrence ~~~~~~~~~ 


## https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

## given an sorted array of elements, find the first and last occurrence oof the target element 


def findOccurrences(arr, target):
    start = 0 
    end = len(arr) - 1 

    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == target:
            first = mid 
            end = mid -1 
        elif arr[mid] > target:
            end = mid -1 

        else:
            start = mid + 1 

    ## to find second occurrences 
    start = 0 
    end = len(arr) -1 
    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == target:
            second = mid 
            start = mid +1 

        elif arr[mid] > target:
            end = mid -1 

        else:
            start = mid + 1 

    return first, second 
    

## time - O(logn) + o(logn) = o(logn)
## space - o(1)


arr = [12,23,24,56,76,76,76,79]
arr = [12,23,24,56,76,76,76,79]

print(findOccurrences(arr, 76)) ## (4,6)

print(findOccurrences(arr, 79)) ## (7, 7)



## BRUTE force Approach - linear search 



def findFirstAndLast(arr, target):
    first, last = -1, -1 
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i 
            last = i 

    return [first,last]

## time - o(n) : as we scan evrry elems once 
## space - o(1)

arr1 = [12,23,24,56,76,76,76,79, 80, 80]
arr = [12,23,24,56,76,76,76,79, 81]
print(findFirstAndLast(arr1, 80)) ## (8,9)

print(findFirstAndLast(arr, 81)) ## (8,8)