## ~~~~~~~~~ Largest Sum Contiguous Subarray ~~~~~~~~~~~~~~~~~

## Kadane's algorithm 

def largestSum(arr):
    maxi = float("-inf")
    prefix = 0 
    for i in range(len(arr)):
        prefix += arr[i]

        maxi = max(maxi, prefix)

        ## kadane's algorithm statement 
        if prefix < 0:
            prefix = 0 

    return maxi 


print(largestSum([3,4,-5,8,-12,7,6])) ## 13 


## time - o(n)
## space - o(1)





## BRUTE force approach for the above problem 
## --> find all subarray and compare 

def func(arr):
    maxi = float("-inf")
    for i in range(len(arr)):
        prefix = 0 
        for j in range(i, len(arr)):
            prefix += arr[j]

            maxi = max(prefix, maxi)

    return maxi 

print(func([3,4,-5,8,-12,7,6])) ## 13 

## time - o(n^2)
## space - o(1)

