'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        while l1 and l2:
            if l1.val < l2.val:
                cur,

                # NOT DONE


if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists((1 -> 2 -> 4), (1 -> 3 -> 4)))
