# Remove Duplicates from Sorted List II
#
# [Medium] [AC:45.9% 592.3K of 1.3M] [filetype:python3]
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
#
# Example 1:
#
# Input: head = [1,2,3,3,4,4,5]
#
# Output: [1,2,5]
#
# Example 2:
#
# Input: head = [1,1,1,2,3]
#
# Output: [2,3]
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 300].
#
# -100 <= Node.val <= 100
#
# The list is guaranteed to be sorted in ascending order.
#
# [End of Description]:


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = ListNode()
        node.next = head
        cur = node

        while cur:
            if cur.next and cur.next.next and (cur.next.val == cur.next.next.val):
                temp = cur.next.next
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                cur.next = temp.next
            else:
                cur = cur.next
        return node.next
