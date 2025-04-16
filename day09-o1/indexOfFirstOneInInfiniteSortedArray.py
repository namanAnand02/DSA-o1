## ~~~~~~~~~ Index of first 1 in infinite binary sorted array ~~~~~~~~~~~~~~

## https://www.naukri.com/code360/problems/search-in-infinite-sorted-0-1-array_696193?leftPanelTabValue=PROBLEM



## You are given an infinite array consisting of only ones and zeroes, in sorted order. You have to find the index of the first occurrence of 1.

## Example:
## If the array is 0 0 0 0 1 1 1 1… then, the first occurrence of 1 will be at index 4 therefore the answer here is 4.



'''

    def get(i):
    
        Use the given get function which is given as an argument here, 
        that returns the value at index i
        in the infinite sorted binary array.

'''


    


def firstOne(get):
    
    # Write your code here.
    # This function returns the first index of the occurence of 1
    ## lets first find range in which 1 lies 

    def BS(start, end, target):
        while start <=end:
            mid = start + (end - start) // 2 
            if get(mid) == 1:
                ans = mid 
                end = mid -1 
                
            else:
                start = mid +1 

        return ans 

    ## first find out the range in which 1 can be found 
    ## then we'll apply BS on that range to find the first 1 
    start = 0 
    end = 1 
    while get(end) < 1 :
        start = end 
        end = end* 2 
    
    return BS(start, end, 1)