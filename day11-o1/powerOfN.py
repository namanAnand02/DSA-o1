## ~~~~~~~~~~~ Pow(x, n) ~~~~~~~~~~~~~~~~~~~


## Leetcode medium : https://leetcode.com/problems/powx-n/description/https://leetcode.com/problems/powx-n/description/


## Input: x = 2.00000, n = 10, Output: 1024.00000

## Input: x = 2.00000, n = -2, Output: 0.25000
## Explanation: 2-2 = 1/22 = 1/4 = 0.25


## Constraints : 
## -100.0 < x < 100.0
## -231 <= n <= 231-1
## n is an integer.
## Either x is not zero or n > 0.
## -104 <= xn <= 104



def myPow(x, n):

    ## do it using d n c 

    ## base case 
    if n == 0:
        return 1 
    if n == 1:
        return x 

    if n < 0: ## 2 ^ (-3) === 1/ 2^3
        x = 1 / x  
        n = -n

    mid = n // 2 
    result = myPow(x, mid)
    finalResult = result * result 

    if n % 2 == 0 :
        return finalResult 
    elif n % 2 == 1:
        return x * finalResult 
    


print(myPow(2.0000, -2)) ## 0.25

## time - o(logn)

## space - o(logn) 


## Divide and conquer - 
# ## time : O(log n -base 2)
# ## space : O(log n - base 2 ) 

## 2 ^ 64 - in this case, we are going 8 levels down - so that many times we are storing it into stack - log base 2 ^ 64