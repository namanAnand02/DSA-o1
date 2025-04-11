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