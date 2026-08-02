def secondlargest(nums):
    large=float("-inf")
    
    slarge=float("-inf")
    for num in nums:
        if num > large:
            slarge=large
            large=num
        elif num > slarge and num !=large:
            slarge=num
      
    return slarge
print(secondlargest([90,89,78,67]))
print(secondlargest([90,-89,-78,-67]))