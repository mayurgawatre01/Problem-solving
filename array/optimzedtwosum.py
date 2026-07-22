def opti_solu(nums,target):
    seen={}
    for i,num in enumerate(nums):
        need=target-num
        if need in seen:
            return [seen[need],i]#Pehle wale number ka indexCurrent number ka index
        seen[num]=i
        
print(opti_solu([1,2,3,5,6,7,8],9))