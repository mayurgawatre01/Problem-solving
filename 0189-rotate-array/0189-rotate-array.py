class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n=len(nums)
        k=k%n
        nums[:]=reversed(nums[:])   
        nums[0:k]=reversed(nums[0:k]) 
        nums[k:]=reversed(nums[k:])