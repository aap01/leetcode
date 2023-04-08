# Remove Duplicates from Sorted List
#
# [Easy] [AC:50.6% 1.2M of 2.3M] [filetype:python3]
#
# Given the head of a sorted linked list, delete all
# duplicates such that each element appears only once. Return
# the linked list sorted as well.
#
# Example 1:
#
# Input: head = [1,1,2]
#
# Output: [1,2]
#
# Example 2:
#
# Input: head = [1,1,2,3,3]
#
# Output: [1,2,3]
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
class ListNode:
    def __init__(
        self,
        val=0,
        next=None,
    ):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        cur = head
        while cur:
            next = cur.next
            while next and next.val == cur.val:
                cur.next = next.next
                next = cur.next
            cur = cur.next
        return head
