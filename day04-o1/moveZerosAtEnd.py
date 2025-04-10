## ~~~~ MOVE ZEROS at the end ~~~~~~~~~~~
## leetcode: 283 : https://leetcode.com/problems/move-zeroes/description/


## Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

## Note that you must do this in-place without making a copy of the array.



## Brute force approach 
def moveZeros(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp),len(arr)):
        arr[i] = 0 

    return arr 


print(moveZeros([1,0,2,3,0,4,1,0,0,6]))
## [1, 2, 3, 4, 1, 6, 0, 0, 0, 0]

## time: O(n + n - x + x) = o(2n)
## space : o(x) or in worst case o(n) when all elements are non zero elems 


def moveZeros2(nums):
    ## do not return anything, and perform nums in-place operations 

    start = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1 


    return nums 

print(moveZeros2([1,2,0,0,8,9,20,0,5,0,22]))
## [1, 2, 8, 9, 20, 5, 22, 0, 0, 0, 0]

## time : o(n)
## space: o(1)