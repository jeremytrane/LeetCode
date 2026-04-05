# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head

        node = slow = head 
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow.next
        slow.next = None

        curr, prev = start, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # [node, ..., slow] [prev, ..., start]
        while node and prev:
            temp1 = node.next
            temp2 = prev.next

            node.next = prev
            node = temp1

            prev.next = node
            prev = temp2

