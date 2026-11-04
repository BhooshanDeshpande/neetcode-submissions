# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        if not head:
            return False

        while head.next and fast and fast.next:
            fast = fast.next.next
            if fast == head:
                return True
            head = head.next

        return False

        