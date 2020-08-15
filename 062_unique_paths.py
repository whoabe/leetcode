'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

def uniquePaths(self, m: int, n: int) -> int:
'''

'''
approach:
    dynamic programming
'''


class Solution(object):
    def uniquePaths(self, m, n):
        '''
        TC: O(m * n)
        SC: O(m * n)
        '''
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]
        can also return dp[m-1][n-1]

        '''
        TC: O(m*n)
        SC: O(n) ~only need to keep the bottom row
        '''
        cur = [1] * n
        for _ in range(1, m):
            for col in range(1, n):
                cur[col] += cur[col-1]
        return cur[-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.uniquePaths(3, 2))
