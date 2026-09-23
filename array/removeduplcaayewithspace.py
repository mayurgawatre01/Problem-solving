
arr = [1, 1, 2, 2, 3, 4, 4]

i = 0

for j in range(1,len(arr)):
    if arr[i]!=arr[j]:
        i+=1
        arr[i]=arr[j]
k=i+1
print(k)
print(arr[:k])