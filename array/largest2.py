arr = [10, 5, 8, 20, 3]
max=arr[0]

for num in arr:
    if num > max:
        max=num
print(max)


arr2 = [10, 5, 8, 20, 3]

max=float("-inf")
second=float("-inf")

for num in arr:
    if num > max:
        second=max
        max=num
        
    elif num > second and num!=max:
        second=num
print(max,second)

#Q3 — Check if Array Is Sorted

arr = [1, 90, 3, 4, 5]
x=len(arr)
for i in range(0,x-1):
    if arr[i]>arr[i+1]:
        print("not sorted")
        break
else:
    print("sorted")
    


#Q4 — Remove Duplicates from Sorted Array


x = [1, 1, 2, 2, 3, 4, 4]
i=0
for j in range(1,len(x)):
    if x[j]!=x[i]:
        i+=1
        x[j]=x[i]
k=i+1

print(k)
print(arr[:k])