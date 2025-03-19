# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = None
        if not head.next:
            return result
        # find length of the linkedlist
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        # Linked list having at least 2 nodes
        result = ListNode(0, head)
        cur = result
        i = 0
        while i <= l - n:
            if i == l - n:
                cur.next = cur.next.next

            cur = cur.next
            i += 1

        return result.next


# @leet end

