
'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution:
    def generate(self, rowIndex):
        '''
        approach 1
            makes a row for range(numRows), the 0 and -1th term are 1,1
            for the other values, calculate using the row on top and previous value
            return the last array, which contains the row
            TC is O(n^2), SC is also O(n^2)
        '''
        # triangle = [[1]*(i+1) for i in range(rowIndex+1)]
        # # create the triangle and fill with all 1s
        # for i in range(2, rowIndex+1):
        #     for j in range(1, i):
        #         # loop through the cells and calculate them accordingly
        #         triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        # return triangle[-1]

        '''
        approach 2
            realize that DP can be used
            use memoization to reduce the memory
            create an empty array with 1 as the first value
            loop through the rows, each time create a copy of the current res array
            calculate the value of the index in the row using pre-the array copy
        '''
        res = [0] * (rowIndex+1)
        res[0] = 1
        for i in range(1, rowIndex+1):
            pre = res[:]
            # [:] returns a shallow copy of the array
            for j in range(1, i+1):
                res[j] = pre[j-1] + pre[j]
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.generate(3))
