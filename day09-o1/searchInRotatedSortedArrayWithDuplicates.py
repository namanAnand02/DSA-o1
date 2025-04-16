## ~~~~~ search in rotated sorted array with duplicates ~~~~~~~~~


## There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

## Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

## You must decrease the overall operation steps as much as possible.

## Input: nums = [2,5,6,0,0,1,2], target = 0
## output = True 


## ~~~~~~~~~~~~ solution : 




## in the previous approach - where finding min elem first and then applying BS on both sorted part won't work here as finding min elem is not easy when duplicates are present - 

##  in nums[mid] <=nums[prev] and nums[mid] <= nums[next]: this check itself will not work when duplicates are present. 
## ex: [3,3,3,3,3,3,3,3,3,1,3,3,3,3,3,]

## When nums[start] == nums[mid] == nums[end], you cannot determine whether the minimum element lies on the left or right half.



def SearchInRotatedWithDuplicates(nums, target):

    start = 0 
    end = len(nums) -1 
    while start <=end:

        mid = start + (end - start) // 2 

        if nums[mid] == target:
            return True 

        ## to handle duplicates 
        if nums[start] == nums[mid] == nums[end]:
            start += 1 
            end -= 1 
            continue 

        ## now find out which sorted side this mid elem lies 
        if nums[start] <= nums[mid]: 
            ## mid elem lying in left sorted array 
            ## now we search for target in [start, mid] range 
            if nums[start] <= target <= nums[mid]:
                end = mid -1 
            else:
                start = mid +1 
            
        elif nums[start] > nums[mid]: 
            ## mid elem lying in right sorted array 
            ## so now we'll search for target in right sorted part - [mid, end]
            if nums[mid] <= target <= nums[end]:
                start = mid +1  
            else:
                end = mid -1 

    return False  


## Worst Case: O(n) (if many duplicates require skipping).
## Average Case: O(log n) for binary search when duplicates are minimal.


## two things are imp worth taking care :

## 1. handle duplicates ---> 
## To handle duplicates in a rotated sorted array, we need to account for cases where the elements at start, mid, and end are the same. This can cause ambiguity in determining which side of the array is sorted. A common solution is to skip duplicates from the start or end when they are equal to the middle element.

## When nums[start] == nums[mid] == nums[end], it becomes ambiguous to determine which part is sorted. In this case, you skip the duplicate elements by incrementing start and decrementing end.



## 2. during checking of which side sorted is mid elem, dont compare it with oth index or -1st index 
## rather, compare with start and end as because of duplicates, start and end pos may change and they may not always be 0 and -1

## ex: arr = [1,0,1,1,1], target == 0