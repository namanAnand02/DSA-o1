##~~~~~~~~~~~~~~~  even indexed words into upper ~~~~~~~~~~~~~~~~~

## NOTE: strings are immutable in python, so we must not do chnages in-string. always take the help of other datastructure
## convert string into other DS 
## do thr modifications in that DS 
## finally, convert from that DS back to strings using " ".join(DS)


def evenIndexWordToUpper(str):
    li = str.split(" ")

    for i in range(len(li)):
        if i % 2 == 0:
            li[i]= li[i].upper()
            

    return " ".join(li)


print(evenIndexWordToUpper("a ab abc abcd abcde abcdef abcdefg"))


## time - o(n)
## space - o(n)


## ~~~~~~~~~~~ reverse the complete sentence ~~~~~~~~~~~~~

def reverseTheSentence(str):
    li = str.split(" ")

    i, j = 0 , len(li) - 1 

    while i <= j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -=1 

    return " ".join(li) 


print(reverseTheSentence("a ab abc abcd abcde"))
## abcde abcd abc ab a


## time - o(n)
## space - o(n)



## ~~~~~~~~~~~ Even indexed words REVERSAL ~~~~~~~~~~~~~~~~~~~~~

## NOTE: strings are immutable in python, so we must not do chnages in-string. always take the help of other datastructure
## convert string into other DS 
## do thr modifications in that DS 
## finally, convert from that DS back to strings using " ".join(DS)




## str = "a ab abc abcd x xy xyz"

## o/p:  a ab cba abcd x xy zyx


def evenIndxReversal(str):
    li = str.split(" ")
    for i in range(len(li)):
        if i % 2 == 0: 
            li[i] = li[i][::-1]
        
    return " ".join(li)



print(evenIndxReversal("a ab abc abcd x xy xyz"))
## a ab cba abcd x xy zyx


## time - o(n)
## space - o(n)


## ~~~~~~~~~~~ odd index words reversal in a sentence ~~~~~~~~~~~~~

def oddIndxReversal(str):
    li = str.split(" ")
    for i in range(len(li)):
        if i % 2 == 1: 
            li[i] = li[i][::-1]
        
    return " ".join(li)


print(oddIndxReversal("a ab abc abcd x xy xyz"))
## a ba abc dcba x yx xyz

## time - o(n)
## space - o(n)






##~~~~~~~~~~~~~~  reverse individual words in sentence ~~~~~~~~~~~~~~~

## NOTE: strings are immutable in python, so we must not do chnages in-string. always take the help of other datastructure
## convert string into other DS 
## do thr modifications in that DS 
## finally, convert from that DS back to strings using " ".join(DS)




def reverseIndividualWords(str):
    li = str.split(" ")

    for i in range(len(li)):
        li[i] = li[i][::-1]

    return " ".join(li)

print(reverseIndividualWords("a ab abc abcd x xy xyz"))
## a ba cba dcba x yx zyx




## OR // 




def helper(s):
    ## li = s.split(" ") ## wrong way - use it only to split the sentence into words
    li = list(s) ### "abc" ---> ["a", "b", "c"]
    i, j = 0, len(li) -1 
    while i<=j:
        li[i], li[j] = li[j], li[i]

        i +=1 
        j -=1  

    return "".join(li)



def rev2(str):
    li = str.split(" ")

    for i in range(len(li)):
        li[i] = helper(li[i])

    return " ".join(li) 


print(rev2("a ab abc abcd x xy xyz")) ## a ba cba dcba x yx zyx



## NOTE: must know the difference between when to use split() and list(str)

## sentence.split("delimeter") - use when want to split a sentence into words - they gets splitted and stored in the form of list. 
## list(str) --> use it when want to convert string words into characters - they gets splittted and stored in the form of list 




## ~~~~~~~~~~~~ Title method of string ~~~~~~~~~~~~~~~~~~~

## capitalize the first char of each word in the string 

def titleStr(s):
    li = s.split()

    ## for i in li:
    ##     i = i[0].upper() + i[1:].lower()
    ## the above thinggy wont work as it saves reference and not the original
    ## and we are doing the modificatiosn to the referenced i 

    ## so use range(len(li)) 
    
    for i in range(len(li)):
        li[i] = li[i][0].upper() + li[i][1:].lower()

    return " ".join(li)



print(titleStr("python Hello world demon")) ## Python Hello World Demon

## time - o(n)
## space - o(n)




## ~~~~~~~~~~~ convert first and last character of each word into upper in a sentence ~~~~~~~~~~~

## sentence = "python hello world demon Hitler"

## o/p : "PythoN HellO WorlD DemoN HitleR"


def func(s):
    li = s.split(" ")

    for i in range(len(li)):
        li[i] = li[i][0].upper() + li[i][1:len(li[i])-1].lower() + li[i][-1].upper()
        # li[i] = li[i][0].upper() + li[i][1:-1].lower() + li[i][-1].upper()


    return " ".join(li)


print(func("python hello world demon Hitler")) ## PythoN HellO WorlD DemoN HitleR


## the above code has a bug - in case of only one char in any word, it will add two chars in the output. 
## to avoid that, we have to explicitly handle such cases when the length of a particular word is 1. 

def func(s):
    li = s.split(" ")

    for i in range(len(li)):

        if len(li[i]) != 1:
            li[i] = li[i][0].upper() + li[i][1:len(li[i])-1].lower() + li[i][-1].upper()
            # li[i] = li[i][0].upper() + li[i][1:-1].lower() + li[i][-1].upper()

        else:
            li[i] = li[i].upper()


    return " ".join(li)


print(func("python hello world demon Hitler")) ## PythoN HellO WorlD DemoN HitleR

print(func("a ab abc abcd x xy xyz"))

## time - o(n)
## space - o(n)

