'''
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        approach:
            iterative
                save the next pointer, reverse, advance pre and cur
            recursive
        """
        # iterative
        # initialize pointers
        pre = None
        cur = head
        next = None
        while cur:
            # save next
            next = cur.next
            # reverse
            cur.next = pre
            # advance pre and cur
            pre = cur
            cur = next
        # new head at end
        return pre

        # recursive
        # base case
        if not head or not head.next:
            return head
            # going down
        reversedHead = self.reverseList(head.next)
        # reverse the head
        head.next.next = head
        # set next to None
        head.next = None
        return reversedHead


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.removeNthFromEnd(5))
