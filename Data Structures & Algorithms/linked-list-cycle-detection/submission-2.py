# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## hset

        # hset = set()
        # curr = head
        # while curr:
        #     if curr.val in hset:
        #         return True
        #     else:
        #         hset.add(curr.val)
        #     curr = curr.next
        # return False
        
        slow = head
        fast = head

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False







