## ~~~~~~~~ search in nearly sorted array ~~~~~~~~~~~~~~~

## nearly sorted array meaning - an ith elem could be at i +1, oi or i-1th place 

## Find element in [10, 3, 40, 20, 50, 80, 70], where every element is at most 1 index away from the sorted position.


## [5,10,30,20,40], target = 20 

## So how do we solve this problem 

## find the mid 

## check if mid elem == target ? return mid 
## check if mid -1 elem == target ? return mid - 1 
## check if mid + 1 elem == target ? return mid +1 

## NOTE: before comapreing with mid -1 or mid +1 , first make sure they exist 
## i.e compare with mid -1 elem when mid -1 >= start 
## i.e compare with mid +1 elem when mid + 1 <= end


## elif mid elem < target ? start = mid + 2 

## else when mid elem > target ? end = mid -2 

## code part 


def findInNearlySorted(nums, target):
    start = 0 
    end = len(nums) -1 
    
    while start <= end:
        mid = start + (end -start) //2 

        if nums[mid] == target:
            return mid 
        elif mid - 1 >= start and nums[mid - 1 ] == target:
            return mid -1 
        elif mid + 1 <= end and nums[mid +1 ] == target:
            return mid +1  
        
        elif nums[mid] < target:
            start = mid +2
        else:
            end = mid -2 

    return -1 

print(findInNearlySorted([5,10,30,20,40], 20)) ## 3




## time - o(logn)
## space - o(1)

