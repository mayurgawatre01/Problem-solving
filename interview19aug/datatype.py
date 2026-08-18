a = [1, 2, 3]
b = a

b[0] = 100

print(a)
print(b)


def add(a,b):
    return a+b

print(add(10,34))

def mult(x,v):
    return x*v
x=mult(5,4)
print(x)
print(x+10)

def test(x):
    x=x+10
    return x
a=5
print(test(a))
print(a)