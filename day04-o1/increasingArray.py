
## ~~~~~~~ Increasing Array : CSES ques 4 ~~~~~~~~~~~~~

## You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.

## On each move, you may increase the value of any element by one. What is the minimum number of moves required?
## Input:
## The first input line contains an integer n: the size of the array.
## Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.


## Output:
## Print the minimum number of moves.
## Constraints

## 1 <= n <=2 * 10^5
## 1 <=x_i <= 10^9

## Example
## Input:
# 5
# 3 2 5 1 7

# Output:
# 5


## a classic greedy algorithm problem. 
## current eklem should be atlease similar or greater than the previous element. 
## In order to achieve that, how many steps are required? 

## --> we traverse through the array, at each ith index, if arr[i] < arr[i-1], we calculate the gap and that's the total move required to make it atlease equal to its previous element. 
## afterwards we also make it updated, similar to the element at the i-1.


def increasingArray(arr):
    moves = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i -1 ]:
            moves += arr[i-1] - arr[i] ## find the gap 
            arr[i] = arr[i -1 ] ## update the value 

    return moves 

print(increasingArray([3,2,5,1,7])) ## 5

## time: o(n)
## space: O(1)