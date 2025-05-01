##~~~~~~~~~~~~~~~  even indexed words into upper ~~~~~~~~~~~~~~~~~



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



