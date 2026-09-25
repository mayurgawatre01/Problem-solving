arr=[1,2,3,5]
n=len(arr)+1
expected=n*(n+1)//2

actual=0

for num in arr:
    actual+=num
print(actual)

print(expected)

missing=expected-actual

print(missing)