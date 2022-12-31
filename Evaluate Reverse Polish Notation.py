class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]
        for i in tokens:
            try:
                a=int(i)
                ans.append(f'{i}')
            except:
                x=ans.pop(-1)
                y=ans.pop(-1)
                ans.append(str(int(eval(f'{y+i+x}'))))
        return int(ans[0])
