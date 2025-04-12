## ~~~~~~~~~~ Majprity element : > n/2  ~~~~~~~~~~~~~~~

## LEETCODE : 169 - https://leetcode.com/problems/majority-element/description/


## method 01 : brute force 

## - using hashmap 
def majorityElem(nums):
    hashMap = {}
    for i in nums:
        hashMap[i] = hashMap.get(i,0)+ 1
    
    for i in hashMap:
        if hashMap[i] > len(nums)/2 :
            return i 
        


print(majorityElem([3,2,3])) ## 3 
print(majorityElem([2,2,1,1,1,2,2])) ## 2



## optimal approach - Moore's voting algorithm 

def majorityElem2(nums):

    ## Moore voting algorithm 
    ## time - o(n), space - o(1)

    cnt = 0 
    elem= None
    for i in nums:
        ## if cnt = 0, think of start - so we assign elem 
        if cnt == 0:
            elem = i
            cnt =1 

        ## if elem is found, increment the count 
        elif i == elem:
            cnt += 1
        ## else, decrement the count 
        else:
            cnt -= 1 

    ## at last, the elem which dominates and that whose corresponding count didnt get zero - should be the majority elem.
    

    ## verify the elem 
    # Optional verification step (only needed if majority element is not guaranteed)
    cntNew = 0 
    for i in nums:
        if i == elem:
            cntNew += 1 
    if cntNew > len(nums)/2:
        return elem 
    else:
        return - 1 