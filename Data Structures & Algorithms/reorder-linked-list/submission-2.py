# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        #Split array in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        #Reverse second array
        prev, curr = None, second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        second = prev

        curr = head
        while second:
            tmp1 = curr.next
            tmp2 = second.next

            curr.next = second
            second.next = tmp1

            curr = tmp1
            second = tmp2