'''
108. Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
'''

'''
essentially creating BST from Inorder traversal
'''


class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right:
                # no elements available for that subtree
                return None
            p = (left+right)//2
            # taking the middle left element
            root = TreeNode(nums[p])
            # recursively compute the left and right subtrees
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)
            return root
        return helper(0, len(nums)-1)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
