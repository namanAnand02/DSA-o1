## ~~~~~~~~~~ maximum consecutive one's ~~~~~~~~~~~~~~


## https://leetcode.com/problems/max-consecutive-ones/


## there is no need for brute, better or optimal 

def maximum(arr):
    count = 0 
    maxCount = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1 

        if arr[i] != 1:
            maxCount = max(maxCount, count)
            count = 0

    ## final check in case last elem was 1. Example: arr = [1,1,1]
    maxCount = max(maxCount, count)
             
    return maxCount


print(maximum([1,1,0,1,1,1,0,1,1])) ## 3


## Time - o(n) - one pass through the array 
## space - o(1) - uses only a few variables


def maximum2(arr):
    cnt = 0
    maxi = 0 

    for i in range(len(arr)):
        if arr[i] == 1:
            cnt +=1 
            maxi = max(cnt, maxi)

        else:
            cnt = 0 

    return maxi


print(maximum2([1,1,0,1,1,1,0,1,1]))