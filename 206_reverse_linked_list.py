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
        # base case. a single node is a reversed list
        if not head or not head.next:
            return head
        # going down list, calling reverseList w the next node
        reversedHead = self.reverseList(head.next)
        # setting the next node's next to head
        head.next.next = head
        # set next node of the head to None
        head.next = None
        return reversedHead
        # return the reversedHead to be called in the reverseList function


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.removeNthFromEnd(5))
