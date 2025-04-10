## ~~~~~~~~~~ Largest element in the array ~~~~~~~~~~~~~


nums = [12,1,23,32,8,0]
largestElem = 32 

## https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0



## Brute force 
## --> sort the array and last elem is the largest element in the array. 
## --> time: o(nlogn) in sorting, space: o(1)

def largest(nums):
    nums.sort()
    return nums[-1]

print(largest([12,13,14,2,3,90])) ## 90

## better approach 
## ---> assume first element is largest element. Traverse through the arraay and keep comparing them. 


def largest2(nums):
    largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i]> largest:
            largest = nums[i]

    return largest 


print(largest2([14,2,12,41,5,23])) ## 41 



