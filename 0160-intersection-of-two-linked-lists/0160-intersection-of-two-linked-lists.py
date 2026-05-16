# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        
        a = headA
        b = headB

        while a != b:

            # If a becomes None, move to headB
            if a:
                a = a.next
            else:
                a = headB

            # If b becomes None, move to headA
            if b:
                b = b.next
            else:
                b = headA

        return a