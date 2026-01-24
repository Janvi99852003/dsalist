# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        temp = head

        # count nodes
        while temp is not None:
            c += 1
            temp = temp.next

        steps = c - n

        # if removing the first node
        if steps == 0:
            return head.next

        temp = head
        for _ in range(steps - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head
