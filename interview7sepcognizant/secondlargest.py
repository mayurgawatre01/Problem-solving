arr=[10,20,3,40,50]

largest=float("-inf")

second=float("-inf")

for num in arr:
    if num > largest:
        second=largest
        largest=num
    if num > second and num!=largest:
        second=num
        
print(largest)
print(second)