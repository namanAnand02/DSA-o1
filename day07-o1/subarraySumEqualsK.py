## ~~~~~~~~~~~~ Subarray sum equals k ~~~~~~~~~~~~~~~~~~



## Leetcode medium - https://leetcode.com/problems/subarray-sum-equals-k/


def subarraySum(arr,k):
    count = 0
    for i in range(len(arr)):
        sumV = 0
        for j in range(i, len(arr)):
            sumV += arr[j]
            if sumV == k:
                count += 1 

    return count 
    
## time - o(n^ 2)
## space - o(1)


print(subarraySum([9,4,20,3,10,5], 33)) ## 2 - [9,4,20], [20,3,10]

        


## ~~~~~~~~~~~~~~

## Method 02 : Optimal approach 

## Prefix Sum + hashMap 


def subarraySum2(nums,k):
    hashMap = {0:1} 
    prefixSum = 0 
    count = 0 

    for i in range(len(nums)):
        prefixSum += nums[i]
        if (prefixSum - k) in hashMap:
            count += hashMap[prefixSum - k]

        ## if or not we find the complement in the hashMap, we store them into hashMap 
        if prefixSum in hashMap:
        
            hashMap[prefixSum] += 1
        else:
            hashMap[prefixSum] = 1 

    return count 


## time - O(n)
## space - o(n)

print(subarraySum2([1,1,1], 2))

