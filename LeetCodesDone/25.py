# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        d = ListNode(0)
        d.next = head
        gp = d
        while True:
            kth = gp
            for i in range(k):
                kth = kth.next
                if not kth:
                    return d.next
            gn = kth.next
            kth.next = None
            gp.next = reverseLinkedList(gp.next, gn)
            gp = gp.next
            while gp.next:
                gp = gp.next
            gp.next = gn