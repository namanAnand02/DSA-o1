

## ~~~~~~~~~ divide array into 2 subarray with equal sum ~~~~~~~~~~~~


## Method 01 : 
def func2(arr):
    for i in range(len(arr) -1 ):
        leftSum = 0
        rightSum = 0 
        for j in range(0, i +1):
            leftSum += arr[j]

        for j in range(i+1, len(arr)):
            rightSum += arr[j]

        if leftSum == rightSum:  
            return 1 
        
    return -1 


print(func2([3,4,-2,5,8,20,-10,8]))

# time - o(n2)
# space - o(1)




## Method 02 : 

def func(arr):
    leftSum = 0 
    totalSum = sum(arr)
    for i in range(len(arr) -1 ): ## we only traverse till n-2th index elem, as we are dealing with left side and rigght side of i both
        leftSum += arr[i]
        rightSum = totalSum - leftSum 

        if leftSum == rightSum:
            return 1 
        
    return -1 



print(func([3,4,-2,5,8,20,-10,8]))

## time - o(n)
## space - o(1)




## NOTE: how to take user's input?

n = int(input("enter the length of array: "))
arr = [int(x) for x in input(f"Enter {n} elements separated by space: ").split()]
print(arr)



## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Prefix and suffix 

# def findPrefixArr(arr):
#     prefixArr = [arr[0]]
#     prefix = arr[0]
#     for i in range(1,len(arr)):
#         prefix += arr[i]
#         prefixArr.append(prefix)

#     return prefixArr


# print(findPrefixArr([1,2,3,4]))