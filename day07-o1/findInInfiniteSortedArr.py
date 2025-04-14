## Array is of infinite length and we have been given a target, find out if that target elem is present in the array or not? 

##  note - infinite sorted meaning we cant use length method here, as the upper bound is not defined 


## --> so we move in chunks, and try to find out the region in which our target elem lies
## if we find it, we apply BS to find the target index 
## else, we double the size of chunk 

## this way - we're doing reverse of what we do usually with the BS
## usually, we half the size of array by 2 in each step - total steps that way - logn
## in here, we increase the size of array by 2 in each step - total steps req here as well = logn 

def binarySearch(arr, target, start,end):
    while start <=end:
        mid = start + (end - start) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            start = mid +1  
        else:
            end = mid -1 

    return -1 



def findRange(arr, target):
    start = 0 
    end = 1 
    ## expand the window exponentially 
    while arr[end] < target:
        prevStart = start
        start = end +1 
        end = (end + ((end - prevStart) + 1 )* 2)

    return binarySearch(arr,target, start,end)

    

print(findRange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,23,34,35,57,67], 9))

## note: since we working on infinite size arr but here, we are taking a finite size arr - make sure to take the right example=, something in which Index bound error doesn't show. 
## Like in the above ex, if target is say 15, then it would lie in the range of start = 14, end = 29, but there isn't 29 elems in arr, so it will through index bound error from our code. 



## time = O(logn) + o(logn) ==== o(logn )
## space = O(1)




## ~~~~~~ Paypal interview questionn ~~~~~~~~~~~~~

## Implement an LRU cache (leetcode hard)
## find the longest subs without repeating chars 
## Given a binary tree, ptint the right view of the tree 
## Design a rate limiter for an API 
## Find the top K frequent elements in a stream of numbers 
## Implement a thread safe singleton in JAVA 

