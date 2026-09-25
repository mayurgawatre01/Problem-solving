arr=[2,1,2,2,1,7,8,9,9,9]

freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)