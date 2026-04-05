# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        first = second = head
        prevGroup = dummy

        while True:

            for _ in range(k-1):
                if not second:
                    return dummy.next
                second = second.next

            if not second:
                return dummy.next

            nextGroup = second.next
            prev, curr = nextGroup, first
            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            prevGroup.next = prev
            prevGroup = first
            first = second = nextGroup

            