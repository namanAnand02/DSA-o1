

## ~~~~~~~~~~ IMP QUES: 01. Reverse vowels of a string ~~~~~~~~~~~~~~~~~


## str = "namesh" 
## o/p : "nemash" - e and a replaces their place 


def reverseVowels(s):
    ## since string is immutable in python, meaning we cant directly make changes to the string

    li = list(s) ## s = "namesn", li = ["n","a","m","e","s","h"]
    ## use 2 pointers - from left and right - if both side vowels, swap 

    i = 0
    j = len(li) - 1 

    while i < j:
        if li[i] not in "aeiouAEIOU":
            i += 1 
        elif li[j] not in "aeiouAEIOU":
            j -= 1 

        else:
            ## both li[i] and li[j] are vowels 
            ## swap them 
            li[i], li[j] = li[j], li[i]
            i += 1 
            j -= 1 

    return "".join(li)


print(reverseVowels("namesh"))  ## nemash

## time - o(n)
## space - O(n)



## NOTE - this code can be slightly optimised - if we use set for vowels lookups 

## we store all 10 vowels chars in a set - and each time we have to check whether a char is vowel or not - we just check in set - 
## lookup time in set - o(1) - just thoda better ho jayega - but overall time and space complexity remains same 



def reverseVowels(s):
    ## since string is immutable in python, meaning we cant directly make changes to the string

    li = list(s) ## s = "namesn", li = ["n","a","m","e","s","h"]
    ## use 2 pointers - from left and right - if both side vowels, swap 

    i = 0
    j = len(li) - 1 

    vowelsSet = set("aeiouAEIOU")

    while i < j:
        if li[i] not in vowelsSet:
            i += 1 
        elif li[j] not in vowelsSet:
            j -= 1 

        else:
            ## both li[i] and li[j] are vowels 
            ## swap them 
            li[i], li[j] = li[j], li[i]
            i += 1 
            j -= 1 

    return "".join(li)


print(reverseVowels("mukesh"))  ## mekush 

## time - o(n)
## space - O(n)



## ~~~~~~~~~~ 02: Find the middle char(s) from the string ~~~~~~~~~~~~~~~


def middleChar(s):
    if len(s) % 2 != 0:
        return s[len(s)//2]
    
    else:
        return s[len(s)//2 -1 : len(s)//2 + 1]
    

# print(middleChar("a")) ## a
# print(middleChar("ab")) ## ab
# print(middleChar("abc")) ## b
# print(middleChar("abcd")) ## bc
# print(middleChar("abcde")) ## c 
# print(middleChar("abcdef")) ## cd 


## time - o(1)
## space - o(1)



## ~~~~~~~~~~~~ 03: Sort the string i.e chars in the string ~~~~~~~~~~~

## ex: bacd ---> abcd 


def sortTheString(s):
    li = list(s) ## kyuki yaha ek hi word hoga string ka, so no meaning using split()

    li.sort()
    return "".join(li)


print(sortTheString("bacdfeh")) ## abcdefh

## list(s) -- time = o(n)
## li.sort() -- time = O(nlogn), tim sort algo 
## "".join(li) -- time = o(n) 

## therefore total time = most expensive = O(nlogn)


## space - o(n) : convert the string into list



## ~~~~~~~~~~ 04: sort the names ~~~~~~~~~~~~~~~ 

# def sortStr(l):
#     l.sort()

# l = ["ijk", "xyz", "pqrs", "mno"]
# sortStr(l)
# print(l) ## ['ijk', 'mno', 'pqrs', 'xyz'] sorted data


## to sort the data in descendingg order

## use l.sort(reverse = True)






## ~~~~~~~~~~~~~~~~~~ 05. remove duplicates character ~~~~~~~~~~~

def removeDupliChars(s):
    # li = list(s)
    hashMap = {}
    for i in s:
        if i not in hashMap:
            hashMap[i] = 1 


    return "".join(hashMap.keys()) ## get the unique chars stored as keys and join them
        

print(removeDupliChars("naman")) ## nam
print(removeDupliChars("abcaba")) ## abc 



## NOTE: its better to use hashMap or set to store the unique chars rather than lists 
## The list-based approach has worse performance due to the O(n) lookup time in the list for each character

## For strings where you need to track unique characters, hashMap is optimal as it allows O(1) average-time insertions and lookups, 
## whereas using a list results in inefficient O(n) searches for duplicates, making overall time as o(n^2)  - This is because for each character, "i not in result" takes O(n) time


## The loop to check whether a character is in the dictionary (if i not in hashMap) takes O(1) time on average, and inserting keys into the dictionary also takes O(1) time on average.



## lookup time in hashmap and hashsets are o(1) - so always choose this over list 

## time - using hashMap - o(n)
## time - using list - o(n^2)

## space - in both cases - o(k)

 

