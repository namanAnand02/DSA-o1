## ~~~~~~~ Maximum consecutive sequence ~~~~~~~~~~~ 

## Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

## Constraints:

## Time Complexity must be O(n) for optimal.

## Elements are distinct (in most variants).



## Input: [100, 4, 200, 1, 3, 2]
## Output: 4
## Explanation: The longest consecutive sequence is [1, 2, 3, 4]



## ~~~~~~~~~~~ 



## BRUTE FORCE approach 

## --> Check for every number x if x+1, x+2... exist in the array.


# def longestConsecutiveSequence(nums):
#     maxLen = 0 
#     ## for each element in nums, run an another loop to search if it's consecutive one's exist or not 
#     for num in nums:
#         currentElem = num 
#         curLen = 1 
#         ## run while loop as long as its consecutive elem is present and keep updating the current length of the sequence.
#         while currentElem + 1 in nums:
#             curLen += 1 ## update the current sequence length 
#             currentElem += 1 

#         ## after the above while loop ends, meaning no more consecutive elem for that elem - we update the max length of such sequence. 
#         maxLen = max(maxLen, curLen)

#     return maxLen 


# ## TIME - o(N^2) - one for loop and one while in loop 

# print(longestConsecutiveSequence([100,4,200,1,3,2])) ## 4





## ~~~~~~~~~ 

## Method 02 : sort and scan
# def func2(nums):
#     maxLen = 0 
#     nums.sort() ## sort the array 
#     currentLength = 1 
#     for i in range(1,len(nums)): ## start from index 1 as we have to compare each elem with its prev elem as after sorting prev and curr elem should be consecutive one's if there is any
#         if nums[i] == nums[i - 1 ]: ## if curr and prev elem are same, we skip this and move 
#             continue 
#         elif nums[i] == nums[i -1] + 1 : ## if curr = prev elem +1 , i.e it is a part of the consecutive seq elem of prev 
#             ## so we increase currLength of sequence by 1
#             currentLength += 1

#         else:   ## else, if there is no sequence, we again make CurrLen =1 ,i .e we start looking for new seq from here.
#             currentLength = 1 

#         ## at the end, we keep updating the maxLen of seq 
#         maxLen = max(maxLen, currentLength)

#     return maxLen 



# print(func2([100,1,300,2,4,3])) ## 4 





## ~~~~~~~~~~~~~~~~~~~~~


## Method 03 : Optimal solution 

## -> using SET and Check start of the sequence 


def findLongestConsecutiveSequence(nums):
    maxLen = 0 
    ## we convert the arr into a set so that lookup is easy - set lookup time is o(1)
    setNums = set(nums)

    ## we keep traversing through the arr and try to find out the start value of all possible sequences 

    for num in nums:
        if (num - 1) not in setNums:
            curLen = 0
            ## that means this num is a start value, a seq can be possible from here
            ## so, we run a while loop to keep checking how many of its consecutive elem are present in arr 

            while (num + curLen) in setNums:
                ## We're using num + curLen inside the while loop — that's a nice way to avoid modifying num directly.

                curLen += 1 

            maxLen = max(maxLen, curLen)


    return maxLen 

## Time - o(n)
## Space - o(n) for set 

print(findLongestConsecutiveSequence([100,3,101,2,1,4]))


        
