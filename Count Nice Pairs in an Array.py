class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            k=i-int(str(i)[::-1])
            a[k]=a.get(k,0)+1
        ans=0
        for i in a:
            ans+=(a[i]*(a[i]-1)//2)
        return ans%1000000007
