# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        node=headA
        lenA=0
        while node!=None:
            lenA=lenA+1
            node=node.next
            
        node=headB
        lenB=0
        while node!=None:
            lenB=lenB+1
            node=node.next
  
        
        while lenA > lenB:
            headA=headA.next
            lenA=lenA-1
        
        while lenB > lenA:
            headB=headB.next
            lenB=lenB-1
        
        while headA!=headB:
            headB=headB.next
            headA=headA.next
            
        return headA
        
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,ListNode):
            prev=None
            curr=ListNode
            fast=curr.next
            
            while fast!=None:
                curr.next=prev
                prev=curr
                curr=fast
                fast=fast.next
            curr.next=prev
            return curr
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None: return
        slow=head
        fast=head
        
        # Gets the midpointer of the list
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        fast =self.reverse(slow.next)
        slow.next=None
        
        slow=head
        
        while fast!=None:
            curr = slow.next
            slow.next=fast
            fast=fast.next
            slow.next.next=curr
            slow=curr
