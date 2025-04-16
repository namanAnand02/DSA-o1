## ~~~~~~~ search insert position ~~~~~~~~~~~

## Leetcode easy problem - https://leetcode.com/problems/search-insert-position/description/


## Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## You must write an algorithm with O(log n) runtime complexity.



def searchInsert(nums, target):
    start = 0 
    end = len(nums) -1 
    potentialAns= len(nums) ## incase the target> all of array elems

    while start <= end:
        mid = start+ (end - start) // 2 

        if nums[mid] == target:
            return mid 
        
        elif nums[mid] < target:
            start =mid + 1 
        else:
            potentialAns = mid 
            end = mid -1 

    return potentialAns 



nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target)) ## 4