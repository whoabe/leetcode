'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        approach:
            recursion
                edge case: if either l1 or l2 is null: return the non null list
                otherwise, determine which of l1 and l2 has the smaller head
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        # iteratively TC: O(n+m)
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            # to iterate to the next node
        cur.next = l1 or l2
        # once l1 or l2 is empty, need to add the remaining node
        return dummy.next
        # return from the first node


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.mergeTwoLists((1, 2, 4), (1, 3, 4)))
