def largest(nums):
    large=nums[0]
    for num in nums:
        if num > large:
            large=num
    return large
print(largest([8,9,8982,822,4,53,4334,]))