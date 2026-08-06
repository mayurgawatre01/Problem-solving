def largest_no(nums):
    largest=float("-inf")
    for num in nums:
        if num > largest:
            largest=num
    return largest
print(largest_no([12,34,45,67,43,21]))