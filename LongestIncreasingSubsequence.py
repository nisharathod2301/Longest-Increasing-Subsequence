class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Using Depth First search caching, Dynamic Programming
        countseq=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    countseq[i] = max(countseq[i], 1 + countseq[j])
        return max(countseq)
        
