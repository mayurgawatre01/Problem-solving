S="hello my name is mayur gawatre . my mother name is maya "

freq={}
for ch in S.split():
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)
        