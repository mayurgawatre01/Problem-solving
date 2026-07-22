def move_zeros(arr):
    arr1=[]
    arr2=[]
    for num in arr:
        if num!=0:
            arr1.append(num)
        else:
            arr2.append(num)
    return arr1+arr2
print(move_zeros([0,1,0,3,12]))
    
        
        
#optimzed

def mov_zeros(nums):
    i=0
    j=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums
print(mov_zeros([0,1,0,3,12,0]))