## ~~~  LEETCODE: 1752- check if array is sorted and rotated ~~~~~~~~

## Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.There may be duplicates in the original array.

## Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.


# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/




def checkSortedAndRotated(nums):
    ## we can use break point concepts here
    ## if an arrays is sorted and rotated, it must have only one break point. 
    count = 0 
    for i in range(len(nums)):
        if nums[i] > nums[(i+1 )% len(nums)]: ## it is to handle cyclic wrap up. 
        ## when i = len(nums) -1 , i.e last element, it will consider comparing it with 0th index elem and wont show index error.
            count += 1 

        if count >1 :   ## as soon as count > 1, immediately return False
            return False 

    return True 



print(checkSortedAndRotated([3,4,5,1,2])) ## TRUE
print(checkSortedAndRotated([1,2,3,4,5]))  ## TRUE
print(checkSortedAndRotated([1,2,2,4,5]))  ## TRUE
print(checkSortedAndRotated([1,2,22,4,5]))  ## False
 