def rotated(nums,d):
    d=d%n
    n=len(nums)
    temp=[1,2,3]
    for i in range(3,len(nums)-1):
        nums[i]=nums[i-d]
    #for temory
    for i in range(n-d,len(nums)-1):
        nums[i]=nums[i-(n-d)]
    for i in range()        
        
print(rotated([1,2,3,4,5,6,7],2))