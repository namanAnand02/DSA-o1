## ~~~~~~~~ find the secind largest element in the array ~~~~~~~~~~\


def secondLargest(arr):

    largest = arr[0]
    sLargest =-1
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
    for i in range(len(arr)):
        if arr[i] != largest and arr[i] > sLargest:
            sLargest = arr[i]
            
    return sLargest 
        
## time: o(2n)
## space : o(1)



def secondLargest2(arr):
        
    largest = arr[0]
    sLargest = -1 
    for i in range(len(arr)):
        if arr[i] > largest:
            sLargest = largest 
            largest= arr[i]
            
        elif arr[i] > sLargest and arr[i] < largest:
            sLargest = arr[i]
    
            
    return sLargest 

## time : o(n)
## space: o(1)



print(secondLargest([12,23,35,1,34,2])) ## 34
print(secondLargest2([12,23,35,1,34,2])) ## 34 
