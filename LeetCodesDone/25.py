# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        gp = d
        while True:
            kth = gp
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return d.next
            gn = kth.next
            prev, curr = gn, gp.next
            while curr != gn:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tail = gp.next
            gp.next = kth
            gp = tail

