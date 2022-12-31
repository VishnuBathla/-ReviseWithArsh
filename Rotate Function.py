class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)):
            a+=i*nums[i]
        n=len(nums)
        cursum=a
        run=sum(nums)
        prev=0
        for i in range(n):
            run=run-nums[i]
            cursum=cursum-run+nums[i]*(n-1)-prev
            prev+=nums[i]
            a=max(a,cursum)
        return a
