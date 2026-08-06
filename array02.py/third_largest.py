def third_largest(nums):
    if len(nums)<3:
        return -1
    largest=float("-inf")
    second=float("-inf")
    third=float("-inf")
    for num in nums:
        if num > largest:
            third=second
            second=largest
            largest=num
        elif num > second:
            third=second
            second=num
        elif num > third and num !=second:
            third=num
            
    return largest,second,third
print(third_largest([10,12,15,34,45]))