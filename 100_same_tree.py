'''
100. Same Tree
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

100. Same Tree
'''

'''
approach:
    brute force
        check every possible prefix of that string in dictionarym if found, call for remaining portion
        TC: O(n^n), SC: O(n)
    dynamic programming
        TC: O(n^2), SC: O(n)
        divide the problem into multiple subproblems of string s1 and s2
        if substrings are in the dict, then mark that position as true 
'''


class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
        # returns True if p==None and q==None else False

        # lengthier
        # p and q are both none
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isSameTree([1, 2, 3], [1, 2, 3]))
