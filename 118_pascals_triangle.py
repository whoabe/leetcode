'''
118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows):
        '''
        approach
            makes a row for range(numRows), the 0 and -1th term are 1,1
            for the other values, calculate using the row on top and previous value
        '''
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
        return triangle

        # # alternative method
        # pascal = [[1]*(i+1) for i in range(numRows)]
        # # create the triangle and fill with all 1s
        # for i in range(numRows):
        #     for j in range(1, i):
        #         # loop through the cells and calculate them accordingly
        #         pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        # return pascal


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.generate(5))
