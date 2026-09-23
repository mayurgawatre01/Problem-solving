arr=[10,20,30,40,10,60,70]
target=10

low=0
high=len(arr)-1
while low <=high:
    mid=(low+high)//2
    if arr[mid]==target:
        print("found")
        break
    elif target > arr[mid]:
        low=mid+1
    else:
        high=mid-1
else:
    print("not found")
        