def sorted_array(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                return False
    return True
print(sorted_array([1,3,4,5]))


#optimal

def sorted_opti(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(sorted_opti([3,4,5,6,7,8]))



def striver(nums):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return False
    return True
print(striver([1,1,2,3]))
            