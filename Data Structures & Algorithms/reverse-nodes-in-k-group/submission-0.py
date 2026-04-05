# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:            

        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            Kth = self.getKth(prevGroup, k)
            if not Kth:
                break
            groupNext = Kth.next

            prev, curr = groupNext, prevGroup.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevGroup.next
            prevGroup.next = Kth
            prevGroup = tmp
        return dummy.next

    def getKth(self, root, k):
        for _ in range(k):
            if root.next:
                root = root.next
            else:
                return None
        return root