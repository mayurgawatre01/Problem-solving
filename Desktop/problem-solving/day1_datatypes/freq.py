# P1 - Frequency Counter
# Input: [1, 2, 2, 3, 3, 3, 4]
# Output: {1: 1, 2: 2, 3: 3, 4: 1}

nums = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)