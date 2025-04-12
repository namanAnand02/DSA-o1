## You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

## Merge nums1 and nums2 into a single array sorted in non-decreasing order.

## The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


## Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
## Output: [1,2,2,3,5,6]
## Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
## The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.



def merge(nums1, m, n, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """


    ## rem: num1 has only m real values, rest are the spaces left for accomodating rest elem 
    ## nums2 has n elem 
    ## therefore when we assign last at the very last index of nums1, last = m + n - 1 
    ## nums1 = [1,2,3,0,0,0] and nums2 = [2,5,6]
    ## we initialise last at end of nums1 - whose index value would be m+ n -1 


    ## method 02 : optimal approach - 3 pointers - merge in rev order 
    last = m + n -1 
    ## start the merge in rev orderr and hence loop until m, n == 0
    while m > 0 and n > 0:
        if nums1[m -1 ] < nums2[n -1 ]:
            ## 0-indexed : so if m = 3, then the last valid element in nums1 is at index 2, not 3
            nums1[last] = nums2[n -1 ]
            n -= 1 
        else: 
            ## when nums1[m] >= nums2[n]:
            nums1[last] = nums1[m -1]
            m -= 1

        ## regardless of which array elem gets filled next, as soon as any new elem gets assigned its correct place, we always update last pointer 
        last -= 1 

    ## an imp edge case we need to handle 
    ## if at last, only smaller elems left are of nums1,  no worries as they are already at correct place. 
    ## only if smaller elems left are from nums2, we need to bring all of them into nums1 - nums2 is also already sorted, so no extra tension.

    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n -1, last - 1 


    




        ## ~~~~~~~~~~~~~~ 


def merge1(nums1, m, n, nums2):
    # Method 01 : brute force - still good approach just extra space has been used 


    i =0 
    j = 0 
    result = [] ## a temporary list same as length of nums1 - we will store merged list into this and at last will copy its elem to nums1 by overriding.

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i +=1 

        elif nums1[i] > nums2[j]:
            result.append(nums2[j])
            j += 1 

    ## when either of the arrays gets over 
    while i < m:
        result.append(nums1[i])
        i +=1 

    while j < n:
        result.append(nums2[j])
        j += 1 

    ## run a loop to copy all elems from result into nums1, as ques expects merged list into nums1 only.
    for i in range(len(result)):
        nums1[i] = result[i]

        ## time - o(n), space - o(n)
