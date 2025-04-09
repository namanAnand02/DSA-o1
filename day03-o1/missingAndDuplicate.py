## ~~~~~~ missing and repeated number ~~~~~~~~~~~~


## Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers in order of one space.

## Input:[3 1 2 5 3] 

## Output:[3, 4] 

## Duplicate = 3, Missing = 4 



## ---> to find duplicates, one way is to use dictionary. 


## method 01: using hashmap
def findDupli(arr):
    hashMap = {}
    for i in range(len(arr)):
        if arr[i] not in hashMap:
            ## storing elem as key and their frequency as value
            hashMap[arr[i]] = 1

        else:
            hashMap[arr[i]] += 1 

    for i in range(1,len(arr)+ 1):
        if i not in hashMap:
            missing= i
    for i in hashMap:
        if hashMap[i] > 1:
            repeated = i

    return missing, repeated


print(findDupli([1,4,3,4,5]))



def missingAndRepeated(arr):
    hashMap = {}
    missing= -1 
    repeated = -1 

    for i in arr:
        if i not in hashMap:
            hashMap[i] = 1 

        else:
            hashMap[i] += 1 

    for i in range(1, len(arr) + 1):
        if i not in hashMap:
            missing = i 

        elif hashMap[i] > 1:
            repeated = i 

    return missing, repeated

print(missingAndRepeated([1,2,3,3,4])) ## 5, 3


## time: o(n)
## space: o(n)




