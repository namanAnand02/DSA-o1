## Order Agnostic array 
 
# array in which its not specified whether its increasing or decreasing sorted 

## we'll first try to find out which type of sorted this array is 

## to do that, we can compare two pos elems - say 1st index and 0th index and we'll have an idea 


## NOTE: only if its specified clearly the array is not one of mountain array - is when we'll try and findout which direction sorted this is 

## ex : [1,2,3,4,5,65] ---> increasing sorted - arr[2], arr[1], arr[3].... > arr[0]


## ex : [10,9,8,7,6,5] ---> decreasing sorted - arr[3], arr[2], arr[1]... < arr[0]


## mountain arr: exception of this case - part of this is inc sorted and some part of this is dec sorted - [2,3,4,5,4,3,2,1]

