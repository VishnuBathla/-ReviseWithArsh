
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a=[]
        s1=[]
        if(root1!=None):
            s1=[root1]
        s2=[]
        if(root2!=None):
            s2=[root2]
        v1=set()
        v2=set()
        while(s1 or s2):
            while(s1 and s1[-1].left!=None and s1[-1].left not in v1):
                v1.add(s1[-1].left)
                s1.append(s1[-1].left)
            while(s2 and s2[-1].left!=None and s2[-1].left not in v2):
                v2.add(s2[-1].left)
                s2.append(s2[-1].left)
            if(s1 and s2):
                if(s1[-1].val>s2[-1].val):
                    p=s2.pop(-1)
                    a.append(p.val)
                    if(p.right!=None and p.right not in v2):
                        v2.add(p.right)
                        s2.append(p.right)
                else:
                    p=s1.pop(-1)
                    a.append(p.val)
                    if(p.right!=None and p.right not in v1):
                        v1.add(p.right)
                        s1.append(p.right)
            elif(s1):
                p=s1.pop(-1)
                a.append(p.val)
                if(p.right!=None and p.right not in v1):
                    v1.add(p.right)
                    s1.append(p.right)
            elif(s2):
                p=s2.pop(-1)
                a.append(p.val)
                if(p.right!=None and p.right not in v2):
                    v2.add(p.right)
                    s2.append(p.right)
        return a
