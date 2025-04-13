## maximum difference betweeen two elememnts ~~~~~~~~~~

def maximumDifference1(arr):
    maxi = float("-inf")
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            maxi = max(maxi, arr[j]- arr[i])

    return maxi 


print(maximumDifference1([9,5,8,12,2,3,7,4])) ## 7 



## ~~~~~~~~~~~~~~~~~~~~~~~~~

## Optimal approach 
## using suffix max 


## MWthod 02 : Suffix max concept 

def maximumDifference2(arr):
    suffixMax = arr[-1]
    ## then we start iterating from 2nd last element
    ## we take the diff for them, i.e diff of arr[i] elem and the suffixMax until them 
    ## we will also updater the suffixMax value here 
    ## and we update the maxDiff value too. 

    maxiDiff = float("-inf")
    for i in range(len(arr)-2, -1,-1):
        diff = suffixMax - arr[i]
        ## update the maxi diff 
        maxiDiff = max(maxiDiff, diff)
        ## update the suffixMax value 
        suffixMax = max(suffixMax, arr[i])


    return maxiDiff

## time - o(n) - in one pass 
## space - o(1) - no extra space used. 


print(maximumDifference2([9,5,8,12,2,3,7,4])) ## 7 





