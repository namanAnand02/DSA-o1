## ~~~~~~ Floor of an element in sorted array ~~~~~~~~~~~~~

## 5.6 - ceil = 6  and floor = 5 

## arr = [1,2,3,4,8,10,10,20,30], target = 5 
## o/p - 4 


def findFloor(nums, target):
    start = 0 
    end = len(nums) -1 
    while start <= end:
        mid = start + (end - start )// 2

        if nums[mid] == target:
            return nums[mid] 
        elif nums[mid] >target:
            end = mid -1 
        else:
            ## nums[mid] < target: potential ans and then move right 
            ans = nums[mid] 
            start = mid +1 

    return ans 

print(findFloor([1,2,3,4,8,10,10,20,30], 11))  ## 10
                       