## ~~~~~~~~~~ Minimum difference element in sorted array ~~~~~~~~~~~~~~~~~


## given a sorted array, return the element whose abs difference with the key is smallest of all

## arr = [1,3,5,8,10,15], key = 12 - o/p = 10 as abs diff with key = 2 is smallest of all 



## approach 

## if key is itself present in the array, return the key 
## if key is not present in the array, find its neighouring elem in the array - take their abs diff with the key and find the minimum. 

## when BS ends, the start pointer usually lies at right neighbour of key 
## and the end pointer lies at the left neighbour of key 

## so when BS ends, and we couldn't find key in array, just calculate the min of the abs diff of both neighbours with key 



def minAbsDiff(arr, key):
    start = 0 
    end = len(arr) -1 

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return key 
        
        elif arr[mid] > key:
            end = mid - 1 

        else:
            start = mid +1 

    ## if we couldn't find the key element in the array 
    # return min(abs(arr[start] - key), abs(arr[end] - key))

    if abs(arr[start] - key) < abs(arr[end] - key):
        return arr[start]
    
    else:
        return arr[end]
    




arr = [1,3,5,8,10,15]
arr1 = [1,3,5,8,10,12,15]
key = 12 

print(minAbsDiff(arr,key))
print(minAbsDiff(arr1,key))



## our implementation can raise an index error in edge cases, especially when:

## key < arr[0] → then start = 0, end = -1

## key > arr[-1] → then start = len(arr), which is out of bounds



## below is the final updated code which handles that edge cases as well: 

def minAbsDiff(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return key

        elif arr[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    # Handle edge cases
    if start >= len(arr):  # key > arr[-1]
        return arr[end]

    if end < 0:  # key < arr[0]
        return arr[start]

    # Now key lies between arr[end] and arr[start]
    if abs(arr[start] - key) < abs(arr[end] - key):
        return arr[start]
    else:
        return arr[end]



## time - o(logn)
## space - O(1)




## ~~~~~~

## not exactly same problem, but worth trying below problems after this - 


## https://www.geeksforgeeks.org/find-closest-number-array/

## https://leetcode.com/problems/find-k-closest-elements/