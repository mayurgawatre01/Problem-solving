arr=[1, 2, 2, 3, 4, 4, 5]

seen=set(arr)
print(seen)


#without set
arr = [1, 2, 2, 3, 4,1000, 4, 5]

x=[]
for num in arr:
    if num not in x:
        x.append(num)
print(x)