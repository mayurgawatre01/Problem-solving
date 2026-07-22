def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j 
    
           
print(two_sum([2,3,4,5,7,6],9))
            
#better
def better(arr,target):
    nums=sorted(arr)
    
    left=0
    right=len(arr)-1
    
    while left < right:
        total=nums[left]+nums[right]
        if target==total:
            return nums[left],nums[right]
        elif target <total :
            right-=1
        else:
            left+=1
print(better([1,2,3,4,5,6,7],9))
#hashing optimal solution 

