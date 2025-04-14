## ~~~~~~~~~~~~ Boats to save people ~~~~~~~~~~~~~


## Leetcode Medium - https://leetcode.com/problems/boats-to-save-people/description/

## You're given:

## An array people[] of weights.

## Each boat can carry at most 2 people, and their combined weight ≤ limit.

## Goal: minimize the number of boats used




## ---> Greedy + Two pointers
def minBoats(people, limit):
    count = 0 
    start = 0 
    end = len(people) -1 

    while start <=end :
        ## one light weight + one heavy person as pair boards the boat 
        if people[start] + people[end] <= limit:
            count += 1 
            start +=1 
            end -= 1 

        else:
            ## when only heaviest person boards the boat
            count += 1
            end -= 1 

    return count 


## Time = o(n)
## space - O(1)


print(minBoats([1,2], 3)) ## 1
print(minBoats([3,2,2,1], 3)) ## 4





## NOTE: Why can't we use SLIDING WINDOW? 

## sliding window is useful when we are dealing with contiguous subarrays 
## or we deal with a fixed or variable length subarrays 
## But here, we are not looking at contiguous subarrays 
## Pairing can be made from anywhere in the array (and not just neighours)

## NOTE: why can't we use PREFIX SUM concept here?

## Prefix sum helps when we are calc sum of elems in a range quickly.
## or checking how many times a certain sum appears (usually with hashmaps)
 

## Don’t use sliding window or prefix sum when you don’t care about subarrays or range sums.

## Use greedy + two pointers when:

## ---> We can sort.

## ---> We're making pairing decisions based on the extreme values.






## Brute force approach 


## Try all possible pair combinations of people to see if they can go together.

## If two people can be paired (i.e., their combined weight ≤ limit), mark them as "used".

## For each person, try to pair them with someone else, or send them alone if no pair is possible.



def numRescueBoats_brute(people, limit):
    n = len(people)
    visited = [False] * n
    boats = 0

    for i in range(n):
        if visited[i]:
            continue
        
        found_pair = False
        for j in range(i + 1, n):
            if not visited[j] and people[i] + people[j] <= limit:
                visited[i] = visited[j] = True
                boats += 1
                found_pair = True
                break
        
        if not found_pair:
            visited[i] = True
            boats += 1

    return boats



## time - o(n^ 2)
## space - o(n)