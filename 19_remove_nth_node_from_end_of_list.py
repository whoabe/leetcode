'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        approach:
            one pass 2 pointers
            fast and slow pointer
                fast and slow pointer start at head
                have fast pointer be n spaces from slow pointer
                then increment fast and slow pointer until fast pointer reaches tail, slow pointer is at n spaces
                set the slow.next to slow.next.next
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.removeNthFromEnd(5))
