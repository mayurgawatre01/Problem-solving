def remove_duplicates(nums):
    seen=set()
    for num in nums:
        if num not in seen:
            seen.add(num)
            
    return seen
print(remove_duplicates([11,11,23,23,34,34,44,44]))



def opti(arr):
    i=0
    j=1
    if arr[i]==arr[j]:
        j+=1
    else:
        i+=1
    return i+1
print(opti([1,1,1,2,3,3,3]))