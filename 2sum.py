nums = [3, 4, 5, 6, 7, 9, 10]
target=12

left=0
right=len(nums)-1

while left < right:
    current_sum=nums[left]+nums[right]
    if current_sum==target:
        print(nums[left],nums[right])
        left+=1
        right-=1
    elif current_sum<target:
        left+=1
        
    else:
        right-=1
        
        