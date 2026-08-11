def remove_duplicates(nums):
    seen=set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            pass
    return seen
print(remove_duplicates([11,11,22,23,33,23,45,45,45,56,56,56,78]))


#optimized solution

def opti(nums):
    i=0
    j=1
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return nums
print(opti([1,2,2,4,4,5,6,6,7,8,8,9]))