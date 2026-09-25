arr=[2,4,5,7,890,45]
largest=float("-inf")
second=float("-inf")

for num in arr:
    if num > largest:
        second=largest
        largest=num
    elif num > second and num !=largest:
        second=num
if second==float("-inf"):
    print("no second largtest")
else:
    print(second)
print(largest)
print(second)


