s = "abc123xyz45"

result=""
for ch in s:
    if ch.isdigit():
        result=result+ch
print(result)