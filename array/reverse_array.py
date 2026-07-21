def reverse_array(arr):
    rev=[]
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
print(reverse_array([1,2,3,4]))