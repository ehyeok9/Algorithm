# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode()
        prev = node
        flag = False
        
        while l1 or l2:
            cur = ListNode()
            
            if l1 is None:
                cur.val = l2.val
            elif l2 is None:
                cur.val = l1.val
            else:
                cur.val = l1.val + l2.val
                
            if flag:
                cur.val += 1
                flag = False
                
            if cur.val >= 10:
                cur.val -= 10
                flag = True
                
            prev.next = cur
            prev = cur
            
            if l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
            
        
        if flag:
            prev.next = ListNode(1)
            
        node = node.next
        
        return node