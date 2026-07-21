def second(arr):
    largest=-1
    second=-1
    for num in arr:
        if num > largest :
            second=largest
            largest=num
        elif num > second and num !=largest:
            second=num
    return second
           
print(second([12,34,45,65,78]))