arr=[1,2,3,4,4,4,4,3,21,1,5,6]

seen=set()
duplicate=set()

for num in arr:
    if num not in seen:
        seen.add(num)
    else:
        duplicate.add(num)
    
print(seen)
print(duplicate)
        