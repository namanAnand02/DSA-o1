## ~~~~~~~~~ Binary search - ascending ~~~~~~~~~~~~~~

def Bs(arr, target):
    start = 0 
    end = len(arr)- 1 
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid 
        
        elif arr[mid] > target:
            end = mid -1 
        else:
            start = mid + 1 

    return -1 

## time - o(logn)
## space - o(1)

print(Bs([12,23,24,56,118], 56))  ## 3

## ~~~~~~~~~~~~ binary search - descending sorted arr ~~~~~~~~~~


def BsDes(arr, target):
    start = 0 
    end = len(arr)- 1 
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid 
        
        elif arr[mid] > target:
            start = mid +1 
        else:
            end = mid - 1 

    return -1 

## time - o(logn)
## space - o(1)


print(BsDes([15,13,12,11,9,5,1], 11)) ## 3