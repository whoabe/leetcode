'''
143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

def reorderList(self, head: ListNode) -> None:
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head):
        """
        approach:
            find the middle of the LL, if 2 middle nodes, return 2nd middle
            split into 2 LLs at the middle node
            reverse the 2nd LL
            merge the 2 LLs
        """
        #  check for empty LL
        if not head:
            return
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow is the middle node
        # reverse the 2nd LL
        pre, cur = None, slow
        while cur:
            # cur.next, pre, cur = pre, cur, cur.next
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # merge the lists
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.reorderList([1, 2, 3, 4]))
