def contains_duplicate(arr):
    seen=set()
    for num in arr:
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False
    
    
print(contains_duplicate([10,20,10,20,30,30,40,90,90]))