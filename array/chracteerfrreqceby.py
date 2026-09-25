x="i love python"

freq={}

for ch in x:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]+=1
print(freq)



    