
'''
98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(self, root: TreeNode) -> bool:
'''


class Solution(object):
    def isValidBST(self, root):
        # recursion
        def helper(node, lower, upper):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))

        # def isValidBST(self, root: TreeNode) -> bool:
        #     return self.helper(root, float('-inf'), float('inf'))
        # def helper(self, node, lower, upper):
        #     if not node:
        #         return True
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False
        #     if not self.helper(node.right, val, upper):
        #         return False
        #     if not self.helper(node.left, lower, val):
        #         return False
        #     return True


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isValidBST([5, 1, 4, null, null, 3, 6]))
