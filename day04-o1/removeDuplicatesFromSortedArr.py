## ~~~~~~~~~~~ Remove duplicates from a sorted array ~~~~~~~~~~~

## Method 01: Brute force - Using Set 


def removeDupli(arr):
    set_arr = set(arr)
    return set_arr, len(set_arr)

## Time: O(n) - inserting all elements into set takes n*O(1)
## space: O(n) - set creation 


## Method 02: Optimal - TWO pointers approach 

def removeDupli2(arr):
    i = 0 
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]

    return i + 1, arr


print(removeDupli2([1,1,2,2,3,3,4,4,5]))
## (5, [1, 2, 3, 4, 5, 3, 2, 4, 1])


## time: o(n)
# space: O(1)






