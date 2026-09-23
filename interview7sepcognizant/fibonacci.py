n=int(input())
a=0
b=1
c=a+b
for i in range(0,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    