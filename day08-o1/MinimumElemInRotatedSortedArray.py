## ~~~~~~~~ Find minimum elem in rotated sorted arrray ~~~~~~~~~~~~


## https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

## Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

## [4,5,6,7,0,1,2] if it was rotated 4 times.
## [0,1,2,4,5,6,7] if it was rotated 7 times.


## Given the sorted rotated array nums of unique elements, return the minimum element of this array.

## You must write an algorithm that runs in O(log n) time.




    ## min elem always lies in right sorted side of array - only in case of rotated sorted array
    ## also note that in case of rotated sorted array, at any instance, mid elem always divides the array into two part - sorted and unsorted part - and if mid elem itself is not min elem, then min elem is always found in unsorted part of the array.

    ## step1: find the mid elem 
    ## check if this mid elem is min or not - do it by comparing it with its left and right frnd
    ## if mid is not min, we then find out which side sorted mid elem lie
    ## that helps us decide which side to move next to find the min elem 
    ## if mid elem is lying in left sorted side, we know for sure the min elem lies in right sorted and so we can move to right of mid to search for min elem 
    ## else if mid elem is already in right sorted side, we can move to left side of mid to find min 
    ## to check if mid elem lies in left or right sorted, we can compare it with start and end 
    ## if arr[mid] <= arr[start] -- > mid lying in right sorted side --> move left of it 
    ## if arr[mid] >= arr[start] --> mid lying in left sorted side --> move right of it  

def findMinElem(nums):

    start = 0 
    end = len(nums) -1 


    while start <= end:
        mid = start + (end - start) // 2 
        next = (mid +1 ) % len(nums) ## mid = len(nums) -1, next = 0
        prev = (mid + (len(nums) -1)) % len(nums) ## mid = 0, prev = len(nums) -1 

        ## when array is completely sorted 
        if nums[start] <= nums[end]:
            return nums[start]

        ## check if mid == min elem 
        if nums[mid] <= nums[prev] and nums[mid] <= nums[next]:
            return nums[mid] 
        
        if nums[mid] >= nums[start]: ## mid lying in left sorted side and we need to move right 
            start = mid + 1 
        # elif nums[mid] <= nums[end]: 
            ## mid lying in right sorted side and we know if this is not min, we search left to it.
        else:
            end = mid -1 





## time involved = o(logn)