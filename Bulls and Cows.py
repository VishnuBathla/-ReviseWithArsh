class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        undone={}
        for i in range(len(guess)):
            if(guess[i]==secret[i]):
                bulls+=1
            else:
                undone[secret[i]]=undone.get(secret[i],0)+1
        for i in range(len(guess)):
            if(guess[i]!=secret[i]):
                if(guess[i] in undone and undone[guess[i]]>0):
                    cows+=1
                    undone[guess[i]]-=1
        return f'{bulls}A{cows}B'
