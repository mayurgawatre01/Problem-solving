def second_smallest(nums):
    smallest=nums[0]
    second_small=max(nums)
    for num in nums:
        if num < smallest:
            second_small=smallest
            smallest=num
        elif num < second_small and num!=smallest:
            second_small=num
    return second_small
print(second_smallest([12,32,4342,90,3]))
print(second_smallest([5, 1, 4, 2, 3])) 










def second_smallest(arr):
    smallest=float("inf")
    second_sm=float("inf")
    for num in arr:
        if num < smallest:
            second_sm=smallest
            smallest=num
        elif num !=smallest and second_sm > num :
            second_sm=num
            
    return second_sm
print(second_smallest([5,1,12,4,3]))


def second_largest(nums):
    largest=float("-inf")
    second_large=float("-inf")
    for num in nums:
        if num > largest:
            second_large=largest
            largest=num
        elif num!=largest and num > second_large:
            second_large=num
    return second_large

print(second_largest([20,30,43,432]))