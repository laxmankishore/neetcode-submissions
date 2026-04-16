# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLen(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        lengthA = getLen(headA)
        lengthB = getLen(headB)

        l1, l2 = None, None
        if lengthA <= lengthB:
            l1 = headA # l1 -> list with min length
            l2 = headB
        else :
            l1 = headB
            l2 = headA
        diff = abs(lengthA - lengthB)
        while diff > 0:
            l2 = l2.next
            diff -= 1

        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        
        return l1





        



        