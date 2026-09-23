arr=[-10,-20,-30,-40,-50,-909900,-343434]
largest=arr[0]
for num in arr:
    if num > largest:
        largest=num
print(largest)

#built in fucnion

print(max(arr))