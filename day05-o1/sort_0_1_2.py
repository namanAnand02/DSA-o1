## ~~~~~~ Sort an array of 0's, 1's and 2's ~~~~~~~~~~ 

## LEETCODE - medium 

## method 01 : Brute force approach 

## ---> use some sorting algorithm - merge sort 

## time - o(nlogn)




## method 02 : 
## --> count the no of 0's, 1's and 2's and then override the array elements accodingly.


def sortColors(nums):
    cnt0 = 0 
    cnt1 = 0 
    cnt2 = 0 
    for i in range(len(nums)):
        if nums[i] == 0:
            cnt0 += 1 
        elif nums[i] == 1:
            cnt1 += 1 
        else:
            cnt2 += 1 

    for i in range(cnt0):
        nums[i] = 0
    for i in range(cnt0, cnt0 + cnt1):
        nums[i] = 1 

    for i in range(cnt0 + cnt1, cnt0 + cnt1 + cnt2):
        nums[i] = 2 



## time - O(n)
## space - o(1)


## ~~~~~~~~~~~~~~~~~~~~

## METHOD 03: MOST optimal - Dutch National flag algorithm


def func(arr):
    low = 0 
    mid = 0 
    high = len(arr) - 1 
    while mid <= high: ## this is the part of unsorted arr 
        if arr[mid] == 0:
            ## swap arr[low] and arr[mid]
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1 
            mid += 1 
        elif arr[mid] == 1:
            mid += 1 
        else: 
            ## arr[mid] == 2
            ## swap arr[mid] and arr[high]
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1 

    return arr 

print(func([1,0,0,1,1,0,2,1,0,2,0,0,2]))
## [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

## time : o(n) - one pass thorugh array 
## space - o (1) - in place swaps 


