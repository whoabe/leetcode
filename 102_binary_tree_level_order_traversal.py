
'''
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(self, root: TreeNode) -> List[List[int]]:
'''


class Solution(object):
    def levelOrder(self, root):
        '''
        check if root is empty
        initialize ans and level
        level is an array that has the values of all the nodes at the current level
        append the values in level to ans
        then for each node in level, add their children ~basically setting up for next iteration
        '''
        # empty case
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

        # solution 2
        '''
        DFS + recursion: TC: O(N) each node processed once, SC: O(N) 
            initialize res and level
            if len(res) which is basically level < level +1, then append [], which is setting up for the next level
            go into the res level and append the root values
            call the root's left and right recursively
        '''

    def levelOrder(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)

    # recursion alternative
    def levelOrder(self, root):
        res = []

        def helper(node, level):
            if node:
                if len(res) == level:
                    res.append([])
                res[level] += [node.val]
                helper(node.left, level+1)
                helper(node.right, level+1)
        helper(root, 0)
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.levelOrder([3, 9, 20, null, null, 15, 7]))
