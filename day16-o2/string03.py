

## ~~~~~~~~~~~~~~~ 01: check if a string is palindrome or not ~~~~~~~~~~~~~~~~~~~~~~~~~


## two pointers 
def checkPali(s): 
    start = 0 
    end = len(s) - 1 

    while start < end:
        if s[start] != s[end]:
            return False 
        elif s[start] == s[end]:
            start +=1 
            end -=1 

    return True 



def checkPaliThodaBetterClean(s): 
    start = 0 
    end = len(s) - 1 

    while start < end:
        if s[start] != s[end]:
            return False 
        # elif s[start] == s[end]:
        start +=1 
        end -=1 

    return True 



## time - o(n)
## space - o(1)



print(checkPali("abab")) ### false 
print(checkPali("abba")) ## true 
print(checkPali("naman")) ## true 



## there is a scope of few extra things to be handled 
## like spaces, punchuations, or any non-alphanumeric chars, then some lower/upper case differences 





## optimised code 
def isPalindrome(s):
    start = 0 
    end = len(s) - 1 

    while start < end:
        while start < end and not s[start].isalnum():
            start +=1 ## start ko tab tak aage inc karte raho jab tak alnum na mile 

        while start < end and not s[end].isalnum():
            end -= 1 

        ## now,compare them- but only in lowercase chars - a and A are not same isliye 
        if s[start].lower() != s[end].lower():
            return False 

        ## agar same hua to dono pointers ko handle kar lo
        start +=1 
        end -= 1 


    return True  



## time - O(n)
## space - o(1)



print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
print(isPalindrome("No lemon, no melon"))              # True
print(isPalindrome("naman"))                           # True
print(isPalindrome("Was it a car or a cat I saw?"))    # True

