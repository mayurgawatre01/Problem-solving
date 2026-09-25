x="mayurgAwAtre"

total=0

consonant=0

for ch in x.lower():
    if  ch in "aeiou":
        total+=1
    else:
        consonant+=1
print(total)
print(consonant)