'''
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        approach:
            1. copy into array list and then check reverse
            2. reverse second half in place
        """
        # 1 copy into array list
        vals = []
        while head:
            vals += head.val,
            # head.val is a single element tuple
            #alternative is vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

        # 2
        # reverse the first half while finding the middle
        # compare the reversed first half with the second half
        rev = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isPalindrome(1, 2))
