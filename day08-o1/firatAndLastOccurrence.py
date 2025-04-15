## ~~~~~~~~ first and last occurrence ~~~~~~~~~ 

## given an sorted array of elements, find the first and last occurrence oof the target element 


def findOccurrences(arr, target):
    start = 0 
    end = len(arr) - 1 

    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == target:
            first = mid 
            end = mid -1 
        elif arr[mid] > target:
            end = mid -1 

        else:
            start = mid + 1 




    start = 0 
    end = len(arr) -1 
    while start <= end:
        mid = start + (end - start) // 2 
        if arr[mid] == target:
            second = mid 
            start = mid +1 

        elif arr[mid] > target:
            end = mid -1 

        else:
            start = mid + 1 

    return first, second 
    



arr = [12,23,24,56,76,76,76,79]
arr = [12,23,24,56,76,76,76,79]

print(findOccurrences(arr, 76)) ## (4,6)

print(findOccurrences(arr, 79)) ## (7, 7)