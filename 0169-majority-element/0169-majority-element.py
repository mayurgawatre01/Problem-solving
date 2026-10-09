class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        n=len(nums)

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums:
            if freq[num]>n//2:
                return num
        