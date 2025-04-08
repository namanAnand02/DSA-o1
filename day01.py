## ~~~~~~~~~~~~~ 1. Reverse the array ~~~~~~~~~~~~~~~~~

## Function definition 

## method 00: SLICING 

# def reverse(arr):
#     return arr[::-1]

## Time : O(n) : acts as a loop only 
## space: O(1) : no extra space is used


## NOTE: if we had used another list, it would have become o(n) space complexity 

# list 2 = list1[::-1]
# list2 

## in above case, space is o(n)


## method 01 : Negative indexing 
#  
# def reverse(arr):
#     resultArr  = []
#     for i in range(len(arr)- 1, -1, -1 ):
#         resultArr.append(arr[i])

#     return resultArr

## time complexity : o(n) : linear time complexity 
## space complexity : o(n) : n sized array was used
 


## Method 02: TWO POINTERS 

# def reverse(arr):
#     ## two pointers approach 
#     i = 0 
#     j = len(arr) - 1 
#     while i <= j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i+=1 
#         j-= 1 
#     return arr 



# ## driver code
# arr = [11,12,13,14,15,100,133]
# result = reverse(arr)
# print(result)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



## ~~~~~~~~~ 2. segregate the even and odd elements ~~~~~~~~


## method 01: 

# def func(arr):
#     even = []
#     odd = []
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             even.append(arr[i])
#         else:
#             odd.append(arr[i])

#     return even + odd 




## Method 02 : 

# def func(arr):
#     ans = [] ## this extra space causes us space complexity of o(n)
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             ans.append(arr[i])

#     for i in range(len(arr)):
#         if arr[i]% 2 != 0:
#             ans.append(arr[i])


#     return ans 


## time complexity : o(n)
## space complexity : O(n)




## method 03 : Two pointers  

# def func(arr):
#     i = 0 
#     j = len(arr) - 1  
#     while i < j:
#         if arr[i] % 2 == 0:
#             i += 1 
#         # else:
#         #     if arr[j] % 2 == 0:
#         #         arr[i], arr[j] = arr[j], arr[i]
#         #         i += 1 
#         #         j -= 1 

#         #     else:
#         #         j -= 1

#         elif arr[j] % 2 != 0:
#             j -= 1 

#         else:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1 
#             j -= 1 
    
#     return arr 


# print(func([7,2,9,4,6,1,3,8,5]))




# ## method 04: Two pointers from front 
# def segre(arr):
#     i = -1 
#     j= 0 
#     while j < len(arr): 
#         ## if jth elem is odd, kuch nhi karo, move forward and find out the even elem 
#         ## if jth elem is even, firstly increase i by 1 and then put that elem on ith pos.
#         ## i only bothers about even elements 

#         if arr[j]% 2 == 0:
#             i += 1 
#             arr[i], arr[j] = arr[j], arr[i]

#             j += 1
#         else:
#             j += 1 

#     return arr  


# ## time complexity : O(n) as we traverse through all elem atleast for once. 
# ## space complexity: O(1) as there is no extra space used in this case




# print(segre([7,2,9,4,6,1,3,8,5]))


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





## NEXT LECTURE 


## ~~~~~~~~~~~~ TWO SUM 2 : Input array is sorted - leetcode 167 ~~~~~~~~~~~~~~~~


# def func(arr, k):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] + arr[j] == k:
#                 return [i, j]
            
#     return [-1,-1]

## time complexity : O(n^2)
## space complexity : o(1)


## HASHMAP approach 

# def func(arr, k):
#     hashMap = {}
#     for i in range(len(arr)):
#         if k - arr[i] in hashMap:
#             return [hashMap[k- arr[i]], i]
        
        
#         hashMap[arr[i]] = i 
#         # print(hashMap)


#     return [-1,-1]


## hashmap - enumerate 
# def func(arr, k):
#     hashMap = {}
#     for index, val in enumerate(arr):
#         if k - val in hashMap:
#             return [hashMap[k-val], index]
        
#         hashMap[val] = index 


#     return [-1,-1]

        
## time - o(n) and space : O(n)




## INPUT SORTED ARRAY - use two pointers 

# def func(arr, k):
#     i = 0 
#     j = len(arr) - 1 
#     while i <= j:
#         if arr[i] + arr[j] == k:
#             return [i,j]
        
#         elif arr[i] + arr[j] <k:
#             i +=  1 

#         else:
#             j -= 1 

#     return [-1,-1]

## time complexity: o(n)
## space complexity : o(1)



# print(func([2,3.5,5,6,7,9], 9))

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





## ROTATE ARRAY  


## brute force approach 
 
# def rotate(arr, k):
#     for i in range(0, k):
#         elem = arr[-1]

#         for j in range(len(arr)):
#             arr[j], elem = elem, arr[j]

#     return arr 




## optimised approach: reverse helper function 

# def func(arr,k ):

#     k %= len(arr)
#     def reverse(start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]

#             start += 1 
#             end -= 1

        
#     reverse(0, len(arr)- 1) ## reverse the whole arr 
#     reverse(0, k- 1 )       ## reverse the first k elem 
#     reverse(k, len(arr)- 1 ) ## reverse the rest 
    

#     return arr 


# def reverse(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1 
#         end -= 1 

    
# def func(arr, k):
#     k %= len(arr)
#     reverse(arr, 0, len(arr)- 1 )
#     reverse(arr, 0, k- 1 )
#     reverse(arr, k, len(arr)- 1 )

#     return arr

# print(func([1,2,3,4,5,6,7], 3))

## time complexity : o(n)
## space complexity : o(1)

## in place rotation 




## in the ques itself, it has been specified to not return anything, so we wont do that. 
## also, we can check that from the given snippet - NONE mentioned over there. 
## if there specifed NONE, we dont need to return anything, and that we should avoid return statement at the end. 



## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




## ~~~~~~~~~~~~~~~~~~ REMOVE ELEMENT - leetcode 27 ~~~~~~~~~~~~~~~


## brute force approach 

# def func(arr, k):
#     ans = []
#     for i in range(len(arr)):
#         if arr[i] != k:
#             ans.append(arr[i])

#     return ans 

## UsiNg LiSt COmpreHEnsion 

# def func(arr, k):
#     return [arr[i] for i in range(len(arr)) if arr[i]!= k ]


# def func(arr, k):
#     return [x for x in arr if x!= k ]

## time complexity: o(n)
## space complexity: O(n) as it creates a new list  



## optimised approach: two pointers 

# def func(arr, k):
#     write_index= 0 
#     for i in range(len(arr)):
#         if arr[i] != k:
#             arr[write_index] = arr[i]
#             write_index += 1 

#     return write_index, arr


## or  

# def func(arr, k):
#     x = -1 
#     for i in range(len(arr)):
#         if arr[i] != k:
#             x += 1
#             arr[x] = arr[i]

#     return x + 1, arr 

## time complexity: O(n)
## space complexity : O(1)


# print(func([2,3,3,2,3,2], 3))

# arr = [3,2,2,3] 
# print(func(arr, 3))


## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

