def do(arr):
    i=0
    su=[0]
    done={0}
    fl=0
    sp=-1
    st=-1
    for i in range(len(arr)):
        if(su[-1]+arr[i] in done ):
            sp=su[-1]+arr[i]
            st=i
            fl=1
            break
        else:
            su.append(su[-1]+arr[i])
            done.add(su[-2]+arr[i])
    if(fl==1):
        ko=su.index(sp)
        return arr[:ko]+arr[i+1:],1
    return arr,0


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        while(head!=None):
           a.append(head.val)
           head=head.next
        while(0 in a):
            del a[a.index(0)]
        fl=1
        while(fl==1):
            a,fl=do(a)
        if(a):
            t=ListNode(a.pop(0))
            o=t
            while(a):
                o.next=ListNode(a.pop(0))
                o=o.next
            return t
        return None
