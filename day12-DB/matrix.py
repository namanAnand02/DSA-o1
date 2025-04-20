# ## ~~~~~~~~~ Matrices ~~~~~~~~~~~~~~~~~~

# ## read and write matrix elements 

# m = int(input("enter the number of rows: "))
# n = int(input("enter the number of columns: "))
# arr = []

# for i in range(m):
#     tempL = [int(i) for i in input().split()]
#     arr.append(tempL)

# print(arr)

# ## enter the number of rows: 3
# ## enter the number of columns: 3
# ## 1 2 3
# ## 4 5 6 
# ## 7 8 9
# ## [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# ## print them in the form of matrix 

# for i in range(m):
#     for j in range(n):
#         print(arr[i][j], end= " ")
#     print()

# 1 2 3
# 4 5 6
# 7 8 9


## in function form : 


## ~~~~~~~~~~~~~~~~~~~~~~~ 1. read and write matrix ~~~~~~~~~~~~~~~~




# def read(arr, m, n):
#     for i in range(m):
#         tempL = [int(i) for i in input().split()]
#         arr.append(tempL)

#     print(arr)



# def printM(arr, m, n):
#     for i in range(m):
#         for j in range(n):
#             print(arr[i][j], end= " ")
#         print()

# m = int(input("enter the no of rows: "))
# n = int(input("enter the no of cols: "))
# arr = []


# read(arr, m, n)
# printM(arr, m, n)



## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




## ~~~~~~~ 2. sum of all elements in the matrix ~~~~~~~~~~~~~~

def sumOfAllElements(arr, m,n):
    ## m = rows no 
    ## n = cols no 

    ## for m,n = 3,3 - arr = [[1,2,3], [4,5,6], [7,8,9]]
    ## arr[0] = [1,2,3]
    ## arr[1] = [4,5,6]
    ## arr[2] = [7,8,9]

    ## sum(arr[0]) = 6 
    ## sum(arr[1]) = 15 
    ## sum(arr[2]) = 24 

    ## finalSum = 6 + 15 + 24 = 45 

    sumV = 0 
    for i in range(m):
        sumV += sum(arr[i])
        


    return sumV


m = int(input("enter the no of rows: "))
n = int(input("enter the no of cols: "))
arr = []
for i in range(m):
    ## arr += [int(i) for i in input().split()] ## WRONG  ## only enter inputs n times that too space separated 

    arr.append([int(i) for i in input().split()]) ##This ensures we're appending a list (a row) into your 2D matrix.



print(sumOfAllElements(arr, m, n)) ## 45 



