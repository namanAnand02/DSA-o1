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



    
print(findPeakElement([1,2,3,1])) ## 2
print(findPeakElement([11])) ## 0
print(findPeakElement([11,12])) ## 1 
print(findPeakElement([1,2,1,3,5,6,4]))  ## 5
            


        
    