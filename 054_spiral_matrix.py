'''
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        '''
        approach:
            Traverse through the matrix, if we hit an edge or something in the seen collection, rotate direction by 90 degrees
            r,c = current row and column
            di is the direction 
            dr,dc are the potential directions that row and column can go in
        '''
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        # iterate through the number of cells in R*C
        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr = r + dr[di]
            cc = c + dc[di]
            # check if next row or next col are at the edge or if theyre not in seen
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di+1) % 4
                r = r+dr[di]
                c = c+dc[di]
        return ans

        '''
        approach 2:
            get the first row + the spiral order of the rotated (reversed and transpose) matrix
        '''
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
