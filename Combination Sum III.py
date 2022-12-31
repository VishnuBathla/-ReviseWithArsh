def do(k,su,need,done,start):
    if(k==0 and su==need):
        return [list(done)]
    ans=[]
    for i in range(start,10):
        if(i not in done):
            if(su+i<=need):
                done.add(i)
                ans+=do(k-1,su+i,need,done,i+1)
                done.remove(i)
    return ans
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return do(k,0,n,set(),1)
