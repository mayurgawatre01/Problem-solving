arr = [10, 25, 35, 45, 50]

target=30

for num in range(len(arr)):
    if arr[num]==target:
        print("found")
        break
else:
    print("not found")
        