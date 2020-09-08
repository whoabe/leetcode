'''
73. Set Matrix Zeroes
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

def setZeroes(self, matrix: List[List[int]]) -> None:
'''


class Solution(object):
    def setZeroes(self, matrix):
        '''
        approach:
            look for zero entires
            if we find entry that is equal to 0, then record it into the rows set and the cols set
            loop over the matrix, and if the cell is in the row or col set, then set value to 0
        TC: O(MxN) where M and N are the number of rows and columns
        SC: O(M + N) since we use 2 sets to keep track 
        '''
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return matrix

        '''
        approach:
            Use first row or col to mark if there's a 0 in that row or col
        TC: O(MxN) 
        SC: O(1)
        '''
        R = len(matrix)
        C = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # iterate through matrix to mark the zero row and cols
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, R):
            for col in range(1, C):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]

        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(C):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(R):
                matrix[row][0] = 0
        return matrix


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
