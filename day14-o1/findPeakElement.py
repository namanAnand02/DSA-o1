## ~~~~~~~~~~ Finde peak element ~~~~~~~~~~~~~~~~

## all distinct elements in the array 


## in case of multiple peaks, return any of the peak. 



def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    

    start = 0 
    end = len(nums) -1 

    while start <= end:
        mid = start + (end - start) // 2

        if mid == 0 and nums[mid] > nums[mid +1 ]:
            return mid 
        
        elif mid == len(nums) -1 and nums[mid] > nums[mid -1 ]:
            return mid 
        
        else:
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid -1 ]:
                return mid 
            elif nums[mid] < nums[mid + 1]:
                start = mid +1 

            else:
                end = mid - 1 


## time - o(logn)
    
# print(findPeakElement([1,2,3,1])) ## 2
# print(findPeakElement([11])) ## 0
# print(findPeakElement([11,12])) ## 1 
# print(findPeakElement([1,2,1,3,5,6,4]))  ## 5
            



## Brute force approach - for loop 

## o(n) time 

## this approach is also helpful in finding the peak element even when there are duplicates in the array. 

def findPeaK_brute(nums):
    if len(nums) == 1:
        return 0
    for i in range(len(nums)):
        if (i == 0 and nums[i] > nums[i +1 ]):
            return i 
        

        elif (i == len(nums)-1 and nums[i] > nums[i -1 ]):
            return i 
        
        else:
            if (nums[i] > nums[i + 1] and nums[i] > nums[i -1 ]):
                return i 
            


## time - o(n) 

print(findPeaK_brute([10])) ## 0
print(findPeaK_brute([10,12])) ## 1 
print(findPeaK_brute([10,12, 11, 9, 13, 8])) ## 1 
print(findPeaK_brute([10,11,13, 19, 23, 24])) ## 5


## in case the question asks us to return all the peaks -- we can do that as well with this approach 
## we can store all the peaks in a separate data structure as we move along the array and find them and then finally return that data structure as the final answer. 
        
    