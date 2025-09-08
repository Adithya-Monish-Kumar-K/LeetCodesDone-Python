# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        v=list()
        for i in lists:
            while i:
                v.append(i.val)
                i=i.next
        if not v:
            return None
        v.sort()
        d=ListNode(0)
        c=d
        for j in v:
            c.next=ListNode(j)
            c=c.next
        return d.next
