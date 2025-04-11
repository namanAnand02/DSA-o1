## ~~~~~ Intersection of two  sorted arrays with duplicates ~~~~~~~


## NOTE: result array can have duplicates 

## BRUTE FORCE - o(n * m)
def intersection(nums1,nums2):
    result = []
    vis = [0]* len(nums2)
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j] and vis[j]== 0:
                result.append(nums1[i])
                vis[j] = 1 
                break 
            
            ## also, no point continuing finding intersection in nums2 beyond when nums2 elem > current nums1 elem as nums2 is also sorted.
            if nums2[j] > nums1[i]:
                break 

    return result 


nums1 = [1,2,2,3,3,4,5,6]
nums2 = [2,3,3,5,6,6,7]
print(intersection(nums1, nums2)) ## [2,3,3,5,6]

## time - o(n1 * n2)
## space - o(n2)



## METHOD 02 : Two pointers (hint- sorted arrays)

def intersection2(nums1, nums2):
    i, j = 0, 0 
    ans = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1 
        elif nums1[i] > nums2[j]:
            j += 1 

        else:
            ## nums1[i] == nums2[j]
            ans.append(nums1[i])

            i += 1 
            j += 1 

    return ans 

nums1 = [1,2,2,3,3,4,5,6]
nums2 = [2,3,3,5,6,6,7]
print (intersection2(nums1, nums2)) ## [2,3,3,5,6]

## time : o(n1 + n2)
## space : O(k)






## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


## INTERSECTION OF TWO ARRAYS : leetcode- 349 easy 

## https://leetcode.com/problems/intersection-of-two-arrays/


## Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


## rem - in leetcopde problem, unsorted array is given and also they expect you to return the result array having no duplicates. 



## given arrays are unsorted 
## and also the order of numbers in the result array does not matter here, so we can use set

## method 01 - using set in python 
def intersectionFunc(nums1, nums2):
    ## set in python stores element in unsorted ways, and that's not a problem here.

    ## elements in the result array should be unique 
    set_nums2 = set(nums2)
    result = [elem for elem in nums1 if elem in set_nums2] ## set lookup time is o(1) in python 




## METHOD 02: Two pointers - rem two pointers ke liye we sort the arrays firsthand 
def intersectionFunc(nums1, nums2):

    nums1.sort()
    nums2.sort()

    result = []

    i, j = 0, 0 
    while i <len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1

        elif nums1[i] < nums2[j]:
            i += 1 

        else:
            # nums1[i] == nums2[j]
            ## in case, we get similar elems in nums1 and nums2, we dont directly put it in result
            ## we check if this eleme is already present in result or not - check last elem of res 
            ## also, if result is empty, no need to run to check last elem of result
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])

            i += 1 
            j += 1 

    return result