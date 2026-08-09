n=int(input())
for i in range(0,n):
    #space
    for j in range(0,i):
        print(" ",end=" ")
    
    #stars
    for j in range(0,2*n-(2*i+1)):
        print("*",end=" ")
    
    
    #space right
    for j in range(0,i):
        print(" ",end="")
    print()