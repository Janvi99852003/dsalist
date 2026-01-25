# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # 1. Find middle (end of first half)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse second half
        prev, curr = None, slow.next
        slow.next = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3. Merge
        first = head
        second = prev
        
        while second:
            t1 = first.next
            t2 = second.next
            
            first.next = second
            second.next = t1
            
            first = t1
            second = t2