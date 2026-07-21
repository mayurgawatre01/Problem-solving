def largest(arr):
    maximum=arr[0]
    for num in arr:
        if maximum<num:
            maximum=num
    return maximum
print(largest([2,5,1,3,0]))

        