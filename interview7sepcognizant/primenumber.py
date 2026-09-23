nums=int(input())
if nums <=1:
    print("not prime")
for num in range(2,nums):
    if nums%num==0:
        print("not prime")
else:
    print("prime")
    