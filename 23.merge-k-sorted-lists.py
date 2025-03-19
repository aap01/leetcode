# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def min_val_index(self, lists: List[ListNode]) -> int:
        min_pos = 0
        min_val = lists[0].val
        for i in range(len(lists)):
            if lists[i].val < min_val:
                min_val = lists[i].val
                min_pos = i
        return min_pos

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        cur = None
        # clear empty lists or None nodes
        lists = [item for item in lists if item]

        while lists:
            # position of the listNode with minValue

            min_pos = self.min_val_index(lists=lists)

            # update current pointer
            if not cur:
                cur = lists[min_pos]
            else:
                cur.next = lists[min_pos]
                cur = cur.next

            # update head
            if not head:
                head = cur

            lists[min_pos] = lists[min_pos].next

            if not lists[min_pos]:
                lists.pop(min_pos)

        return head


# @leet end

