## ~~~~~~~~~~ find out the first occurrence of infinity ~~~~~~~~~~~

## there are finite blocks of array in which starting x elements are finite numbers. After one point, all the elements inside the array are infinity. Find out the first occurrence of Infinity. 

## [2,4,2,12,45,13,55,6, inf, inf, inf,inf,inf,inf,inf]

## we can apply binary search here as it states that after one point, its all always inf element in the array. 
## so we can easily decie which side to move after finding mid elem in order to find the first inf eleme in the array. 

def firstInf(arr):
    start = 0
    end = len(arr) -1 

    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == "inf":
            result = mid 
            end = mid - 1 

        else: ## if arr[mid] == finite elem, we know for sure inf elem is at right. 
            start = mid + 1 


    return result 



arr = [2,4,2,12,45,13,55,6, "inf", "inf", "inf","inf","inf","inf","inf"]
print(firstInf(arr)) ## 8 