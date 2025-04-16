## ~~~~~~~~ search in rotated sorted array ~~~~~~~~~~~~~

##  Leetcode medium -  https://leetcode.com/problems/search-in-rotated-sorted-array/description/ 


## Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.



def binarySearch(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) //2 
        if nums[mid] == target:
            return mid 

        elif nums[mid] < target:
            start = mid +1 
        else:
            end = mid -1 

    return -1 


def searchElement(nums, target):

    ## first find min elem 
    start = 0 
    end = len(nums) -1 
    while start <= end:
        mid = start + (end - start) // 2 
        if nums[start] <= nums[end]:
            ## array is completley sorted 
            minIndex = start 
            break 

        ## min elem - find it by comparing it with its neighbours 
        prev = (mid + (len(nums) - 1 )) % len(nums)
        next =( mid +1 ) % len(nums)

        ## comparing it with its neighbors to find if it is mimimum or not 
        if nums[mid] <=nums[prev] and nums[mid] <= nums[next]:
            minIndex = mid 
            break 
        
        ## elif we'll find which side sorted mid elem is lying currently and then we'll move towards the right sorted side
        ## as min elem always lies in right sorted side of rotated sorted array 

        elif nums[mid] >= nums[start]:
            ## mid is currently is left sorted side 
            ## min elem lies in right sorted side, so move right 
            start = mid + 1 

        else:
            ## mid is in right sorted part 
            ## so we move left to search min elem
            end = mid -1 

    
    ## so far, we have findout min elem index in the given array.
    ## the whole point of finding the minimum element in the array was to get an idea about the two sorted side of the rotated array.
    ## if minimum element itself is the target, fir to balle balle! nahi to it has served enough. 

    ## because of the minimum element, now we know the left and right sorted part of array - and we can individually apply BS on each of them to search the target element. 

    ## [0, min elem - 1] - left sorted part of array 
    ## [min elem, n -1] - right sorted part of array  

    if nums[minIndex] == target:
        return minIndex 
    

    ## applying BS on left sorted part of array - [0, minElem-1]

    leftAns = binarySearch(nums, target, 0, minIndex-1 )

    ## if target is not present in left sorted part - only then we apply BS on right sorted part of the array
    if leftAns == -1:
        rightAns = binarySearch(nums, target, minIndex+1, len(nums)- 1)
        return rightAns 
    else:
        return leftAns
    


## Input: nums = [4,5,6,7,0,1,2], target = 0
## Output: 4



## first find the index of the minimum element in rotated array using binary search 
## minimum element in rotated array divides the array into two left and right sorted part 
## then perform Bs on both sorted part of the array individually to find the target. 


## o(logn)-> finding  min elem     + 
## o(logn)--> bs on sorted parts  

## Total time = o(logn)

## space - o(1)