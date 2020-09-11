'''
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

def findDuplicate(self, nums: List[int]) -> int:
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findDuplicate(self, nums):
        '''
        approach 1:
            sort() has O(NlogN) worst case time complexity
            TC: O(NlogN)
            SC: if input array cannot be modified, need to allocate linear space for copy of nums and sort that -> O(N). Else O(1)
        '''
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return nums[i]

        '''
        approach 2:
            check if element is in set, else insert element into set
            TC: O(N)
            SC: O(N)
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        '''
        approach 3:
            is using a fast and slow runner, similar to 141: linked list cycle
            TC: O(N)
            SC: O(1)
        '''
        # start hopping from node 0
        slow, fast = 0, 0
        # for locating start node of cycle
        check = 0

        # cycle detection
        while True:
            # slow increments 1
            slow = nums[slow]
            # fast increments 2
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # locate start node of the cycle (duplicate number)
        while True:
            slow = nums[slow]
            check = nums[check]
            if slow == check:
                break
        return check


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))
