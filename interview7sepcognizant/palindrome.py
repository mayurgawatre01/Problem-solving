S="madaooppppppppp"
rev=S[::-1]
if S==rev:
    print("it is palindrom")
else:
    print("not an palindrome")
    
    
#witghout slicng 

X="mam"
rev=""
for ch in X:
    rev=ch+rev
    
if X==rev:
    print("it is an palindrome")
else:
    print("not an palindorm")