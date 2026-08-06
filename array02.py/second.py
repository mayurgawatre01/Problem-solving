def secondlarge(nums):
    if len(nums)<2:
        return None
    large=float("-inf")
    second=float("-inf")
    for num in nums:
        if num > large:
            second=large
            large=num
        elif num > second and num !=large:
            second=num
    return second
print(secondlarge([12,24,56,78]))