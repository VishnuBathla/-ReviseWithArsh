class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        a={}
        for i in nums:
            x=[]
            for j in a:
                if(j%i==0):
                    if(len(a[j])>len(x)):
                        x=a[j]
            a[i]=[i]+x
        x=[]
        for i in a:
            if(len(a[i])>len(x)):
                x=a[i]
        return x
