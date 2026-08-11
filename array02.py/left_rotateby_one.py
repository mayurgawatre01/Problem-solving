def left(nums):
    last=nums[0]
    for i in range(0,len(nums)-1):
        nums[i]=nums[i+1]
    nums[4]=last    
    return nums
print(left([1,2,3,4,5]))