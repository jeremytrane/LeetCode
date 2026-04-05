# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = head = ListNode()
        while l1 or l2 or carry:
            value1, value2 = 0, 0
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next
            total = value1 + value2 + carry
            head.next = ListNode(total%10)
            carry = total//10
            head = head.next
        return dummy.next