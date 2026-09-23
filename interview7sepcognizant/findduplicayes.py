arr=[10,20,20,30,10,30,20,10,40,50,60]

seen=[]

dup=[]

for num in arr:
    
    if num in seen:
        
        if num not in dup:
            dup.append(num)
    
    else:
        seen.append(num)
print(seen)
print(dup)