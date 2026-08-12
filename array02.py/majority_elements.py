def majority(nums):
    freq={}
    for x in nums:
        if x not in freq:
            freq[x]=1
        else:
            freq[x]+=1
    for x in freq:
        if freq[x]>len(nums)//2:
            return x
            
print(majority([3,2,3]))