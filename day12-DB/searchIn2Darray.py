## ~~~~~~~~~~~ Search in 2D array ~~~~~~~~~~~~~~

## Leetcode 74: medium : https://leetcode.com/problems/search-a-2d-matrix/description/ 


## You are given an m x n integer matrix matrix with the following two properties:

## Each row is sorted in non-decreasing order.
## The first integer of each row is greater than the last integer of the previous row.
## Given an integer target, return true if target is in matrix or false otherwise.

## You must write a solution in O(log(m * n)) time complexity.



def searchMatrix(matrix, target):
    m = len(matrix) ## num of rows
    n = len(matrix[0]) ## num of columns
    
    ## lets implement BS on it to search for the target 

    start = 0 
    end = m * n -1 

    while start <= end:
        mid = start + (end - start) // 2 
        ## map this mid index to row and cols index of the elem in 2D arr

        row_idx = mid // n 
        cols_idx = mid % n 

        midElement = matrix[row_idx][cols_idx]

        if midElement == target:
            return True 
        elif midElement < target:
            start = mid +1  
        else:
            end = mid -1 

    return False

## time - o(log m * n)
## space - o(1)
