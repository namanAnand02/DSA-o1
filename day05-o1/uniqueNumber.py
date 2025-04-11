## ~~~~~~~~~~~~~~~ UNIQUE NUMBER ~~~~~~~~~ 
## Every number appears twice except for one element, find that unique element. 


## method 01 : use hashSet or hashMap


## method 02 : use XOR 

def uniqueNumber(arr):
    xor1 = 0 
    for i in arr:
        xor1 ^= i 
    return xor1 


print(uniqueNumber([1,1,2,2,3,4,4])) ## 3 