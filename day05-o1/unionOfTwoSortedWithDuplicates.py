## ~~~~~~~~ Union of two sorted arrays with duplicates ~~~~~~~~~~~
## GFG - medium - https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1


## Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

## Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.


## Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
## Output: 1 2 3 4 5 6 7
## Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.



    
#Function to return a list containing the union of the two arrays.
def findUnion(a,b):
    # code here 
    
    ## METHOD 03 : Optimal solution using TWO pointers 
    n1 = len(a)
    n2 = len(b)
    i, j = 0, 0 
    unionArr = []
    while (i < n1 and j < n2):
        ## compare a[ith] elem and b[jth] elem
        ## whichever is smol and not present in unionArr, put it there and increase that variable 
        if (a[i] <= b[j]):
            ## meaning we should put a[i] next but first ensure it is not present in unionArr already
            # if a[i] not in unionArr: ## dont do this, it takes o(n) time 
            #     unionArr.append(a[i])
            
            ## Regardless of whether a[i] already presnt in union or not 
            ## once we are sure a[i]th elem is smaller and it was his turn to send elem into unionArr
            ## we increase i by 1, whether it got shifted into union arr or not 
                
            ## or --> this is better - o(1)
            if not unionArr or  unionArr[-1] != a[i]:
                ## if unionArr is empty, put a[i] in it anyway 
                ## if unionArr is not empty, compare last element first 
                unionArr.append(a[i])
            
            i += 1 
            
        else: ## when b[j] < a[i], again first we check whether last elem in unionArr is not same as b[j]
            
            if not unionArr or  unionArr[-1] != b[j]:
                unionArr.append(b[j])

            
            j += 1 
            
            
            
    ## next we handle the cases when either of the two arrays are over 
    while i < n1:
        if not unionArr or unionArr[-1] != a[i]:
            unionArr.append(a[i])
            
        i +=1 
        
    while j < n2:
        if not unionArr or unionArr[-1] != b[j]:
            unionArr.append(b[j])
            
        j += 1 
            
            
    return unionArr
                
                
    ## Time - o(n1 + n2)
    ## space - o(n1 + n2)
        
        
        
        




## ~~~~~~~~~~~~
    
## METHOD 01: Brute force 
def findUnion2(a, b):
    finalList = a + b # combine both lists - o(n1 + n2)
    set1 = set(finalList) ## remove duplicates - o(n1 + n2)
    arr = sorted(list(set1)) ## sort the unique elements - o(k logk)

    return arr
    

## total time: O(n1 + n2 + klogk)
## space - o(k)

## this approach is better for unsorted arrays 
## but if the arrays are already sorted, best approach would be to use two Pointers

## two pointers approach - time: O(n1 + n2), space; O(1)
    
## ~~~~~~~~~~~~~~~~
    
## METHOD 02: 
    
def findUnion3(a,b):
    set1 = set()
    for i in a:
        set1.add(i)
    for i in b:
        set1.add(i)
        
    return sorted(list(set1))
    
    
# ## it expects us to return the union of the array in sorted order.
# ## but set in python stores elements in unordered manner.
# ## and hence we need to sort at last before returning the union.