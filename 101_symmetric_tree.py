
'''
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(self, root: TreeNode) -> bool:
'''


class Solution(object):
    # def isSymmetric(self, root):
    #     # recursion
    #     return self.isMirror(root, root)

    # def isMirror(self, left, right):
    #     if not left and not right:
    #         return True
    #     if not left or not right:
    #         return False
    #     return (left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left))

    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left))
        return isMirror(root, root)

        # iterative
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isSymmetric([1, 2, 2, 3, 4, 4, 3]))
