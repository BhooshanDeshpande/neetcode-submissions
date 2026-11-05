# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev, curr = None, head
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr 
            curr = t
        
        curr, tail = prev, prev 
        count = 1
        while curr:
            if count == n:
                if prev == curr:
                    tail = tail.next
                else:
                    prev.next=curr.next
                break
            prev = curr
            curr = curr.next
            count += 1
        
        prev, curr = None, tail
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr 
            curr = t
        
        return prev